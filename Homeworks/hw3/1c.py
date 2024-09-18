# import libraries
import numpy as np


# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success
#      itr   - number of iterations
    itr = 1

#     first verify there is a root we can find in the interval 
    
    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier, itr]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, itr]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier, itr]

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
      
    itr = count
    astar = d
    ier = 0
    return [astar, ier, itr]

def driver():

# use routines    
    f = lambda x: 2*x - 1 - np.sin(x)
    a = 0
    b = 1

    tol = 1e-8

    [astar, ier, itr] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))
    print('number of iterations: ', itr)

driver()