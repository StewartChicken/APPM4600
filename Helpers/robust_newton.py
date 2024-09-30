# import libraries
import numpy as np

# define routines
def bisection(f, fp, fpp, a, b, max_iterations):
    
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
    fb = f(b)
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

    iteration = 0 # Track the number of iterations
    d = 0.5*(a+b) # Midpoint

    while (iteration < max_iterations):
        fn = -( (fp(d)*fp(d) - f(d)*fpp(d)) / (fp(d) ** 2) )

        # Check if the point is within the basin of convergence
        if (fn < 1):
            astar = d
            ier = 0
            return [astar, ier]
        if (fa*fd<0):
            b = d
        else: 
            a = d
            fa = fd
        d = 0.5*(a+b)
        iteration = iteration +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 1
    print("Max iterations reached")
    return [astar, ier]


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

def driver():
    f = lambda x: np.exp(x**2 + 7*x - 30) - 1
    fp = lambda x: (2*x + 7) * np.exp(x**2 + 7*x - 30)
    fpp = lambda x: (2 * np.exp(x**2 + 7*x - 30)) + ((2*x + 7) * (2*x + 7) * np.exp(x**2 + 7*x - 30))

    a = 2
    b = 4.5
    
    Nmax = 100
    tol = 1.e-14

    [astar, ier] = bisection(f, fp, fpp, a, b, Nmax)

    if(ier == 0):
        [p, pstar, info, it] = newton(f, fp, astar, tol, Nmax)

        print('the approximate root is', '%16.16e' % pstar)
        print('the error message reads:', '%d' % info)
        print('Number of iterations:', '%d' % it)
    else:
        print('An error occured')

driver()
