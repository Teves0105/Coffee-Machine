# -*- coding: utf-8 -*-
"""COMP1010-Student-Lab13

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XdBLTJ-XHYV5pDTzLBzfhrs9PNKW5fse

# **COMP1010 - Lab 13 - Python Libraries: NumPy, pandas, and Matplotlib**

### **Introduction to Python Libraries for Data Science**

In this lab, we will introduce you to three essential Python libraries for data science:
- **NumPy**: Used for numerical computations and working with arrays.
- **pandas**: A powerful data manipulation and analysis library.
- **Matplotlib**: A library for creating visualizations.

---

### **1. NumPy: Working with Arrays**

Let's start by importing **NumPy** and creating arrays.
"""

# Importing NumPy
import numpy as np

# Create a 1D array (vector)
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr_1d)

# Create a 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array (Matrix):\n", arr_2d)

"""**Q1**: What is the difference between a 1D array and a 2D array in NumPy?

**Answer**:
In NumPy, the difference between a 1D array and a 2D array lies in their structure and how they store data:

1D Array (Vector):
- Structure: A 1D array is a single-dimensional collection of elements. It is essentially a list of numbers with one axis (axis 0).
- Shape: Its shape is represented as (n,), where n is the number of elements in the array.
- Indexing: In a 1D array, elements are accessed with a single index: arr_1d[i].


2D Array (Matrix):
- Structure: A 2D array is a two-dimensional grid of elements. It has two axes: rows (axis 0) and columns (axis 1).
- hape: Its shape is represented as (m, n), where m is the number of rows and n is the number of columns.
- Indexing: In a 2D array, elements are accessed with two indices: arr_2d[i, j].

---

### **2. Array Operations in NumPy**

NumPy allows you to perform vectorized operations, which are more efficient than traditional loops.
"""

# Element-wise operations

arr_add = arr_1d + 10  # Adding 10 to each element
arr_mul = arr_1d * 2   # Multiplying each element by 2

# TODO: Compute the dot product of arr_1d with itself
# Hint: Use np.dot() to calculate the dot product.
arr_dot = np.dot(arr_1d, arr_1d)  # Fill in this line

print("Array after addition:", arr_add)
print("Array after multiplication:", arr_mul)
print("Dot product of arr_1d with itself:", arr_dot)

"""**Q2**: What does `np.dot()` do? How is it different from simple element-wise multiplication?

**Answer**:

> np.dot() computes the dot product of two arrays.

For 1D arrays (vectors):

- It calculates the sum of the products of corresponding elements.

- Example:

- np.dot([1, 2, 3], [4, 5, 6]) = 1 × 4 + 2 × 5 + 3 × 6 = 32

- np.dot([1, 2, 3], [4, 5, 6])= 1×4+2×5+3×6= 32

For 2D arrays (matrices):
- It performs matrix multiplication, combining rows of the first matrix with columns of the second.
- Example:

- np.dot([[1, 2]], [[3], [4]]) = [[ 1 × 3 + 2 × 4]] = [[11]]
- np.dot([[1, 2]], [[3], [4]])=[[1×3+2×4]]=[[11]]

> How is it different from element-wise multiplication (*)?

| Feature  | np.dot()  | Element-wise Multiplication (*)  |
|--------|--------|--------|
| Operation | Computes dot product or matrix multiplication | Multiplies corresponding elements directly |
| Result for 1D arrays | A single scalar value | An array of the same size as the inputs |
| Result for 2D arrays	 | A new matrix	 | A matrix with element-wise products |
| Example for 1D arrays | np.dot([1, 2], [3, 4]) = 11	 | [1, 2] * [3, 4] = [3, 8]|
| Example for 2D arrays | np.dot([[1, 2]], [[3], [4]]) = [[11]]	 | [[1, 2]] * [[3, 4]] = [[3, 8]]
 |

---

### **3. NumPy Indexing and Slicing**

In NumPy, you can index and slice arrays in a variety of ways.
"""

# Indexing
print("Element at index 2:", arr_1d[2])

# Slicing
print("Sliced Array from index 1 to 3:", arr_1d[1:4])

# Slicing a 2D array
print("Sliced 2D Array (first 2 rows and first 2 columns):\n", arr_2d[:2, :2])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Simple indexing (using integer indexing)
third_column_simple = arr[:, 2]
print(third_column_simple)

# Advanced indexing (using a list of column indices)
column_index_list = [2]
third_column_advanced_list = arr[:, column_index_list]
print(third_column_advanced_list)

