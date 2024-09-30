import numpy as np
import sympy as sp

# Define original newton routine
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
  p = []
  p.append(p0)
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p.append(p1)
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it+1]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]


# Define modified newton 
def newton_modified(p0, tol=1e-7, Nmax=100):
  # Begin modified newton approx
  x = sp.symbols('x')

  # Redifine f, fp
  f = sp.exp(3*x) - 27*(x**6) + 27*((x**4)*sp.exp(x)) - 9*((x**2)*sp.exp(2*x))
  fp = sp.diff(f, x)

  g = f / fp 
  gp = sp.diff(g, x)

  p = []
  p.append(p0)
  for it in range(Nmax):
    # Substitute p0 into g and gp
    g_val = g.subs(x, p0)
    gp_val = gp.subs(x, p0)

    p1 = p0 - g_val / gp_val
    p.append(p1)

    if(abs(p1 - p0) < tol):
      pstar = p1
      return [pstar, it+1]

    p0 = p1

  pstar = p1

  return [pstar, it+1]


# Define newton for root with multiplicity > 1
def newton_multiplicity(p0, tol=1e-7, Nmax=100):

  x = sp.symbols('x')

  m = 3 # Multiplicity of root in question

  # Define f, fp
  f = sp.exp(3*x) - 27*(x**6) + 27*((x**4)*sp.exp(x)) - 9*((x**2)*sp.exp(2*x))
  fp = sp.diff(f, x)

  for it in range(Nmax):
    f_val = f.subs(x, p0)
    fp_val = fp.subs(x, p0)

    p1 = p0 - m*(f_val / fp_val)

    if(abs(p1 - p0) < tol):
      pstar = p1
      return [pstar, it+1]

    p0 = p1

  pstar = p1

  return [pstar, it+1]


def driver():

  # Initial guess
  x_0 = 4.0

  # Approximation tolerance
  tol = 1e-7
  # Max iterations
  Nmax = 100

  # Define the function
  f = lambda x: np.exp(3*x) - 27*(x**6) + 27*((x**4)*np.exp(x)) - 9*((x**2)*np.exp(2*x))
  fp = lambda x: 3 * np.exp(3 * x) - 162 * x**5 + 108 * x**3 * np.exp(x) + 27 * x**4 * np.exp(x) - 18 * x * np.exp(2 * x) - 9 * x**2 * 2 * np.exp(2 * x)

  [p1, pstar1, info1, it1] = newton(f, fp, x_0, tol, Nmax)

  print("Newton's method root: ", pstar1)
  #print("Newton's method iterations: ", p1, "\n")
  print("Newton's method iteration count: ", it1, "\n")

  # END NEWTON METHOD

  [pstar2, it2] = newton_modified(x_0)

  print("Modified Newton's method root: ", pstar2)
  #print("Modified Newton's method iterations: ", p2, "\n")
  print("Modified Newton's method iteration count: ", it2)

  # END MODIFIED NEWTON METHOD

  [pstar3, it3] = newton_multiplicity(x_0)

  print("\nMultiplicity Newton's method root: ", pstar3)
  #print("Modified Newton's method iterations: ", p2, "\n")
  print("Multiplicity Newton's method iteration count: ", it3)

driver()