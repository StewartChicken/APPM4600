import numpy as np



# Would take an array of functions (a system of equations)
    # and return the Jacobian matrix evaluated at the vector of points 'eval_vector'
def evalJacobian(functions, eval_vector):
    pass

# Returns the inverse of a matrix if it is invertible 
def evalInverse(matrix):
    pass

# Returns the vector of solutions evaluated within a system of functions
def evalFunction(functions, eval_vector):
    pass

def SlackerNewton(functions, initial_guess, tol=1e-6, max_iter=100):
    # Evaluate the initial Jacobian and its inverse
    J = evalJacobian(functions, initial_guess)
    J_inv = eval_inverse(J)

    x_n = initial_guess
    
    iterations = 0
    while(iterations < max_iter):
        iterations = iterations + 1

        F = evalFunctions(functions, initial_guess) 
        x_n1 = x_n - Jinv.dot(F)

        if (norm(x_n1 - x_n) < tol):
            return [x_n1, iterations]

        # Todo - check if the most recent iterations are diverging when compared to the previous iteration
        # if it diverges, recalculate the jacobian




def driver():
    functions = [] # Some array of functions - defines the system of equations
    initial_guess = []

    [solution, iterations] = SlackerNewton(functions, initial_guess)

driver()