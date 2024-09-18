# import libraries
import numpy as np

# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count < Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]

def driver():

# Function to calculate
    f = lambda x: -np.sin(2 * x) + 5 * x / 4 - 3 / 4

    Nmax = 1000
    tol = 1e-12

    # First root: x = -0.5444424006
    #x0 = 0.0
    # Second root: x = 3.161826486
    #x0 = 2
    # Third root: x = 
    x0 = 4.6

    [xstar,ier] = fixedpt(f,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f1(xstar):',f(xstar))
    print('Error message reads:',ier)

# Second root: x = 
    

driver()