"""** *văn bản in nghiêng*Q3**: How does slicing work in NumPy? What does `arr_1d[1:4]` return?

**Answer**:
> How does slicing work in NumPy?

Slicing in NumPy allows me to extract subsets of an array using the syntax:

Syntax: array[start:stop:step]

Where:
- start: The starting index of the slice (inclusive).
- stop: The ending index of the slice (exclusive).
- step: The interval between indices (default is 1).

For multi-dimensional arrays, slicing can be applied independently along each axis by separating slices with commas:

Syntax: array[row_start:row_stop:row_step, col_start:col_stop:col_step]

> What does `arr_1d[1:4]` return?

The code:

"
arr_1d = np.array([1, 2, 3, 4, 5])

sliced_array = arr_1d[1:4] "

How it works:

- 1: Start slicing from index 1 (second element, value 2).
- 4: Stop slicing before index 4 (not including value at index 4).
- The default step is 1.

Result: sliced_array = np.array([2, 3, 4])

---

### **4. pandas: Working with DataFrames**

Now, let’s move on to **pandas** for handling structured data in the form of DataFrames.
"""

# Importing pandas
import pandas as pd

# Creating a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Miami']
}

df = pd.DataFrame(data)
print(df)

"""[văn bản liên kết](https://)**Q4**: What are the main components of a **pandas DataFrame**? How are rows and columns represented?


**Answer**:
> Main Components of a pandas DataFrame

A pandas DataFrame is a two-dimensional, tabular data structure with labeled rows and columns, similar to a spreadsheet or SQL table. The key components of a DataFrame are:

1. Data:

- The actual data stored in a 2D structure, typically in the form of numpy arrays or lists.
- Each column represents a feature, and each row represents an observation or record.
2. Index:

- A set of labels or integers that uniquely identify the rows of the DataFrame.
- By default, pandas assigns an integer-based index starting from 0.
3. Columns:

- Labels for each column in the DataFrame. These are typically strings but can be any hashable type.
- Each column is a pandas Series object, holding data of the same type or mixed types if necessary.

> How Rows and Columns Are Represented

1. Rows:
- Represented by the index of the DataFrame.
- Access individual rows using the .loc[] or .iloc[] methods.
2. Columns:
- Represented by the column labels (keys in the dictionary used to create the DataFrame).
- Access individual columns as pandas Series using bracket notation or dot notation.

---

### **5. DataFrame Operations**

You can perform many useful operations on pandas DataFrames, such as selecting columns, filtering rows, and applying transformations.
"""

# Select a single column
age_column = df['Age']
print("Age Column:\n", age_column)

# TODO: Filter rows where Age is greater than 25
age_above_25 = df[df['Age'] > 25]  # Fill in this line

print("People older than 25:\n", age_above_25)

# Adding a new column
# TODO: Add a 'Salary' column to the DataFrame with values [50000, 60000, 55000, 70000]
df['Salary'] = [50000, 60000, 55000, 70000]  # Fill in this line

print("DataFrame with new 'Salary' column:\n", df)

"""\**Q5**: How do you filter rows in a pandas DataFrame? What is the output of `df[df['Age'] > 25]`?


**Answer**:
> How to Filter Rows in a pandas DataFrame?

Can filter rows in a pandas DataFrame using boolean indexing. This involves creating a condition that evaluates to True or False for each row, and then using that condition to select the rows where the condition is True.


> Filtered Result of df[df['Age'] > 25]

| Name  | Age  | City  |
|--------|--------|--------|
| Bob | 27 | Los Angeles |
| David | 32 | Miami |

---

### **6. Handling Missing Data in pandas**

Real-world data often has missing values. pandas provides tools to handle these missing values.
"""

# Introducing missing data (NaN)
df.loc[2, 'Salary'] = np.nan

# Check for missing values
print("Missing values in DataFrame:\n", df.isnull())

# TODO: Fill missing values in the 'Salary' column with the column mean (use df.fillna())
salary_mean = df['Salary'].mean()  # Calculate the mean of the 'Salary' column
df_filled = df.fillna({'Salary': salary_mean})  # Fill in this line

print("DataFrame with missing values filled:\n", df_filled)

