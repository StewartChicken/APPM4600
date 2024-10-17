import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    f = lambda x: math.exp(x)
    a = 0
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 10
    
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
        fex[j] = f(xeval[j])
      
    plt.plot(xeval, fex, label="Evaluation", color="blue")
    plt.plot(xeval, yeval, label="Interpolation", color="red")
    plt.legend()
    plt.show()   
     
     
    #err = abs(yeval-fex)
    #plt2 = mypkg.my2DPlotB(xeval,err)
    #plt2.show()            

def eval_line(x0, y0, x1, y1, a):
    m = (y1 - y0) / (x1 - x0)
    b = y0 - m*x0

    return a*m + b
    
# xeval are the points that will be evaluated along the x axis
# Nint is the number of intervals
# a, b, are the end points of the interval
# f is the function
# neval is the number of points at which the function is evalutated
def  eval_lin_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)

    #create vector to store the evaluation of the linear splines
    yeval = np.zeros(Neval) 
    
    # For every interval
    for jint in range(Nint):
        #find indices of xeval in interval (xint(jint),xint(jint+1))
        #let ind denote the indices in the intervals
        #let n denote the length of ind

        #temporarily store your info for creating a line in the interval of 
        #interest
        a1 = xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)

        for n in range(jint*10, jint*10+10):
            yeval[n] = eval_line(a1, fa1, b1, fb1, xeval[n])

    return yeval
           
           
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               
