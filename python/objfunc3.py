import numpy as np
import math

"""
This is an impementation of the Styblinski-Tang function in python
"""

#import objfunc3
#xlow=np.array([[-5.1,-5.12,-5.12]])
#aa=objfunc3.install(xlow)
def install(a):
    n=np.size(a)
    objval=0.0
    for i in range(0,n):
        x=a.item(i);  
        objval = objval + 0.5*math.pow(x,4) -8* math.pow(x,2)+ 2.5* x;
    return objval

if __name__ == "__main__":
 x=np.array([[-2.90354,-2.90354,-2.90354,-2.90354,-2.90354,-2.90354]])
 print install(x)," should be same as ",-39.16599*np.size(xlow)


