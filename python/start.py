import numpy as np
import complexpy  # Implementation of complexpy
import sys,time
import time as t

startime = t.perf_counter()

def apply(func, xlow, xup,samplingmethod,option):  
     return complexpy.complexpy_(func,xlow,xup,samplingmethod,option)  

"""
USER: The function definition.  
for e.g. import objfunc2 as obj Which refers to the filename objfunc2.py
obj.install refers to the implementation which is objfunc2.install 
"""
import objfunc5 as obj  
funcname=obj.install


"""
USER:  Sampling method: Choose the method to create the first set of random numbers.
Your options are based on sampling.py

samplingmethod = "LHS" or "Debug" or "Uniform"
For "LHS" add the shuffle = True/False
"""
samplingmethod = "LHS"
option=True


# NE is the number of times complexpy will be run.
NE=10


"""
USER: Please Enter the bounds of the objective function
This was done for the Objfunc.py
xlow=np.array([-2.048,-2.048])
xup=np.array([2.048,2.048]
"""
xlow=np.array([-1500,-1500])
xup=np.array([1500,1500])

# Variables for outputs
c=0
#start_=time.time()
np.set_printoptions(precision=3)
print("{:12}".format("No."), '{:15}'.format("xmin"), "{:8}".format("fmin"), "{:12}".format("Iterations"), "{:7}".format("Evals"), "{:4}".format("conv") ) 
 
for i in range(NE):
    xmin,fmin,funcVector,allf,Iterations,conv,noofevaluations=  complexpy.complexpy_(funcname,xlow,xup,samplingmethod,option)
    print("{:4}".format(i+1), '{:>17}'.format(np.array2string(xmin)), "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) ) #,"\t","{:7.3f}".format(time.time()-start_))
    if conv>1:
         c=c+1
    #start_=time.time()

print("Number of times that it has converged c= %s out of %s"%(c,i+1))

endtime = t.perf_counter()
print(f'Total time taken is  {round(endtime-startime,2)}')
