import numpy as np
def install(a):
        objval=np.sum(np.sum(np.floor(a)))
        return objval
 
if __name__ == "__main__":
 """Implements the  Step function and is also known as DE JONG's Function 3
  
 
 Syntax:  ObjVal = dejong3(x)
 Input parameters:  x - A numpy array of real values
 eg:  x = np.array([[1.2,2.2,-1.3]])

 Output parameters:
    objval    - One real value according to DeJong's function 3.
 
 Usage: python objfunc2.py               
 """
 
 x=np.array([[1.2,2.2,-1.3]])
 print "x = ",x, " and the function value is ", install(x)
 print " Should be two for [[1.2,1.2]] and three for  [[1.2,1.2,1.3]] and one  for [[1.2,2.2,-1.2]] " 

