# import libraries
import numpy as np
    
# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    approximations = []
    while (count < Nmax):
       count = count + 1
       x1 = f(x0)
       approximations.append(x1) # Append the most recent approximation
       if (abs(x1-x0) < tol):
          xstar = x1
          ier = 0
          return [approximations, xstar,ier] # If the tolerance is acceptable, return the most recent approximation
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    
def driver():

# test functions 
     f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....

     Nmax = 100
     tol = 1e-6

# test f1 '''
     x0 = 0.0
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)

driver()