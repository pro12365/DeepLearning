from faker import Faker
import pandas as pd
import random

# Initialize Faker to generate fake data
fake = Faker()
# Generate fake data for 50 students
data = []
for _ in range(50):
    name = fake.name()
    student_class = random.randint(1, 12)
    roll_no = fake.random_int(min=1000, max=9999)
    age = fake.random_int(min=16, max=20)
    weight = fake.random_int(min=40, max=100)  # Weight in kilograms
    height = fake.random_int(min=150, max=200)  # Height in centimeters
    data.append({'Name': name, 'Class': student_class, 'Roll No': roll_no, 'Age': age, 'Weight (kg)': weight, 'Height (cm)': height})

# Create a DataFrame from the generated data
df = pd.DataFrame(data)
# Display the generated dataset
print(df)
# Export the dataset to a CSV file
df.to_csv('student_dataset.csv', index=False)
