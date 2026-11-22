"""
Experiment 10(b): Implement various types of data visualization.

Aim:
To create bar, line, pie, scatter, and histogram plots using Matplotlib.
"""

import matplotlib.pyplot as plt

# Sample data
subjects = ["Python", "DBMS", "OS", "EVS"]
marks = [85, 90, 75, 80]

# 1. Bar chart
plt.figure()
plt.bar(subjects, marks, color="skyblue")
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 2. Line graph
plt.figure()
plt.plot(subjects, marks, marker="o")
plt.title("Line Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 3. Pie chart
plt.figure()
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()

# 4. Scatter plot
plt.figure()
plt.scatter(subjects, marks, color="red")
plt.title("Scatter Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 5. Histogram
plt.figure()
plt.hist(marks, bins=4, color="green")
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
