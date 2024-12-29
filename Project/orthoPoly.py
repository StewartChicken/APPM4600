import numpy as np
import matplotlib.pyplot as plt

# Returns a list of coefficients for the legendre polynomial of degree 'n'
# 
# Returns these coefficients in order of increasing power of x
# i.e. returning [1, 2, 3] means returning 1 + 2x + 3x^2
def generate_legendre_polynomial(n):
    # Base cases
    # The Legendre polynomial of degree 0 is 1
    # The Legendre polynomial of degree 1 is x
    if n == 0:
        return [1]  
    elif n == 1:
        return [0, 1]  # 0*(1) + 1*(x)

    # Initialize P0 and P1 as lists of coefficients
    # These will be used to start the recursive construction of the Legendre polynomial
    P0 = [1]  
    P1 = [0, 1]  

    # Legendre polynomial obey the following three term recurrence relation
    #
    # (n + 1)*P_{n+1}(x) = (2n + 1)*x*P_n(x) - n*P_{n-1}(x)

    # This loop is used to iteratively generate the nth order Legendre polynomial
    # For each iteration, k is the degree of the polynomial that will be generated
    for k in range(2, n + 1):
        # Start by creating a new list of coefficients for P_k
        P_k = [0] * (k + 1)  # Degree k polynomial has (k+1) coefficients

        # First, for the x-term (2k + 1)*x*P_k(x)
        for i in range(len(P1)):
            P_k[i + 1] += (2 * (k-1) + 1) * P1[i] 

        # Second, for the P_{k-1}(x) term -k*P_{k-1}(x)
        for i in range(len(P0)):
            P_k[i] -= (k-1) * P0[i]  

        # Divide by (k + 1) to obtain the P_{k+1} polynomial explicitly
        P_k = [coef / (k) for coef in P_k]

        # Update P0 and P1 for the next iteration
        P0, P1 = P1, P_k

    # The final P_k is the Legendre polynomial of degree n
    return P_k


# Returns a list of coefficients for the Chebyshev polynomial of degree 'n'
# 
# Returns these coefficients in order of increasing power of x
# i.e. returning [1, 2, 3] means returning 1 + 2x + 3x^2
def generate_chebychev_polynomial(n):
    # Base cases
    # The Chebyshev polynomial of degree 0 is 1
    # The Chebyshev polynomial of degree 1 is x
    if n == 0:
        return [1]  
    elif n == 1:
        return [0, 1]  # 0*(1) + 1*(x)

    # Initialize P0 and P1 as lists of coefficients
    # These will be used to start the recursive construction of the Chebyshev polynomial
    P0 = [1]  
    P1 = [0, 1]  

    # Chebyshev polynomial obey the following three term recurrence relation
    #
    # P_{n+1}(x) = 2*x*P_n(x) - P_{n-1}(x)

    # This loop is used to iteratively generate the nth order Chebyshev polynomial
    # For each iteration, k is the degree of the polynomial that will be generated
    for k in range(2, n + 1):
        # Start by creating a new list of coefficients for P_k
        P_k = [0] * (k + 1)  # Degree k polynomial has (k+1) coefficients

        # First, for the x-term 2*x*P_k(x)
        for i in range(len(P1)):
            P_k[i + 1] += 2 * P1[i]  

        # Second, for the P_{k-1}(x) term -P_{k-1}(x)
        for i in range(len(P0)):
            P_k[i] -= P0[i]  

        # Update P0 and P1 for the next iteration
        P0, P1 = P1, P_k

    # The final P_k is the Legendre polynomial of degree n
    return P_k

# Given the desired family of polynomials and a degree,
# generates the corresponding orthogonal polynomial
#
# Default params:
#  - family: legendre
#  - degree: 3
#
# Returns a list of coefficients for each power of x in ascending order
# i.e. returning [1, 2, 3] means returning 1 + 2x + 3x^2
def generate_orthogonal_polynomial(family="legendre", n=3):
    if family == "legendre":
        return generate_legendre_polynomial(n)
    elif family == "chebychev":
        return generate_chebychev_polynomial(n)
    else:
        raise ValueError(f"Unsupported polynomial family: {family}")


# Given a list of coefficients, returns a lambda function representing the corresponding polynomial
# [1, 2, 3] yields f(x) = 1 + 2x + 3x^2
def lambda_from_coefficients(coeffs):
    def poly_function(x):
        result = 0

        for i, coeff in enumerate(coeffs):
            result += coeff * x ** i

        return result

    return poly_function


def driver():

    # Parameter definitions
    left_bound = -3
    right_bound = 3

    family = "chebychev"
    degree = 6

    xLim = (left_bound, right_bound)
    yLim = (-3, 3)

    steps = 500 # Number of data points

    # Generate the coefficients for a legendre polynomial of degree 4
    coeffs = generate_orthogonal_polynomial(family, degree)
    print(coeffs)

    # Convert the coefficients to a lambda function
    poly_func = lambda_from_coefficients(coeffs)
    
    # Define the x values for plotting
    x_values = np.linspace(left_bound, right_bound, steps)
    y_values = np.array([poly_func(x) for x in x_values])
    
    # Plot the polynomial
    plt.plot(x_values, y_values, label=f'{family} Polynomial of degree {degree}')
    plt.xlabel('x')
    plt.ylabel(f'P_{degree}(x)')
    plt.title(f'{family} Polynomial of Degree {degree}')
    plt.legend()
    plt.grid(True)
    plt.xlim(xLim) 
    plt.ylim(yLim)
    plt.show()

driver()
