import matplotlib.pyplot as plt
import numpy as np
import math

pi=np.pi

R=500;
r=50
d=60;

t=np.linspace(0, 2*pi*math.lcm(r,R)/r, 500)

x=lambda t : (R-r)*np.cos(t) + d*np.cos((R-r)/r*t)
y=lambda t : (R-r)*np.sin(t) - d*np.sin((R-r)/r*t)

plt.plot(x(t), y(t), '-')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('plot.png',dpi=300)
plt.show()



