import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

plt.rcParams['text.usetex'] = True

# I-V curve
x = np.array([0.50,1.00,1.50,2.00,2.50,3.00])
y = np.array([0.60,1.00,1.30,1.55,1.75,1.90])
x_smooth = np.linspace(x.min(), x.max(), 300) # Smooth out with 300 points
spl = make_interp_spline(x, y, k=3) # Cubic fit
y_smooth = spl(x_smooth)

# Kirchoff I-V
xa = np.linspace(2,3,100)
ya = 8-2.5*xa

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_smooth, 'k-')
plt.scatter(x, y, c='b')
plt.plot(xa, ya, 'k--')

# Customise axes
plt.title('Voltage and current at the lightbulb', fontsize=16)
plt.xticks(fontsize=14)
plt.xlabel('$U\,\mathrm{[V]}$', fontsize=16)
plt.yticks(fontsize=14)
plt.ylabel('$I\,\mathrm{[A]}$', fontsize=16)
plt.show()
