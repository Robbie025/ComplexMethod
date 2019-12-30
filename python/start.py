import numpy as np,complexpy  
import sys,time


def apply(func, xlow, xup,samplingmethod): # 1
     return complexpy.complexpy_(func,xlow,xup,samplingmethod) # 2


"""
USER:  Sampling method: Choose the method to create the first set of random numbers.
Your options are based on sampling.py

samplingmethod = "LHS"
samplingmethod = "Debug"
amplingmethod = "Uniform"
For "LHS" add the shuffle = True/False
"""
samplingmethod = "LHS"
shuffle=False

NE=10


# OBJFUNC  --------- OBJFUNC
"""
USER: Please Enter the bounds of the objective function
USER: Please enter the objfunc module and define the function in the next two lines
"""
import objfunc2 as obj  
funcname=obj.install
# This was done for the Objfunc.py
#xlow=np.array([-2.048,-2.048])
#xup=np.array([2.048,2.048])
xlow=np.array([-5.12,-5.12])
xup=np.array([5.12,5.12])
c=0
start_=time.time()
np.set_printoptions(precision=3)
#print "\ni \t \t xmin \t\t\tfmin \t No.Of Evaluations \t Iterations"
for i in range(NE):
    xmin,fmin,funcVector,allf,Iterations,conv,noofevaluations= apply(funcname,xlow,xup,samplingmethod)
    print "{:4}".format(i+1),'{:>17}'.format(np.array2string(xmin)),"{:8.4f}".format(fmin),"{:4}".format(Iterations), "{:4}".format(noofevaluations) #,"\t","{:7.3f}".format(time.time()-start_)
    #print i+1," [","{:7.4f} ".format(xmin.item(0)),"{:7.4f}".format(xmin.item(1)),"] ","{:8.4f}".format(fmin),"\t",allf.shape[0],"\t",Iterations #,"\t","{:7.3f}".format(time.time()-start_)

    if conv>1:
        c=c+1
    start_=time.time()

#print"Number of times that it has converged c= %s out of %s"%(c,i+1)




# OBJFUNC2  --------- OBJFUNC2
"""
USER: Please enter the objfunc module and define the function in the next two lines
import objfunc2 as obj  
funcname=obj.install
# This was done for the Objfunc2.py
xlow=np.array([[-5.12,-5.12]])
xup=np.array([[5.12,5.12]])
start_=time.time()
np.set_printoptions(precision=3)
print "\ni \t \t xmin \t\t\tfmin \t No.Of Evaluations \t Iterations\t time"
for i in range(NE):
    xmin,fmin,funcVector,allf,Iterations= apply(funcname,xlow,xup,samplingmethod)
    print i,"\t",xmin,"\t\t","{:10.6f}".format(fmin),"\t\t",allf.shape[0],"\t\t",Iterations,"\t","{:7.3f}".format(time.time()-start_)
    start_=time.time()

"""

# OBJFUNC3  --------- OBJFUNC3
"""
USER: Please enter the objfunc module and define the function in the next two lines
import objfunc3 as obj  
funcname=obj.install
# This was done for the Objfunc3.py
xlow=np.array([[-5.12,-5.12]])
xup=np.array([[5.12,5.12]])

start_=time.time()
np.set_printoptions(precision=3)
print "\ni \t \t xmin \t\t\tfmin \t No.Of Evaluations \t Iterations\t time"
for i in range(NE):
    xmin,fmin,funcVector,allf,Iterations= apply(funcname,xlow,xup,samplingmethod)
    print i,"\t",xmin,"\t\t","{:10.6f}".format(fmin),"\t\t",allf.shape[0],"\t\t",Iterations,"\t","{:7.3f}".format(time.time()-start_)
    start_=time.time()


"""
# OBJFUNC4  --------- OBJFUNC4
"""
USER: Please enter the objfunc module and define the function in the next two lines
import objfunc4 as obj  
funcname=obj.install
# This was done for the Objfunc4.py
xlow=np.array([[-512,-512]])
xup=np.array([[512,512]])

start_=time.time()
np.set_printoptions(precision=3)
print "\ni \t \t xmin \t\t\tfmin \t No.Of Evaluations \t Iterations\t time"
for i in range(NE):
    xmin,fmin,funcVector,allf,Iterations= apply(funcname,xlow,xup,samplingmethod)
    print i,"\t",xmin,"\t\t","{:10.6f}".format(fmin),"\t\t",allf.shape[0],"\t\t",Iterations,"\t","{:7.3f}".format(time.time()-start_)
    start_=time.time()

    
"""
# This is the plotting functions 
"""
import matplotlib.pyplot as plt
line, = plt.plot(allf, '--', linewidth=2)
dashes = [10, 5, 100, 5] 
line.set_dashes(dashes)
plt.show()
"""