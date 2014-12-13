import numpy as np
import random

def Sample_Uniform(xlow=np.array([[-5,-5,-5]]),xup=np.array([[5,5,5]]),k=10):
    xlowr,xlowc = xlow.shape[0],xlow.shape[1]   
    xupr,xupc = xup.shape[0],xup.shape[1]
    
    x=np.zeros((k,xlowc))

    # this attempts to fill an array of size (p,q) with random numbers 
    #print "Uniform Sampling"
    for i in range(0,xlowc):   
        vet = [random.uniform(xlow[0,i],xup[0,i]) for _ in range(1,k+1)] 
        x[:,i]=np.array(vet).transpose()
    return np.array(x)
    

def Sample_LHC(xlow=np.array([[-5,-1,1]]),xup=np.array([[5,1,5]]),k=10,shuffle=True):
    # print "Latin Hypercube Sampling"
    xlowr,xlowc = xlow.shape[0],xlow.shape[1]   
    xupr,xupc = xup.shape[0],xup.shape[1]

    segsize=(xup-xlow)/float(k) 
    xlow_=xlow
    xup_=xlow
    x=np.zeros((k,xlowc))
    
    for i in range(k): 
           xup_=xlow+segsize*(i+1);  
           a=random.uniform(xlow_,xup_)
           xlow_=xup_ 
           x[i,:]=a
    if shuffle:
		np.random.shuffle(x)
		return x
    else: 
		return x

def Sample_debug(xlow=np.array([[-5,-1,1]]),xup=np.array([[5,1,5]]),k=10):
    # print "Same Sample returned -- for debug purposes"
    xlowr,xlowc = xlow.shape[0],xlow.shape[1]   
    xupr,xupc = xup.shape[0],xup.shape[1]

    segsize=(xup-xlow)/float(k) 
    xlow_=xlow
    xup_=xlow
    x=np.zeros((k,xlowc))
    
    for i in range(k): 
           xup_=xlow+segsize*(i+1);  
           a=(xlow_+xup_)/2 
           xlow_=xup_ 
           x[i,:]=a
    return x
                      
if __name__=="__main__":
  #x=Sample_Uniform(xlow=np.array([[-5,-1,-5]]),xup=np.array([[5,1,5]]),k=6)
  x=Sample_LHC(xlow=np.array([[-5,-5,-5]]),xup=np.array([[5,5,5]]),k=6,shuffle=True)
  #x=Sample_debug(xlow=np.array([[-5,-5,-5]]),xup=np.array([[5,5,5]]),k=6)
  print x
  #import objfunc2
  #xlow=np.array([[-5,-5,-5]])
  #a=map(objfunc2.install,x)
  #print a
