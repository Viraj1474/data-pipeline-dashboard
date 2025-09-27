import sweetviz as sv
import pandas as pd

# Sample dataframe
df = pd.DataFrame({
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 70000, 80000]
})

# Analyze
report = sv.analyze(df)
report.show_html("sweetviz_report.html")
