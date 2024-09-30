import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt


# Define bisection routine
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier]

# Define newton routine
def newton(f, fp, p0, tol, Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]


# Graph the temperature / depth function
def graph(): 
	# Generate x values for plotting
	x_values = np.linspace(0, x_bar, 1000)  # Range of x from 0 to 2 meters
	f_values = f(x_values)

	# Plot the function f(x)
	plt.plot(x_values, f_values, label=r'$f(x)$')
	plt.axhline(0, color='black', linestyle='--')  # Line at f(x) = 0
	plt.xlabel('Depth (meters)')
	plt.ylabel('f(x) - Temperature (Degrees Celsius)')
	plt.title('Root Finding Problem for Soil Freezing Depth')
	plt.legend()
	plt.grid(True)
	plt.show()

# Run bisection root approximation
def bisection_driver():
	# Define the parameters
	alpha = 0.138e-6  # Thermal diffusivity in m^2/s
	T_i = 20          # Initial temperature in degrees Celsius
	T_s = -15         # Surface temperature in degrees Celsius
	t = 60 * 24 * 3600  # Time in seconds (60 days)

	x_0 = 0 
	x_bar = 2 

	# Approximation tolerance
	tol = 1e-13

	# Define the function
	f = lambda x: (T_i - T_s) * sp.erf(x / (2 * np.sqrt(alpha * t))) + T_s
	
	[astar,ier] = bisection(f, x_0, x_bar, tol)

	print('The bisection approximation of the root is', astar)
	print('The evaluation of the root yields', f(astar))

# Run newton root approximation
def newton_driver():
	# Define the parameters
	alpha = 0.138e-6  # Thermal diffusivity in m^2/s
	T_i = 20          # Initial temperature in degrees Celsius
	T_s = -15         # Surface temperature in degrees Celsius
	t = 60 * 24 * 3600  # Time in seconds (60 days)

	# Startig points
	x_0 = 0.01
	x_1 = 2 # x_bar 

	# Approximation tolerance
	tol = 1e-13
	# Max iterations
	Nmax = 100

	# Define the functions
	f = lambda x: (T_i - T_s) * sp.erf(x / (2 * np.sqrt(alpha * t))) + T_s
	fp = lambda x: ((T_i - T_s) / 1.6916) * (  (2 / np.sqrt(np.pi)) * np.exp(-((x / 1.6916) ** 2))  ) 
	
	[p, pstar, info, it] = newton(f, fp, x_0, tol, Nmax)
	#[p, pstar, info, it] = newton(f, fp, x_1, tol, Nmax)
	print('the approximate root is', pstar)
	print(f(pstar))
	print('the error message reads:', '%d' % info)
	print('Number of iterations:', '%d' % it)

# Main
def driver():
	#bisection_driver()
	newton_driver()

driver()

