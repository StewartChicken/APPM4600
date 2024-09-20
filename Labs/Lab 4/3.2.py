
# Derived from formula solving for p
def aitken_helper(p_n, p_n1, p_n2):
    return (p_n1**2 - p_n*p_n2) / (2*p_n1 - p_n - p_n2)

# approximations is an array of approximations produced by fixed point iteration
def aitken(approximations):
    new_approximations = []

    for i in range(len(approximations)- 2):
        new_approximations.append(aitken_helper(approximations[i], approximations[i+1], approximations[i+2]))