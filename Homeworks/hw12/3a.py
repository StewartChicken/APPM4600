import numpy as np

def hilbert_matrix(n):
    # Construct the Hilbert matrix of size n x n.
    return np.array([[1 / (i + j - 1) for j in range(1, n+1)] for i in range(1, n+1)])

def power_method(A, tol=1e-8, max_iter=1000):
    """Implement the power method to find the dominant eigenvalue and eigenvector."""
    n = A.shape[0]
    x = np.ones(n)  # Initial vector
    x = x / np.linalg.norm(x)  # Normalize initial vector
    lambda_old = 0
    
    for iteration in range(max_iter):
        y = A @ x 
        x = y / np.linalg.norm(y)  # Normalize the result
        lambda_new = x.T @ A @ x  # Rayleigh quotient
        
        if abs(lambda_new - lambda_old) < tol:
            return lambda_new, x, iteration + 1
        lambda_old = lambda_new
    
    raise ValueError("Power method did not converge within max_iter iterations")

# Test the power method for n = 4, 8, ..., 20
for n in range(4, 21, 4):
    H = hilbert_matrix(n)
    dominant_eigenvalue, dominant_eigenvector, iterations = power_method(H)
    print(f"n = {n}:")
    print(f"  Dominant Eigenvalue: {dominant_eigenvalue}")
    print(f"  Dominant Eigenvector: {dominant_eigenvector}")
    print(f"  Iterations: {iterations}")
