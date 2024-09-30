import numpy as np



# Define the functions f(x, y) and g(x, y)
def f(x, y):
    return x**2 + y**2 - 4  # Example function

def g(x, y):
    return x*y - 1  # Example function

# Iteration scheme
# f, g are lambda functions
# x0, y0 are initial guesses
def iteration_scheme(f, g, x0, y0, tol=1e-6, max_iter=100):

    # Coefficient matrix
    # Defined for this iteration scheme
    A = np.array([[1/6, 1/18],
                  [0, 1/6]])
    
    # Initial guess
    xn, yn = x0, y0

    # Track num iterations
    iterations = 0

    # Track iteration values
    x_iter = [x0]
    y_iter = [y0]
    
    for n in range(max_iter):

        iterations = iterations + 1

        # Compute f(x_n, y_n) and g(x_n, y_n)
        F = np.array([f(xn, yn),
                      g(xn, yn)])
        
        # Update x_{n+1}, y_{n+1} using the iteration scheme
        x_new, y_new = np.array([xn, yn]) - np.dot(A, F)

        x_iter.append(x_new)
        y_iter.append(y_new)
        
        # Check convergence
        if np.linalg.norm([x_new - xn, y_new - yn]) < tol:
            return [x_new, y_new, x_iter, y_iter, iterations]
        
        # Update for next iteration
        xn, yn = x_new, y_new

    # Max iterations reached
    return [x_new, y_new, x_iter, y_iter, iterations]
    
def driver():

    f = lambda x, y: 3*(x**2) - y**2 
    g = lambda x, y: 3*x*(y**2) - x**3 - 1


    # Initial guesses
    x0, y0 = 1.0, 1.0

    [x_star, y_star, x_iter, y_iter, iterations] = iteration_scheme(f, g, x0, y0)

    #print("The iteration scheme converges to (", x_star, ", ", y_star, ") as a solution to the system\n")
    #print("Number of iterations: ", iterations, "\n")

    print(x_iter)
    print(y_iter)

driver()
