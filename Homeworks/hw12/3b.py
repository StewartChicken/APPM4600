import numpy as np

def hilbert_matrix(n):
    # Construct the Hilbert matrix of size n x n.
    return np.array([[1 / (i + j - 1) for j in range(1, n+1)] for i in range(1, n+1)])

def inverse_power_method(A, tol=1e-8, max_iter=1000):
    """Find the smallest eigenvalue using the inverse power method."""
    n = A.shape[0]
    x = np.ones(n)  # Initial vector
    x = x / np.linalg.norm(x)  # Normalize initial vector
    lambda_old = 0

    for iteration in range(max_iter):
        # Solve A y = x (instead of directly computing A^{-1} x)
        y = np.linalg.solve(A, x)  
        x = y / np.linalg.norm(y)  # Normalize the result
        lambda_new = x.T @ A @ x  # Rayleigh quotient
        
        if abs(lambda_new - lambda_old) < tol:
            smallest_eigenvalue = 1 / lambda_new
            return smallest_eigenvalue, x, iteration + 1
        lambda_old = lambda_new
    
    raise ValueError("Inverse power method did not converge within max_iter iterations")

# Use the inverse power method for n = 16
n = 16
H = hilbert_matrix(n)
smallest_eigenvalue, corresponding_eigenvector, iterations = inverse_power_method(H)
print(f"n = {n}:")
print(f"  Smallest Eigenvalue: {smallest_eigenvalue}")
print(f"  Corresponding Eigenvector: {corresponding_eigenvector}")
print(f"  Iterations: {iterations}")
