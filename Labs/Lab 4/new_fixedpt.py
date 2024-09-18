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
       approximations.append(x1)
       if (abs(x1-x0) < tol):
          xstar = x1
          ier = 0
          return [approximations, xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]

def driver():

     f = lambda x: (10 / (x + 4))**(0.5)

     Nmax = 100
     tol = 1e-10

# test f1 '''
     x0 = 1.5
     [approximations, xstar, ier] = fixedpt(f,x0,tol,Nmax)
     print('================================================================')
     print('The approximate fixed point is:',xstar)
     print('')
     print('Num iterations: ', len(approximations))
     print('Iterations: ', approximations)
     print('')
     print('f1(xstar):',f(xstar))
     print('')
     print('Error message reads:',ier)
    
driver()