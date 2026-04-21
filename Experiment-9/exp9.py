# Import libraries
import numpy as np
import pandas as pd

# --------- NumPy Example ---------
print("NumPy Example:")

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Perform operations
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))


# --------- Pandas Example ---------
print("\nPandas Example:")

# Create a dictionary
data = {
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 78]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# Display basic info
print("Average Marks:", df["Marks"].mean())