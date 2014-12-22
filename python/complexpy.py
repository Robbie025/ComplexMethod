import math,sys,random
import numpy as np
import sampling as sample_vector
import pdb

def complex_func(func,x): #func,xup,xlow,maxeval,xstart):
    return func(x)
               
def firstChecks(xlowr,xupr,xlowc,xupc): 
	#TOFO : Check if xlow and xup are correct as in all values in xlow < xup even for positive and negative limits
    if xlowr==0 and xupr==0: 
        print "Only a row vector is allowed. Make sure you have an row vector"; sys.exit(0)
    
    if not (xlowc==xupc):
        print "Sorry! The dimensions have to be the same"; sys.exit(0)    
    
    checkok = True
    return checkok
    
def complexpy_(obj,xlow,xup,samplingmethod="LHS"):
    """ The complexrf method implemented in python -- 
    
    References

    1. Box, M.J., "A new method of constrained optimization and a comparison with other method," 
    Computer Journal, Vol. 8, No. 1, pp. 42-52, 1965.
    
    2. Andersson J, "Multiobjective Optimization in Engineering Design - Application to fluid Power Systems." 
    Doctoral thesis, Division of Fluid and Mechanical Engineering Systems, Department of Mechanical Engineering, 
    Linkping University, 2001 	

    3. Krus P., Andersson J., Optimizing Optimization for Design Optimization, 
    in Proceedings of ASME Design Automation Conference, Chicago, USA, September 2-6, 2003
    
    """
    #Block one
    # Constants to be used in the complex algorithm
    
    # Reflection Distance
    Alfa = 1.3
    
    # Maximum number of iterations for the correcting the reflection point.
    IterMax=30                  
    
    # Maximum number of complex iterations
    MaxEvals=10000                
    
    # Constant used when moving the newpoint towards the center and best
    b=4.0                      
    
    # Tolerance for function convergence
    TolFunc = 0.0000001  
    
    # Tolerance for parameter convergence - Not implemented
    TolX = 0.0001               
    
    Gamma = 0.3
    
    #Radomization factor 
    Rfak = 0.3;
    
    # Count of Number of Function evaluation
    NoEvals=0                    
    
    # Count of Number of Optimization iteration
    Iterations=0                  
    
    # Count of Iterations when the reflected point exceeds the limits
    itera=1           
               
    fmin=float("inf")
    
    # to be described
    conv_cond=0      
    fminV=[];
    allx=[];
    allf=[];
    W=0.0;
    
    #find the row and column of xlow, xup  
    xlowr,xlowc = xlow.shape[0],xlow.shape[1] #print xlowr,xlowc 
    xupr,xupc = xup.shape[0],xup.shape[1]
    
    Nparams = xlowc;            # Number of optimization parameters
    xmin=np.zeros([xlowc]) 
    
    if Nparams == int(1):
		k=3;   
    else:
		k=2*Nparams;      
        
    kf = 1 - math.pow((Alfa/2),(Gamma/k))

	# Some Checks needs to be moved to a function as first_checks   
    if xlowr==0 and xupr==0: 
        print "Only a row vector is allowed. Make sure you have an row vector"; sys.exit(0)
    
    if not (xlowc==xupc):
        print "Sorry! The dimensions have to be the same"; sys.exit(0)    

    #firstcheck=firstChecks(xlowr,xupr,xlowc,xupc)
    #if firstcheck==True:
       #print "Passed the first Check"
       #sys.exit()
        
    # Create a random vector, within the limits, to start the optimization Process (x
    # this can be changed into a seperate function depending on the type of input
    # pdb.set_trace()
    if samplingmethod == "LHS":
      x = sample_vector.Sample_LHC(xlow,xup,k)
    elif samplingmethod == "Debug":
      x = sample_vector.Sample_Debug(xlow,xup,k)
    else:
       x=sample_vector.Sample_Uniform(xlow,xup,k)
    
    allx=x.copy()
    
    # This is the starting value of complex method -- I will have to change this to a function. Modularize!
    NoEvals=k
    f=np.zeros([k,1])
    for i in range(0,x.shape[0]):
		 f[i,0]=complex_func(obj,np.array(x[i,:]))
   
     
    allf=f
    #Block 2    
    fworstind,fbestind =f.argmax(),f.argmin()
    
    xworst,xbest=x[fworstind,:],x[fbestind,:]
    xmin=xbest   
        
    fmin,fmax = f[fbestind,0],f[fworstind,0]
    fminV=fmin
    
    if abs(abs(fmax)-abs(fmin)) <= TolFunc:        #Is this correct? especially if fmin==0
            conv_cond = 1 ;             print "Done- No need to Optimize fmin=0",abs(abs(fmax)-abs(fmin))                         
    if abs(abs(fmax)-abs(fmin))/abs(fmin) <= TolFunc:    
        conv_cond = 1;         print "Done -- No need to Optimize ",abs(abs(fmax)-abs(fmin))
    #else: print "Complex Method Started"; print
      
    while NoEvals < MaxEvals and conv_cond == 0:
        #print "NoEvals",NoEvals,"and fmin is ",fmin,"with x is ",xmin
        #Increase all f-values with a factor kf. This is the forgetting principle.
        f = f + (fmax-fmin)*kf;

        # Centroid calculation
        xc_=x.sum(0)
        xc=(xc_-xworst)/(k-1)   
        
        # Reflected point        
        x_1  = xc + (xc-xworst)*Alfa   
        
	    # Add some noise to the Reflected Point
        xmax=x_1.item(x_1.argmax()) 
        xmin=x_1.item(x_1.argmin()) 
        l1=(xmax-xmin)/(xup-xlow)
        ri = [random.uniform(-0.5,0.5) for _ in range(1,Nparams+1)]
        x_1=Rfak*(l1.item(l1.argmax())*(xup-xlow))*ri + x_1

        # Checking the point, whether it is in the limits or not
        # Is it possible to write a seperate function for this. Is it needed?
        x_2 = x_1.copy()
        truth = x_1<xlow; #print truth,"\n"
        truthla= np.array([truth])
        a1=np.array(truthla[0,0]);
        for i in range(len(a1)):
            if  a1[i]:
                x_2[0,i] = xlow[0,i]
        
        xnew=x_2.copy()
        truth = x_2 > xup;  
        truthla= np.array([truth])
        a1=np.array(truthla[0,0]);
        for i in range(len(a1)):
            #print a1[i]
            if  a1[i]:    
                xnew[0,i] = xup[0,i] 
        
        x[fworstind]=xnew[0,:] # Update the x

        # Updating f with the reflected point
        f[fworstind,0]=complex_func(obj,xnew[0,:])
        NoEvals=NoEvals+1

        # New function index calculation
        fworstind_new =f.argmax()
        fbestind_new  =f.argmin() 
        
        #Block 3 
        itera=1
        #pdb.set_trace()
        while (fworstind_new == fworstind) and (itera < IterMax) and (NoEvals < MaxEvals):  
            #print "Inside while loop 2"
            #print fworstind_new == fworstind
            a = 1 - math.exp(-1.0*itera/b)
            xnew_ = ((xc*(1.0-a) + x[fworstind_new,:]*a) + xnew)/2.0
            
            x_2N = xnew_.copy()  # Check if it is within the design limits, if not move back:
            truth = x_2N<xlow;  
            truthla= np.array([truth])
            a1=np.array(truthla[0,0]);
            for i in range(len(a1)):
                if  a1[i]:    
                    x_2N[0,i] = xlow[0,i]
                
            xnew2=x_2N.copy()
            truth = x_2N > xup;  
            truthla= np.array([truth])
            a1=np.array(truthla[0,0]);
            for i in range(len(a1)):
                if  a1[i]:    
                    xnew2[0,i] = xup[0,i]
            
            #print xnew2,"\n"    xnew2 is pretty much the result of checking if it is within the design limits

            x[fworstind_new]=xnew2[0,:]
            xnew=xnew2;     

            # Updating f with the reflected point
            f[fworstind_new,0]=complex_func(obj,xnew2[0,:])
            allf=np.vstack((allf,f[fworstind_new,0]))
            NoEvals=NoEvals+1
            
            # Function index calculation
            fworstind_new =f.argmax()
            fbestind_new  =f.argmin() 
            
            itera=itera+1            
            #print fworstind_new == fworstind
            if fmin > f[fworstind_new,0]: # Not needed in this while loop
                #print "fmin",fmin
                fmin = f[fworstind_new,0]
                xmin= x[fworstind_new,:]

            #raw_input("Press Enter to continue...")
        
        fworstind,fbestind=f.argmax(),f.argmin()
                   
        fmin,fmax= f[f.argmin(),0],f[f.argmax(),0]
        
        xworst,xbest= x[fworstind,:],x[fbestind,:] 
        xmin=xbest.copy() 
        
        fminV= np.vstack((fminV,fmin))
        #Iterations = Iterations + 1; # Not implemented either
        #NoEvals=NoEvals+1
        allf=np.vstack((allf,fmin))
        
        #if fmin == 0:
        if abs(abs(fmax)-abs(fmin)) <= TolFunc:
                conv_cond = 1 ;             print "Done 1"                         
        elif abs(abs(fmax)-abs(fmin))/abs(fmin) <= TolFunc:
            conv_cond = 1 ;             print "Done 2"  
        
    fmin=complex_func(obj,np.array(xmin))    # this does not make any sense here either
    print NoEvals
    return xmin,fmin,fminV,allf
    
def apply(func, xlow, xup ,samplingmethod="LHC"): # 1
     return complexpy_(func,xlow,xup,samplingmethod="LHC") # 2
         
if __name__=="__main__":
  import objfunc
  funcname=objfunc.install
  xlow=np.array([[-5,-5]])
  xup=np.array([[5,5]])
  
  for i in range(1):
    xmin,fmin,funcVector,allf= apply(funcname,xlow,xup,samplingmethod="LHC")
    #print i+1
    #print "i,xmin,fmin, allf.shape[0],Hit count = , count"
    print i,xmin,fmin,funcVector.shape[1]
    #if abs(fmin)<1e-4:
        #print i,xmin,fmin, allf.shape[0],"Hit count = ", count
     #   count=count+1
