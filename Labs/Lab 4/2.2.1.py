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


def compute_order(x, xstar):
   print('Computing the order alpha and lambda')
   print('')
   diff1 = np.abs(np.array(x[1:-1]) - xstar) # Contains all p_n+1 values. Excludes the very last value because it = xstar

   diff2 = np.abs(np.array(x[0:-2]) - xstar) # Contains all p_n values

   print("Diff1: ", diff1)
   print("Diff2: ", diff2)

   fit = np.polyfit(np.log(diff2.flatten()), np.log(diff1.flatten()), 1)

   print('Lambda = ', str(np.exp(fit[1])))
   print('Alpha = ', str(fit[0]))


def driver():

     f = lambda x: (10 / (x + 4))**(0.5)

     Nmax = 100
     tol = 1e-10

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
     print('')

     compute_order(approximations, xstar)
    
driver()