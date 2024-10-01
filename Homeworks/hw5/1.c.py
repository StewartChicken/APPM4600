import numpy as np

# Define the system of equations F(x)
def F(x, y):
    return np.array([3*(x**2) - y**2, 3*x*(y**2) - x**3 - 1])

# Define the Jacobian matrix J_F(x)
def J_F(x, y):
    return np.array([[6*x, -2*y], 
                     [3*(y**2) - 3*(x**2), 6*x*y]])

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
    return X

# Initial guess
x0 = [1.0, 1.0]

# Solve the system using Newton's method
solution = newtons_method(F, J_F, x0)

# Output the solution
print("Solution:", solution)
