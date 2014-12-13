import numpy as np
import math

# Rosenbrooks banana function implemented in python. 
# The x*= [1,1,1] and f*=0
def install(a):
        ObjVal = 0.0;
        for i in range(1,a.shape[0]):
			x1= a.item(i-1)
			x2= a.item(i)
                        #print x1,x2
			ObjVal = ObjVal + 100*math.pow((x1**2-x2),2) + pow((1-x1),2);
	return ObjVal

if __name__ == "__main__":
 x=np.array([[1,1,1,1]])
 print install(x)," and it  should be zero for x is zero for [1,1,1]"
 #print x.shape[0]," ", x.shape[1]
