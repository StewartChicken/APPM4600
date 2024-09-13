import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
theta = np.linspace(0, 2 * np.pi, 1000)

# First Figure
R = 1.2
delta_r = 0.1
f = 15
p = 0

x1 = R * (1 + delta_r * np.sin(f * theta + p)) * np.cos(theta)
y1 = R * (1 + delta_r * np.sin(f * theta + p)) * np.sin(theta)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x1, y1, label=r'$x(\theta) = R(1 + \delta r \sin(f \theta + p)) \cos(\theta)$')
plt.title('Parametric Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')  # Equal scaling of x and y axes
plt.grid(True)
#plt.legend() # Toggle legend if desired

# Second Figure
plt.subplot(1, 2, 2)
for i in range(1, 11):
    R_i = i
    delta_r_i = 0.05
    f_i = 2 + i
    p_i = random.uniform(0, 2)
    
    x2 = R_i * (1 + delta_r_i * np.sin(f_i * theta + p_i)) * np.cos(theta)
    y2 = R_i * (1 + delta_r_i * np.sin(f_i * theta + p_i)) * np.sin(theta)
    
    plt.plot(x2, y2, label=f'Curve {i} (R={R_i}, f={f_i:.1f}, p={p_i:.2f})')

plt.title('Multiple Parametric Curves')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')  # Equal scaling of x and y axes
plt.grid(True)
#plt.legend() # Toggle legend if desired

plt.tight_layout()
plt.show()
