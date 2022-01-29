import numpy as np
import src.complexpy as cp # Implementation of complexpy
import sys 
import time as t

startime = t.perf_counter()

def apply(func, xlow, xup,samplingmethod,option):  
     return complexpy.complexpy_(func,xlow,xup,samplingmethod,option)  

"""
USER: The function definition.  
for e.g. import objfunc2 as obj Which refers to the filename objfunc2.py
obj.install refers to the implementation which is objfunc2.install 
"""
import src.testfunctions.objfunc5 as obj  
funcname=obj.install


"""
USER:  Sampling method: Choose the method to create the first set of random numbers.
Your options are based on sampling.py

samplingmethod = "LHS" or "Debug" or "Uniform"
For "LHS" add the shuffle = True/False
"""
samplingmethod = "Uniform"
option=False


# User: NE = number of complexpy calls.
# For large number (NE>1000) try start_multip.py
NE=200


"""
USER: Please Enter the bounds of the objective function
This was done for the Objfunc.py
xlow=np.array([-2.048,-2.048])
xup=np.array([2.048,2.048]
"""
xlow=np.array([-15,-15])
xup=np.array([15,15])

"""
Variables to prepare for printout
c = number of times complexpy has converged
xprint = space for printing xmin
"""
c=0
np.set_printoptions(precision=4)



# Printing out the results
print("{:12}".format("No."), '{:16}'.format("xmin"), "{:8}".format("fmin"), "{:10}".format("Iterations"), "{:7}".format("Evals"), "{:4}".format("conv") ) 

for i in range(NE):
    xmin,fmin,funcVector,allf,Iterations,conv,noofevaluations=  cp.complexpy_(funcname,xlow,xup,samplingmethod,option)
    print("{:4}".format(i+1), '{:>17}'.format(np.array2string(xmin)), "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) ) #,"\t","{:7.3f}".format(time.time()-start_))
    if conv>1:
         c=c+1


print("Number of times that it has converged c= %s out of %s"%(c,i+1))

endtime = t.perf_counter()
print(f'Total time taken is  {round(endtime-startime,2)}') # works only in python> 3.x
