import numpy as np
import numpy.linalg as la
import math

def driver():
    n = 100
    x = np.linspace(0,np.pi,n)

    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.
    
    f = lambda x: x**2 + 4*x + 2*np.exp(x)
    g = lambda x: 6*x**3 + 2*np.sin(x)
    y = f(x)
    w = g(x)

    # Creating two new, orthogonal vector
    vector1 = [1, 0, 0]
    vector2 = [0, 1, 0]

    # evaluate the dot product of y and w
    dp = dotProduct(y,w,n)
    dp2 = dotProduct(vector1, vector2, 3)

    # print the output
    #print('the dot product is : ', dp)
    #print('The dot product of the new vectors is', dp2)

    mat1 = np.array([[2, 2], [2, 2]])
    mat2 = np.array([3, 3], [3, 3])

    print(testMat)

    return


def dotProduct(x,y,n):
    # Computes the dot product of the n x 1 vectors x and y
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]

    return dp

# Multiply two matrices (list of lists)
def matrixMult(mat1, mat2):
    return

driver()