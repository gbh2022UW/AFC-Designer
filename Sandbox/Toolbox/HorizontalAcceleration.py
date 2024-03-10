import numpy as np
from scipy import optimize

def CalculateHA(weight, length, theta):
    ht = weight / 4 #hover thrust in pounds: just enough thrust to make keep drone stable

    '''
    x = [fd, fr]
    fd: force of propeller that is dropped down
    fr: force of propeller that is raised up
    '''
    
    def staticEq(x):
        return [2 * x[0] * np.cos(theta) + 2 * x[1] * np.cos(theta) - weight, 
                length / 2 * x[1] - length / 2 * x[0]]
        
    
    pf = optimize.root(staticEq, [1.25 * ht, 1.25 * ht], method = "hybr")
    print(pf.x)
    print(ht)

CalculateHA(10, 1, np.pi / 6)