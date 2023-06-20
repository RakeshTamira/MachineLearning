import numpy as np

# 1.a Create a random vector of size 15 with integers in the range 1-20
vector = np.random.randint(1, 21, size=15)

# a.12Reshape the array to 3 by 5
reshaped_array = vector.reshape(3, 5)

# a.2 Print array shape
print("Array shape:", reshaped_array.shape)

# a.3 Replace the max in each row by 0
reshaped_array[np.arange(reshaped_array.shape[0]), np.argmax(reshaped_array, axis=1)] = 0

# Print the modified array
print("Modified array:")
print(reshaped_array)



# Create a 2-dimensional array of size 4 x 3 with 4-byte integer elements
array = np.empty((4, 3), dtype=np.int32)

# Print array shape
print("Array shape:", array.shape)

# Print array type
print("Array type:", type(array))

# Print array data type
print("Array data type:", array.dtype)


# 1.b. Define the square array
array = np.array([[3, -2], [1, 0]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, right_eigenvectors = np.linalg.eig(array)

# Print the eigenvalues
print("Eigenvalues:")
for eigenvalue in eigenvalues:
    print(eigenvalue)

# Print the right eigenvectors
print("\nRight Eigenvectors:")
for i in range(len(right_eigenvectors)):
    print("Eigenvector", i+1, ":", right_eigenvectors[:, i])


# Define the array
array = np.array([[0, 1, 2], [3, 4, 5]])

# 1.c. Compute the sum of the diagonal elements
diagonal_sum = np.trace(array)

# Print the sum of the diagonal elements
print("Sum of diagonal elements:", diagonal_sum)



# 1.d. Define the original array
array = np.array([[1, 2], [3, 4], [5, 6]])

# Reshape the array to 3x2
reshaped_array_1 = array.reshape(3, 2)

# Reshape the array to 2x3
reshaped_array_2 = array.reshape(2, 3)

# Print the original array
print("Original array:")
print(array)

# Print the reshaped arrays
print("\nReshaped array 1 (3x2):")
print(reshaped_array_1)

print("\nReshaped array 2 (2x3):")
print(reshaped_array_2)





# 2.1, 2.2

import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create a pie chart
plt.pie(popularity, labels=languages, autopct='%1.1f%%')

# Add title
plt.title('Popularity of Programming Languages')

# Display the chart
plt.show()


