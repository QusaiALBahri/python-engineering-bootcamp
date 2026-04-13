"""Day 12, Lesson 1: Advanced NumPy Operations"""
import numpy as np

print("=== Advanced NumPy ===\n")

# 1. Matrix Operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

print("\n--- Element-wise operations ---")
print("A + B:\n", A + B)
print("A * B (element-wise):\n", A * B)
print("A @ B (matrix multiplication):\n", np.dot(A, B))

# 2. Linear Algebra
print("\n--- Linear Algebra ---")
print("Transpose of A:\n", A.T)
print("Inverse of A:\n", np.linalg.inv(A))
print("Determinant of A:", np.linalg.det(A))

# 3. Eigenvalues
print("\n--- Eigenvalues ---")
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# 4. Broadcasting
print("\n--- Broadcasting ---")
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([10, 20, 30])
print("Broadcasting:", x + y)

# 5. Reshaping
print("\n--- Reshaping ---")
arr = np.arange(12)
print("Original:", arr)
print("Reshaped (3x4):\n", arr.reshape(3, 4))

# 6. Stacking
print("\n--- Stacking ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("vstack:\n", np.vstack([a, b]))
print("hstack:", np.hstack([a, b]))

print("\n✅ Lesson 1 done!")
