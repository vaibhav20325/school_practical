import matplotlib.pyplot as plt
import math
import numpy as np

x=np.arange(0,10,0.1)
y1=np.exp(-(x/10))*np.sin(math.pi*x)
y2=x*np.exp(-(x/3))
plt.plot(x,y1,label='f(x)')
plt.plot(x,y2,label='g(x)')
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig('graph.jpg')
plt.show()


