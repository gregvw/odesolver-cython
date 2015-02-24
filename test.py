import forward_euler as fe
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    N = 100
    t = np.linspace(0,3,N)
    y = np.zeros(N)
    y0 = 1.0

    f = lambda y,t : -t*y/2

    fe.solve(f,y,t,y0)
 
    plt.plot(t,y)
    plt.show()
    

    
