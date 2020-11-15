import concurrent.futures
import time
import numpy as np
import complexpy # Implementation of complexpy

def apply(func,xlow,xup,samplingmethod,option):  
    xmin,fmin,funcVector,allf,Iterations,conv,noofevaluations = complexpy.complexpy_(func,xlow,xup,samplingmethod,option) 
    return(xmin,fmin,Iterations,noofevaluations,conv)

 
"""
USER: The function definition.  
for e.g. import objfunc as obj Which refers to the filename objfunc.py
install refers to the implementation in objfunc
"""
from objfunc import install as obj
 


"""
USER:  Sampling method: Choose the method to create the first set of random numbers.
Your options are based on sampling.py

samplingmethod = "LHS" or "Debug" or "Uniform"
For "LHS" add the shuffle = True/False
"""
import sampling as samplingmethod
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

# NE is the number of times complexpy will be run.
NE=2000


if __name__ == "__main__":
#    pass

     start = time.perf_counter()
     
     # start processes to execute the optimizer for obh. max_worker is the total number of workers  ; 
     # concurrent.futures.ProcessPoolExecutor(max_workers=10)
     with concurrent.futures.ProcessPoolExecutor() as executor:
          arg=[obj,xlow,xup,samplingmethod,option]
          e1 = [executor.submit(apply,*arg) for _ in range(NE)]

     
     i, c = 0, 0 # i is counter for number of runs; c is the number of converged runs
     np.set_printoptions(precision=3)
     print("{:12}".format("No."), '{:15}'.format("xmin"), "{:8}".format("fmin"), "{:12}".format("Iterations"), "{:7}".format("Evals"), "{:4}".format("conv") ) 
 
     for f in concurrent.futures.as_completed(e1):
          resultf = f.result()
          i=i+1
          xmin,fmin,Iterations,noofevaluations,conv = resultf[0],resultf[1],resultf[2],resultf[3],resultf[4] 
          print("{:4}".format(i), '{:>17}'.format(np.array2string(xmin)), "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) ) #,"\t","{:7.3f}".format(time.time()-start_))
          if conv>1:
               c=c+1

     finish = time.perf_counter()
     print("Number of times that it has converged c= %s out of %s"%(c,i))
     print(f'Finished in {round(finish-start, 2)} second(s)')