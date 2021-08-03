import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

z = np.arange(0, 2 * 300, 10)
print (z)
fig, ax = plt.subplots()

line, = ax.plot(z, np.random.rand(60))
print(np.random.rand(1024))

ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

plt.show()