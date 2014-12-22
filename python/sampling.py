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
    x=np.zeros((k,xlowc))
    step1 = [np.linspace(xlow.item(i),xup.item(i),k+1) for i in range(xlow.shape[1])]
    step2=np.array(step1).T
    for j in range(k):
        xlow_,xup_ = step2[j,],step2[j+1,]
        mylist = [random.uniform(xlow_.item(i),xup_.item(i)) for i in range(xlow.shape[1])]
        x[j,]=mylist 
    if shuffle:
		np.random.shuffle(x)
		return x
    else: 
		return x


def Sample_debug(xlow=np.array([[-5,-1,1]]),xup=np.array([[5,1,5]]),k=10):
    # print "Same Sample returned -- for debug purposes"
    xlowr,xlowc = xlow.shape[0],xlow.shape[1]   
    xupr,xupc = xup.shape[0],xup.shape[1]
    x=np.zeros((k,xlowc))
    step1 = [np.linspace(xlow.item(i),xup.item(i),k,endpoint=False) for i in range(xlow.shape[1])]
    x = np.array(step1).T
    return x
                      
if __name__=="__main__":
  xlow=np.array([[-5,-5,-5]])
  xup=np.array([[5,5,5]])
  k=10
  shuffle=False
  print "Uniform Sampling"
  x=Sample_Uniform(xlow,xup,k)
  print x
  x=Sample_LHC(xlow,xup,k,shuffle)
  print "Lattice Hypercube Sampling"
  print x 
  x=Sample_debug(xlow,xup,k)
  print "Debug mode --  Should give the same values again and again"
  print x
