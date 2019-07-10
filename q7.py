
import matplotlib.pyplot as plt
import math
import numpy as np

x=np.arange(0,10,0.1)
y1=math.e-((x/10)*np.sin(math.pi*x))
y2=math.e*x-(x/3)
plt.plot(x,y1,label='f(x)')
plt.plot(x,y2,label='g(x)')
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig('graph.jpg')
plt.show()
