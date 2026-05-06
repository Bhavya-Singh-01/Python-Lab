#Program for Various Types of Visualization in Python
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data.csv")

# -------- Line Plot --------
plt.plot(data['column1'], data['column2'])
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# -------- Bar Chart --------
data['column1'].value_counts().plot(kind='bar')
plt.title("Bar Chart")
plt.show()

# -------- Histogram --------
plt.hist(data['column1'], bins=10)
plt.title("Histogram")
plt.show()

# -------- Scatter Plot --------
plt.scatter(data['column1'], data['column2'])
plt.title("Scatter Plot")
plt.show()

# -------- Pie Chart --------
data['column1'].value_counts().plot(kind='pie')
plt.title("Pie Chart")
plt.show()

# -------- Seaborn Plot (Boxplot) --------
sns.boxplot(x=data['column1'])
plt.title("Box Plot")
plt.show()
