import numpy as np
# Step function also known as the dejong function _
def install(a):
        #n=np.size(a)
        #objval=0;
        # a much better and elegant solution would be to use sum(sum(np.floor(a)))
        objval=sum(sum(np.floor(a)))
        #for i in range(0,n):
        #    objval = objval + np.floor(a.item(i));
        
        return objval
 
if __name__ == "__main__":
 x=np.array([[1.2,2.2,-1.3]])
 print install(x)," should be two for [[1.2,1.2]] and three for  [[1.2,1.2,1.3]] and one  for [[1.2,2.2,-1.2]] " 

