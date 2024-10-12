import numpy as np
from numpy.linalg import inv 
from numpy.linalg import norm 

def evalF(x):
	F = np.zeros(3)

	F[0] = x[0] + np.cos(x[0] * x[1] * x[2]) - 1
	F[1] = (1 - x[0])**(0.25) + x[1] + 0.05*(x[2]**2) - 0.15*x[2] - 1
	F[2] = -(x[0]**2) - 0.1*(x[1]**2) + 0.01*x[1] + x[2] - 1

	return F

def evalJ(x):
	J = np.array( [  [1 - x[1]*x[2]*np.sin(x[0] * x[1] * x[2]), -x[0]*x[2]*np.sin(x[0] * x[1] * x[2]), -x[0]*x[1]*np.sin(x[0] * x[1] * x[2])], 
		[(-1/4)*( (1-x[0])**(-3/4) ), 1, 0.1*x[2] - 0.15], 
		[-2*x[0], -0.2*x[1] + 0.01, 1]  ])

	return J

def newton(x0, tol=1e-6, Nmax=100):
	
	for iteration in range(Nmax):
		J = evalJ(x0)
		Jinv = inv(J)
		F = evalF(x0)

		x1 = x0 - Jinv.dot(F)

		#print(x1)

		if(norm(x1 - x0) < tol):
			xstar = x1
			return [xstar, iteration]

		x0 = x1

	xstar = x1
	return [xstar, iteration]

def steepest(x0, tol=1e-6, alpha=0.9, Nmax=100):
    for iteration in range(Nmax):
        # Evaluate the function and the Jacobian (gradient)
        F = evalF(x0)
        grad_F = evalJ(x0).T @ F  # Gradient = J.T @ F
        
        # Update step: x1 = x0 - alpha * gradient
        x1 = x0 - alpha * grad_F
        
        # Print progress
        #print(x1)

        # Check for convergence
        if norm(F) < tol:
            return [x1, iteration]

        # Update the estimate
        x0 = x1

    return [x1, iteration]

def newton_steepest(x):
	[x1, iterations] = steepest(x, Nmax=2000, tol=5e-2)
	[x2, iterations2] = newton(x1)

	return [x2, (iterations + iterations2)]

def driver():
	x = np.array([0.5, 0.5, 0.5])

	[xstar, iteration] = newton(x)

	print("Newton Approximation: ", xstar)
	print("Newton Iterations: ", iteration)

	[x1, iterationS] = steepest(x, Nmax=2000)

	print("Steepest Decent Approximation: ", x1)
	print("Steepest Descent Iterations: ", iterationS)

	[x2, iteration_steepest] = newton_steepest(x)

	print("Newton Steepest Approx: ", x2)	
	print("Newton Steepest Approx: ", iteration_steepest)	

driver()