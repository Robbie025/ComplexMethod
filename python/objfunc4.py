import numpy as np
import math

# Egg Holder function  f(512, 404.2319)=-959.6407
def install(a):
        x1=a[0,0]
        x2=a[0,1]
        a1 = -1 * (x2+47) * math.sin( math.pow(abs(x2+x1/2+47),0.5));
        a2 = -1 * x1 * math.sin(math.pow(abs(x1-(x2+47)),0.5));
        objval= a1 + a2        
        return objval
 
if __name__ == "__main__":
 x =np.array([[512,404.2319]])
 print install(x)," should be zero for xlow is -959.6407 " 
