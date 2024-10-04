import numpy as np

# Define the function f(x, y, z) for the ellipsoid
def f(x, y, z):
    return x**2 + 4*(y**2) + 4*(z**2) - 16

# Define the gradient of f (delf)
def grad_f(x, y, z):
    return np.array([2*x, 8*y, 8*z])

# Iteration scheme: x_{n+1} = x_n - (f(x_n) / |delf(x_n)|) * delf(x_n)
def iterate_to_ellipsoid(x0, y0, z0, tol=1e-10, max_iter=100):
    x, y, z = x0, y0, z0

    iteration = 0
    iterations = []
    
    while(iteration < 2):
        iteration = iteration + 1
        grad = grad_f(x, y, z)
        grad_norm = np.linalg.norm(grad)
        f_val = f(x, y, z)

        #print("F evaluation: ", f_val)
        #print("Iteration", (f_val * grad[0]) / grad_norm)
        
        # Update using the iteration scheme
        x_new = x - (f_val * grad[0]) / grad_norm
        y_new = y - (f_val * grad[1]) / grad_norm
        z_new = z - (f_val * grad[2]) / grad_norm

        #print(x_new, y_new, z_new)
        
        iterations.append([x_new, y_new, z_new])
        
        # Check convergence
        if np.linalg.norm([x_new - x, y_new - y, z_new - z]) < tol:
            x = x_new
            y = y_new
            z = z_new
            break

        x = x_new
        y = y_new
        z = z_new
        
    point = [x, y, z]

    return [point, iterations, iteration]
    

# Initial guess
x0, y0, z0 = 1.0, 1.0, 1.0

# Perform the iteration
[point, iterations, iteration] = iterate_to_ellipsoid(x0, y0, z0)

# Output the final point on the ellipsoid
#print("Point: ", point)
#print("Iterations", iterations)