"""**Q6**: How can we handle missing values in a pandas DataFrame? What does `df.fillna()` do?

**Answer**:

> How can we handle missing values in a pandas DataFrame?

To handle missing values in a pandas DataFrame, you can use the .isnull() method to check for NaN values and the .fillna() method to fill those missing values.

- .isnull(): Identifies missing values and returns a boolean DataFrame (True for missing).
- .fillna(): Fills missing values with a specified value or method (e.g., mean, forward fill).


> What does `df.fillna()` do?

The df.fillna() method in pandas is used to fill missing values (NaN) in a DataFrame with a specified value or method.

Key Points:
- Fills missing data: Replaces NaN values with a provided value or calculated value (e.g., mean, median).
- Value: pass a constant, a dictionary, or a Series to fill missing values.
- Method: use forward fill ('ffill') or backward fill ('bfill') to propagate non-missing values.
- Axis: specify whether to fill by rows (axis=0) or columns (axis=1).

---

### **7. Matplotlib: Data Visualization**

Finally, let's explore **Matplotlib** to visualize data. We will create a simple plot of the ages of people in our DataFrame.
"""

# Importing Matplotlib
import matplotlib.pyplot as plt

# TODO: Create a bar plot showing the Age of each person
# Hint: Use plt.bar() with df['Name'] and df['Age'] as inputs
plt.bar(df['Name'], df['Age'])  # Fill in this line
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of People')
plt.show()

"""**Q7**: What kind of plot is generated by the code above? What does `plt.xlabel()` and `plt.ylabel()` do?

**Answer**:

> The code above generates a bar plot. In this plot:

- The x-axis represents the names of people (df['Name']).
- The y-axis represents their ages (df['Age']).

> What does plt.xlabel() and plt.ylabel() do?
- plt.xlabel('Name'): This sets the label for the x-axis. In this case, it labels the x-axis as "Name," indicating that the x-axis represents the names of the individuals.

- plt.ylabel('Age'): This sets the label for the y-axis. In this case, it labels the y-axis as "Age," indicating that the y-axis represents the ages of the individuals.

These functions help to add context and meaning to the axes, making the plot more informative.

---

### **8. Customizing Plots in Matplotlib**

We can customize our plots by changing colors, adding gridlines, and modifying the style.
"""

# Customizing the plot
plt.plot(df['Name'], df['Age'], marker='o', linestyle='-', color='green')
plt.title('Age of People')
plt.xlabel('Name')
plt.ylabel('Age')
plt.grid(True)
plt.show()

"""**Q8**: What do the arguments `marker='o'` and `linestyle='-'` do in the plot?

**Answer**:
The arguments marker='o' and linestyle='-' are used to customize the appearance of a plot in Matplotlib.

> marker='o'
- Marker specifies the shape or symbol that will be used to represent each data point on the plot.
- marker='o' means that each data point will be represented by a circle ('o').

Example: If I have a line plot and use marker='o', each data point will be marked with a circle.

> linestyle='-'
- Linestyle specifies the type of line connecting the data points.
- linestyle='-' means that a solid line will be used to connect the points. Other options for linestyle include:
 '-' for a solid line,

  1. '-' for a solid line,
  2. '--' for a dashed line,
  3. ':' for a dotted line, etc.

---

### **9. Combining NumPy, pandas, and Matplotlib**

Let's put everything together! We will create a simple DataFrame of sales data and plot it using Matplotlib.
"""

# Creating a simple sales DataFrame
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [2500, 3000, 3500, 4000, 4500]
}

df_sales = pd.DataFrame(sales_data)

# Plotting the sales data
plt.plot(df_sales['Month'], df_sales['Sales'], marker='o', color='red', linestyle='--')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.show()

"""**Q9**: What type of plot is generated here? How can you customize the line color or style?

**Answer**:

> Type of Plot is Generated?
- The plot is a line plot with data points marked by circles (marker='o') and a dashed line connecting the points (linestyle='--').
- The x-axis represents the months (df_sales['Month']), and the y-axis represents the sales amounts (df_sales['Sales']).

> Customizing Line Color or Style:
- Customize the line's appearance by modifying the color and linestyle arguments in the plt.plot() function.


*   color='red': Sets the line color to red. Change 'red' to any valid color string (e.g., 'blue', 'green', 'black', or use RGB values like '#FF0000' for red).
*   linestyle='--': Specifies that the line should be dashed. Other options include: '-': solid line, ':': dotted line, '-.': dash-dot line

---

### **10. Additional Resources**

- **NumPy Documentation**: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
- **pandas Documentation**: [https://pandas.pydata.org/pandas-docs/stable/](https://pandas.pydata.org/pandas-docs/stable/)
- **Matplotlib Documentation**: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
- **AI and Data Scientist Roadmap**: [https://roadmap.sh/ai-data-scientist](https://roadmap.sh/ai-data-scientist)
"""