import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial (x + 2)^9
condensed_polynomial = np.poly1d([1, -2])
expanded_polynomial = np.poly1d([1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512])  # Start with x^0

# Define the domain from 1.920 to 2.080 with a step of 0.001
domain = np.arange(1.920, 2.080, 0.001)

# Evaluate the polynomial over the domain
condensed_values = (condensed_polynomial(domain)**9)
expanded_values = expanded_polynomial(domain)

# Plotting the polynomial evaluation
plt.figure(figsize=(10, 6))
plt.plot(domain, condensed_values, label='condensed', color='blue')
plt.plot(domain, expanded_values, label='expanded', color='red')
plt.title(r'Evaluation of expanded p(x)')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.grid(True)
plt.legend()
plt.show()


