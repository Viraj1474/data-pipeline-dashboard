import streamlit as st
import pandas as pd
import numpy as np
import sweetviz as sv
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Set wide layout for full screen
st.set_page_config(page_title="10-Stage Data Pipeline Dashboard", layout="wide")

st.title(" Data Pipeline Dashboard")

# 1️⃣ File Upload
uploaded_file = st.file_uploader("Upload CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # 2️⃣ Data Summary
    st.subheader("Data Summary")
    col1, col2 = st.columns(2)
    col1.write("Shape:")
    col1.write(df.shape)
    col2.write("Columns:")
    col2.write(df.columns.tolist())
    st.write("Missing Values:\n", df.isnull().sum())
    st.write("Data Types:\n", df.dtypes)

    # 3️⃣ Data Cleaning
    st.subheader("Data Cleaning")
    if st.button("Remove Duplicates"):
        df.drop_duplicates(inplace=True)
        st.success("Duplicates removed!")

    # Fill missing values
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = df.select_dtypes(include='object').columns.tolist()

    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    st.success("Missing values handled!")

    # 4️⃣ Data Visualization
    st.subheader("Feature Visualization")
    feature_to_plot = st.selectbox("Select Feature to Visualize", df.columns)
    if df[feature_to_plot].dtype == 'object':
        plot_df = df[feature_to_plot].value_counts().reset_index()
        plot_df.columns = [feature_to_plot, "count"]
        fig = px.bar(plot_df, x=feature_to_plot, y="count", title=f"Bar Chart of {feature_to_plot}",
                     width=1200, height=600)
    else:
        fig = px.histogram(df, x=feature_to_plot, nbins=30, title=f"Histogram of {feature_to_plot}",
                           width=1200, height=600)
    st.plotly_chart(fig, use_container_width=True)

    # 5️⃣ Correlation Analysis
    st.subheader("Correlation Heatmap")
    numeric_df = df.select_dtypes(include=np.number)
    if not numeric_df.empty:
        corr = numeric_df.corr()
        fig_corr = px.imshow(corr, text_auto=True, title="Correlation Heatmap",
                             width=1200, height=600)
        st.plotly_chart(fig_corr, use_container_width=True)
    else:
        st.info("No numeric columns available for correlation analysis.")

    # 6️⃣ Sweetviz EDA
    st.subheader("Sweetviz Report")
    if st.button("Generate Sweetviz Report"):
        report = sv.analyze(df)
        report.show_html("sweetviz_report.html")
        st.success("Sweetviz report generated as 'sweetviz_report.html'")

    # 7️⃣ Feature Engineering
    st.subheader("Feature Engineering")
    df_encoded = df.copy()
    for col in categorical_cols:
        df_encoded[col] = df_encoded[col].astype(str)
    st.success("Categorical columns converted to string for ML!")

    # 8️⃣ Machine Learning
    st.subheader("Machine Learning")
    target_column = st.selectbox("Select Target Column", df_encoded.columns)
    X = df_encoded.drop(columns=[target_column])
    X = pd.get_dummies(X, drop_first=True)
    y = df_encoded[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    st.text("Classification Report:")
    st.text(classification_report(y_test, y_pred))

    # 9️⃣ Explainable AI (RandomForest Feature Importance)
    st.subheader("Feature Importance")
    importance_df = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)
    fig_imp = px.bar(importance_df.head(20), x="Feature", y="Importance",
                     title="Top 20 Feature Importances", width=1200, height=600)
    st.plotly_chart(fig_imp, use_container_width=True)

    # 🔟 Export & Save
    st.subheader("Export Data")
    if st.button("Save Cleaned Data"):
        df.to_csv("cleaned_data.csv", index=False)
        st.success("Cleaned data saved as 'cleaned_data.csv'")
