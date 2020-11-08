import numpy as np
import complexpy  # Implementation of complexpy
import sys 
import matplotlib.pyplot as plt


def apply(func, xlow, xup,samplingmethod,option):  
     return complexpy.complexpy_(func,xlow,xup,samplingmethod,option)  

"""
USER: The function definition.  
for e.g. import objfunc2 as obj Which refers to the filename objfunc2.py
obj.install refers to the implementation which is objfunc2.install 
"""
import objfunc as obj  
funcname=obj.install



"""
USER:  Sampling method: Choose the method to create the first set of random numbers.
Your options are based on sampling.py

samplingmethod = "LHS" or "Debug" or "Uniform"
For "LHS" add the shuffle = True/False
"""
samplingmethod = "LHS"
option=True



"""
USER: Please Enter the bounds of the objective function
This was done for the Objfunc.py
xlow=np.array([-2.048,-2.048])
xup=np.array([2.048,2.048]
"""
xlow=np.array([-15,-15])
xup=np.array([15,15])

np.set_printoptions(precision=3)
print("{:12}".format("No."), '{:15}'.format("xmin"), "{:8}".format("fmin"), "{:12}".format("Iterations"), "{:7}".format("Evals"), "{:4}".format("conv") ) 
xmin,fmin,funcVector,allf,Iterations,conv,noofevaluations=  complexpy.complexpy_(funcname,xlow,xup,samplingmethod,option)
print("{:4}".format(1), '{:>17}'.format(np.array2string(xmin)), "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) ) 

"""
# This is the plotting functions 
funcVectorno=np.array(funcVector)
print("\n",allf.shape[0])
"""


line, = plt.plot(funcVector, '--', linewidth=2)
dashes = [10, 5, 100, 5] 
line.set_dashes(dashes)
plt.show()
