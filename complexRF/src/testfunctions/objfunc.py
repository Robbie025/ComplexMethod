import numpy as np
import math

def install(x):
        """ Rosenbrooks function

 The Rosenbrock function is a non-convex function used as a performance test problem for optimization algorithms introduced by Howard H. Rosenbrock in 1960. It is also known as Rosenbrock banana function or Rosenbrock Valley function.

 http://en.wikipedia.org/wiki/Rosenbrock_function
 http://en.wikipedia.org/wiki/Test_functions_for_optimization

 f(x1,x2) = 100*(x1^2-x2)^2 + (1-x1)^2

 Suggested limits: -5 <= xi <= 5  where  i = (1,2, ...)  
 Optimal Values *: x*= [1,1] f*= 0;

 Usage:
 >> python objfunc.py

 or
 >> import numpy as np
 >> import objfunc

 >> x=np.array([[1,1,1,1]])
 >> print(objfunc.install(x))
        """
        
        a=np.array(x)
        ObjVal = 0.0;
        for i in range(a.shape[0]-1):
            x1= a.item(i)
            x2= a.item(i+1)
            ObjVal = ObjVal + 100*math.pow((x1**2-x2),2) + pow((1-x1),2);
        return ObjVal

if __name__ == "__main__":
    x=np.array([1,2,3])
    print("\n",x)
    print(x,"Value= ",install(x)," and should be zero for x is zero for [1,1,1]")
    number_list = [ x.item(i) for i in range(x.shape[0])]
    number_list2 = [ x.item(i)+x.item(i+1) for i in range(x.shape[0]-1) if i < 2]

    print(number_list)

    print(number_list2)
