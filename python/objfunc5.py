import numpy as np
import math

def install(x):
        """ 
        Simple spherical function that can check the validity of an optimization algorithm

http://en.wikipedia.org/wiki/Rosenbrock_function
 http://en.wikipedia.org/wiki/Test_functions_for_optimization

 f(x1,x2) = 100*(x1^2-x2)^2 + (1-x1)^2

 Suggested limits: -9 <= xi <= j  where  i = (1,2, ...)  
 Optimal Values *: x*= [1,1] f*= 0;

 Usage:
 >> python objfunc5.py

 or
 >> import numpy as np
 >> import objfunc5

 >> x=np.array([1,1])
 >> print objfunc5.install(x)
        """
        
        a=np.array(x)
        ObjVal = 0.0;
	x1= a.item(0)
        return (x1*x1)*a.size

if __name__ == "__main__":
    x=np.array([-5,-0,-5])
    print x,"Value= ",install(x)," and should be zero for x is zero for [1,1,1]"
