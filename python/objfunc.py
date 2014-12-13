import numpy as np
import math

# Rosenbrooks banana function implemented in python. 
# The x*= [1,1,1] and f*=0
def install(x):
        a=np.array(x)
        #print a.shape[0],a.shape[1]
        ObjVal = 0.0;
        for i in range(a.shape[0]-1):
			x1= a.item(i)
			x2= a.item(i+1)
                        #print x1,x2
			ObjVal = ObjVal + 100*math.pow((x1**2-x2),2) + pow((1-x1),2);
	return ObjVal

if __name__ == "__main__":
 x=np.array([[1,2,3,4,5,6]])
 print install(x)," and it  should be zero for x is zero for [1,1,1]"
 print x.shape[0]," ", x.shape[1]
