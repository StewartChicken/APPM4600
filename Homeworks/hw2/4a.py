import numpy as np

# Step 1: Create the vector t
pi = np.pi
increment = pi / 30
t = np.arange(0, pi + increment - .1, increment)


# Step 2: Create the vector y
y = np.cos(t)

# Define N - it can range from 0 to the length of the vectors
N = 1  # Can adjust this

if(N > len(t)):
	N = len(t)

print(N)

# Step 3: Compute the sum from k = 1 to N of t(k) * y(k)
sum_value = np.sum(t[:N] * y[:N])

print("the sum is: ", sum_value)

