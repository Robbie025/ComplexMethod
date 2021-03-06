import numpy as np
import math

def install(x):
        """ 
        Simple spherical function that can check the validity of an optimization algorithm

http://en.wikipedia.org/wiki/Rosenbrock_function
 http://en.wikipedia.org/wiki/Test_functions_for_optimization

 f(x1,x2) = 100*(x1^2-x2)^2 + (1-x1)^2

 Suggested limits: -9 <= xi <= 9  where  i = (1,2, ...)  
 Optimal Values *: x*= [1,1] f*= 0;

 Usage:
 >> python objfunc5.py

 or
 >> import numpy as np
 >> import objfunc5

 >> x=np.array([1,1])
 >> print( objfunc5.install(x))
        """
        
        a=np.array(x)
        ObjVal = 0.0;
        for i in range(a.size):
            x1= a.item(i)
            ObjVal = ObjVal + (x1*x1)
        return ObjVal 

if __name__ == "__main__":
    x=np.array([-9,9,-9])
    print(x,"Value= ",install(x)," and should be 75 for x for [-5,5,-5]")
