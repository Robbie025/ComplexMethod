import numpy as np,complexpy  
import objfunc,sys # Change these Values -- objfunc2 = dejong 3; objfunc = dejong 2 and objfunc3 = tyblinski--Tang Functions
#import time
#import os


def apply(func, xlow, xup): # 1
     return complexpy.complexpy_(func,xlow,xup) # 2

#start_time = time.time()
# Change the Values in the next 3 lines


# why is this function still here!
def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2 ** 20)
    return mem

    
funcname=objfunc.install

xlow=np.array([[-5,-5,-5]])
xup=np.array([[5,5,5]])

n=xlow.shape[1]

count=1
# -39.166*n
for i in range(20):
    xmin,fmin,funcVector,allf= apply(funcname,xlow,xup)
    #print i+1
    if abs(fmin)<1e-4:
        print i,xmin,fmin, allf.shape[0],"Hit count = ", count
        count=count+1

#print("--- %s seconds ---" % time.time() - start_time)
    
"""
import matplotlib.pyplot as plt
line, = plt.plot(allf, '--', linewidth=2)
dashes = [10, 5, 100, 5] 
line.set_dashes(dashes)
plt.show()
"""
