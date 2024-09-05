import numpy as np
import matplotlib.pyplot as plt

############################################
# Steps 1-3
############################################
#x = np.linspace(1, 9, 9)
#y = np.arange(1, 10, 1)

# Access first three elements of x
#print("The first three entries of X are") 
#print(x[0:3])

############################################
# Steps 4-
############################################

w = 10**(-np.linspace(1, 10, 10))
print(w)
# The entries of w are 1*10^-(w[n])

x = np.arange(1, len(w) + 1, 1)
s = 3 * w
plt.semilogy(x, w)
plt.semilogy(x, s)
plt.xlabel('x')
plt.ylabel('w')
#plt.show()
#plt.savefig('Section3Plot')
