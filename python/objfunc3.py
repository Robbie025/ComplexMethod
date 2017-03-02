import numpy as np
import math

def install(a):
    """ Styblinski-Tang function

 http://en.wikipedia.org/wiki/Test_functions_for_optimization
 
 f(x1,x2,...xi) = sum((xi^4 - 16*xi^2 + 5*xi) / 2 )
 Input parameters:  x - A numpy array of real values
 Output			 :  One real value 

 Suggested limits: -5 <= xi <= 5  where  i = (1,2, ...n)  
 Optimal Values *: x*= [-2.90354,-2.90354,-2.90354, ..n] f*=-39.16599*n;

 Usage:
 >> python objfunc3.py

 or
 >> import numpy as np
 >> import objfunc3

 >> x=np.array([[-2.90354,-2.90354]])
 >> print objfunc3.install(x)

    """
    n=np.size(a)
    objval=0.0
    for i in range(0,n):
        x=a.item(i);  
        objval = objval + 0.5*math.pow(x,4) -8* math.pow(x,2)+ 2.5* x;
    return objval

if __name__ == "__main__":
 x=np.array([-2.90354,-2.90354,-2.90354,-2.90354,-2.90354,-2.90354])
 print install(x)," should be same as ",-39.16599*np.size(x)


