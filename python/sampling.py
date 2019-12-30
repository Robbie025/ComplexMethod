import numpy as np
import random

def Sample_Uniform(xlow=np.array([-5,-5,-5]),xup=np.array([5,5,5]),k=10):
    """ Uniform Sampling between two numpy arrays
  
    xlow and xup and two numpy arrays with xlow.shape == xup.shapem. The default values are xlow.shape = (1,3).

    This is also referred to as random sampling.
    
    This function will return an numpy array x with x.shape = (k,3), which have bounds between xlow and xup
    """
    xlowr = xlow.shape[0]   
    xupr = xup.shape[0]
    if xlowr==xupr and xlowr==xlow.size:
       x=np.zeros((k,xlowr))
       for i in range(0,xlowr):   
           vet = [random.uniform(xlow[i],xup[i]) for _ in range(1,k+1)] 
           x[:,i]=np.array(vet).transpose()
    return np.array(x)
    

def Sample_LHC(xlow=np.array([-5,-1,1]),xup=np.array([5,1,5]),k=10,shuffle = False):
    """ Latin Hyper-Cube Sampling between two numpy arrays
  
    xlow and xup and two numpy arrays with xlow.shape == xup.shapem. The default values are xlow.shape = (1,3).

    http://en.wikipedia.org/wiki/Latin_hypercube_sampling
    
    This function will return an numpy array x with x.shape = (k,3), which have bounds between xlow and xup. Unlike random samling, Latin Hyper-cube sampling divides the sample space (equally) into k parts and populates a random number within these regions.

    shuffle is an boolean  argument and will shuffle the generated list column wise for True Value.
    """
    xlowr = xlow.shape[0]   
    xupr = xup.shape[0]
    
    if xlowr==xupr and xlowr==xlow.size:
        x=np.zeros((k,xlowr))
        step1 = [np.linspace(xlow.item(i),xup.item(i),k+1) for i in range(xlow.shape[0])]
        step2=np.array(step1).T
        for j in range(k):
            xlow_,xup_ = step2[j,],step2[j+1,]
            mylist = [random.uniform(xlow_.item(i),xup_.item(i)) for i in range(xlow.shape[0])]
            x[j,]=mylist 
    if shuffle:
		np.random.shuffle(x)
		return x
    else: 
		return x


def Sample_Debug(xlow=np.array([-5,-1,1]),xup=np.array([5,1,5]),k=10):
    """ A non-random sampling for use during complex method development.  
  
    xlow and xup and two numpy arrays with xlow.shape == xup.shapem. The default values are xlow.shape = (1,3).
    
    This function will return an numpy array x with x.shape = (k,3), which have bounds between xlow and xup. 
    """
    xlowr = xlow.shape[0]   
    xupr = xup.shape[0]
    if xlowr==xupr and xlowr==xlow.size:
        x=np.zeros((k,xlowr))
        step1 = [np.linspace(xlow.item(i),xup.item(i),k,endpoint=True) for i in range(xlow.shape[0])]
        x = np.array(step1).T
        return x
                      
if __name__=="__main__":
  xlow=np.array([-12,-12])
  xup=np.array([12,12])
  print("xlow,xup = ",xlow,xup)
  k=5
  shuffle=False
  print "Uniform Sampling"
  x=Sample_Uniform(xlow,xup,k)
  print x
  x=Sample_LHC(xlow,xup,k,shuffle)
  print "Lattice Hypercube Sampling"
  print x 
  x=Sample_Debug(xlow,xup,k)
  print "Debug mode --  Should give the same values again and again"
  print x
