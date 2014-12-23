import numpy as np
import math

def install(x):
        """ Rosenbrooks function

Also known as Rosenbrock banana function or Rosenbrock Valley function 
http://en.wikipedia.org/wiki/Rosenbrock_function
http://en.wikipedia.org/wiki/Test_functions_for_optimization

f(x1,x2) = 100*(x1^2-x2)^2 + (1-x1)^2  
The minimum lies at x*= [1,1] and minimum function value f*= 0;

This implementaion is a general implementaton where for N dimentions, the objective function is succesfully summed over each pair of dimension
        """
        
        a=np.array(x)
        ObjVal = 0.0;
        for i in range(a.shape[0]-1):
			x1= a.item(i)
			x2= a.item(i+1)
			ObjVal = ObjVal + 100*math.pow((x1**2-x2),2) + pow((1-x1),2);
	return ObjVal

if __name__ == "__main__":
    x=np.array([[1,1,1,1]])
    print x,"Value= ",install(x)," and should be zero for x is zero for [1,1,1]"
