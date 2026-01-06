from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_data(n=100):
    data = []
    for _ in range(n):
        data.append({
            "id": fake.uuid4(),
            "name": fake.name(),
            "age": random.randint(18, 60),
            "department": random.choice(["HR", "IT", "Finance", "Marketing"]),
            "salary": random.randint(30000, 100000)
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_data(200)
    df.to_csv("data/raw/employees.csv", index=False)

    print("Employee dataset generated and saved to data/raw/employees.csv")
