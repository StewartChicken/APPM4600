import numpy as np

# Newton's method for nonlinear systems
def newtons_method(F, J_F, x0, tol=1e-6, max_iter=100):
    X = np.array(x0, dtype=float)
    x = X[0]
    y = X[1]

    for i in range(max_iter):
        # Evaluate the function and Jacobian
        F_val = F(x, y)
        J_F_val = J_F(x, y)
        
        # Solve the linear system J_F(x) * delta_x = -F(x)
        delta_X = np.linalg.solve(J_F_val, -F_val)
        
        # Update the solution
        X = X + delta_X
        
        # Check for convergence
        if np.linalg.norm(delta_X, ord=2) < tol:
            print(f"Converged in {i+1} iterations.")
            return X
    
    print("Maximum iterations reached without convergence.")
    return x

# Define the system of equations F(x)
def F(x, y):
    return np.array([3*(x**2) - y**2, 3*x*(y**2) - x**3 - 1])

# Define the Jacobian matrix J_F(x)
def J_F(x, y):
    return np.array([[6*x, -2*y], 
                     [3*(y**2) - 3*(x**2), 6*x*y]])

# Returns the inverse of a matrix
def invert_matrix(matrix):
    return np.linalg.inv(matrix)

def driver():
    tolerance = 1e-6
    max_iterations = 100

    # Initial guess - x = y = 1
    X = np.array([1, 1])

    iterations = 0
    while(iterations < max_iterations):
        iterations += 1
        
        x, y = X

        F_val = F(x, y)

        # Check if the norm of F(X) is within tolerance (convergence)
        if np.linalg.norm(F_val) < tolerance:
            print(f"Solution found: {X}")
            print("Iterations: ", iterations)
            break

        # Compute the Jacobian matrix J_F(X)
        J_F_val = J_F(x, y)

        # Compute the Newton update: ΔX = J_F_inv(X) * (-F(X))
        delta_X = invert_matrix(J_F_val).dot(-F_val)

        # Update the current solution guess
        X = X + delta_X

        

driver()