import numpy as np,complexpy  
import sys,time


def apply(func, xlow, xup,samplingmethod): # 1
     return complexpy.complexpy_(func,xlow,xup,samplingmethod) # 2

"""
USER: Please enter the objfunc module and define the function in the next two lines
"""
import objfunc4 as obj  


funcname=obj.install

"""
USER:  Sampling method: Choose the method to create the first set of random numbers.
Your options are based on sampling.py

samplingmethod = "LHS"
samplingmethod = "Debug"
amplingmethod = "Uniform"
For "LHS" add the shuffle = True/False
"""
samplingmethod = "Uniform"
shuffle=False


"""
USER: Please Enter the bounds of the objective function
"""
"""
# This was done for the Objfunc.py
xlow=np.array([[-5,-5]])
xup=np.array([[5,5]])
"""
"""
# This was done for the Objfunc2.py
xlow=np.array([[-5.12,-5.12]])
xup=np.array([[5.12,5.12]])
"""
"""
# This was done for the Objfunc3.py
xlow=np.array([[-5.12,-5.12,-5.12]])
xup=np.array([[5.12,5.12,5.12]])
"""

# This was done for the Objfunc4.py
xlow=np.array([[-512,-512]])
xup=np.array([[512,512]])



start_=time.time()


np.set_printoptions(precision=3)
print "i \t \t xmin \t\t\tfmin \t No.Of Evaluations \t Iterations\t time"
for i in range(10):
    xmin,fmin,funcVector,allf,Iterations= apply(funcname,xlow,xup,samplingmethod)
    print i,"\t",xmin,"\t\t","{:10.6f}".format(fmin),"\t\t",allf.shape[0],"\t\t",Iterations,"\t","{:7.3f}".format(time.time()-start_)
    start_=time.time()

    
"""
# This is the plotting functions 
import matplotlib.pyplot as plt
line, = plt.plot(allf, '--', linewidth=2)
dashes = [10, 5, 100, 5] 
line.set_dashes(dashes)
plt.show()
"""
