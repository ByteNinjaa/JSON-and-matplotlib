import matplotlib.pyplot as plt
import json

with open('student_data.json', 'r') as file:
    data = json.load(file)

# Extracting study hours
study_hours = df['Study']

# Creating the histogram
plt.figure(figsize=(10, 6))
plt.hist(study_hours, bins=5, color='blue', edgecolor='black')
plt.title('Distribution of Study Hours')
plt.xlabel('Study Hours per Week')
plt.ylabel('Number of Students')
plt.grid(True)
plt.show()

#customizing histogram
plt.hist(study_hours, bins=[10, 20, 30, 40, 50], color='green', edgecolor='black')  # Specify exact bin edges
plt.title('Histogram with Custom Bins')
plt.xlabel('Study Hours per Week')
plt.ylabel('Number of Students')
plt.show()
