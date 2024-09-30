import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Define Newton method subroutine
def newton(f, fp, p0, tol=1e-10, Nmax=100):
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
    it     - number of iterations
     
  """
  p = []
  p.append(p0)
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p.append(p1)
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]


# Define Secant method subroutine
def secant(f, p0, p1, tol=1e-10, Nmax=100):
    """
    Secant iteration.
    
    Inputs:
        f    - function
        p0   - initial guess for root (first point)
        p1   - initial guess for root (second point)
        tol  - iteration stops when p_n, p_{n+1} are within tol
        Nmax - max number of iterations
    Returns:
        p     - an array of the iterates
        pstar - the last iterate
        info  - success message
              - 0 if we met tol
              - 1 if we hit Nmax iterations (fail)
        it    - number of iterations
    """
    p = []
    p.append(p0)
    p.append(p1)
    
    for it in range(Nmax):
        # Calculate next approximation using the secant formula
        p2 = p1 - f(p1) * ((p1 - p0) / (f(p1) - f(p0)))
        p.append(p2)
        
        # Check for convergence
        if abs(p2 - p1) < tol:
            pstar = p2
            info = 0
            return [p, pstar, info, it]
        
        # Update previous points
        p0, p1 = p1, p2

    pstar = p2
    info = 1
    return [p, pstar, info, it]

def driver():

    # Function definitions
    f = lambda x: x**6 - x - 1
    fp = lambda x: 6*(x**5) - 1

    # Initial guesses
    x_0_newton = 2
    x_0_secant = 2
    x_1_secant = 1

    [p_newton, pstar_newton, info_newton, it_newton] = newton(f, fp, x_0_newton)

    newton_errors = [p - pstar_newton for p in p_newton]
    newton_errors = newton_errors[0:-1] # Make sure error corresponds to each iteration including first
    
    #print("\nNewton's method iterations: ", p_newton, "\n")
    #print("Newton's method errors: ", newton_errors, "\n")
    #print("Newton's method root: ", pstar_newton)
    #print("Newton's method iterations: ", it_newton)

    [p_secant, pstar_secant, info_secant, it_secant] = secant(f, x_0_secant, x_1_secant)

    secant_errors = [p - pstar_secant for p in p_secant]
    secant_errors = secant_errors[0:-2]

    #print("\n\nSecant method iterations: ", p_secant, "\n")
    #print("Secant method errors: ", secant_errors, "\n")
    #print("Secant method root: ", pstar_secant)
    #print("Secant method iterations: ", it_secant)


    '''
    # Create the index array
    iterations = np.arange(1, 10)

    # Make newton errors list the same length as the secant list
    newton_errors.append(np.nan)


    # Set up the figure and axis
    fig, ax = plt.subplots()

    # Hide the axes
    ax.axis('tight')
    ax.axis('off')

    # Create the table data
    table_data = np.column_stack((iterations, newton_errors, secant_errors))

    # Create table and display
    table = ax.table(cellText=table_data, colLabels=['Iteration', 'Newton Errors', 'Secant Errors'], cellLoc='center', loc='center')

    # Adjust table styling
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.5, 1.5)

    # Show the table
    plt.show()
    '''

    newton_errors = np.array(newton_errors)
    secant_errors = np.array(secant_errors)

    alpha = 1.134724

    # Calculate log|x_{k+1} - alpha| vs log|x_k - alpha|
    log_error_newton_xk = np.log10(np.abs(newton_errors[:-1]))
    log_error_newton_xk1 = np.log10(np.abs(newton_errors[1:]))

    log_error_secant_xk = np.log10(np.abs(secant_errors[:-1]))
    log_error_secant_xk1 = np.log10(np.abs(secant_errors[1:]))

    # Calculate the slopes (linear regression) for each method
    slope_newton, intercept_newton, _, _, _ = stats.linregress(log_error_newton_xk, log_error_newton_xk1)
    slope_secant, intercept_secant, _, _, _ = stats.linregress(log_error_secant_xk, log_error_secant_xk1)

    # Plotting the log-log plot for Newton's method
    plt.figure(figsize=(10, 6))
    plt.plot(log_error_newton_xk, log_error_newton_xk1, label=f"Newton's Method (Slope: {slope_newton:.2f})", marker='o')

    # Plotting the log-log plot for Secant method
    plt.plot(log_error_secant_xk, log_error_secant_xk1, label=f"Secant Method (Slope: {slope_secant:.2f})", marker='s')

    # Labels and title
    plt.xlabel(r"$\log_{10} |x_k - \alpha|$")
    plt.ylabel(r"$\log_{10} |x_{k+1} - \alpha|$")
    plt.title("Error Convergence for Newton and Secant Methods")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()


driver()


