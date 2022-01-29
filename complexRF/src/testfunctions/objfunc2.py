import numpy as np
def install(a):

 """Step function and is also known as DE JONG's Function 3
 
 This function can be described as Non convex wih flat surfaces.
 
 http://en.wikipedia.org/wiki/Test_functions_for_optimization
 
 f(x) = sum(floor(x))
 Input parameters:  x - A numpy array of real values
 Output			 :  One real value 

 eg: 
 x =[1.2,1.2]        => f = 2
 x =[1.2,2.2,-1.2]   => f = 1
 x =[1.2,-2.2]       => f = -2


 Usage:
 >> python objfunc2.py

 or
 >> import numpy as np
 >> import objfunc2

 >> x=np.array([[1.2,2.2,-1.]])
 >> print(objfunc2.install(x))
 """
 objval=np.sum(np.sum(np.floor(a)))
 return objval
 
if __name__ == "__main__":
 
 x=np.array([1.2,1.2,-1.2])
 print("x = ",x, " and the function value is ", install(x))
 print(" Should be two for [[1.2,1.2]] and three for  [[1.2,1.2,1.3]] and one  for [[1.2,2.2,-1.2]] ")