import pandas as pd
import json

# Assuming the JSON data is stored in a file named 'student_data.json'
with open('student_data.json', 'r') as file:
    data = json.load(file)

# Convert JSON to DataFrame
df = pd.DataFrame(data)
print(df.head())
