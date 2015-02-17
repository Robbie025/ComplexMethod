import math,sys,random
import numpy as np
import sampling as sample_vector
import pdb
def complex_func(func,x): #func,xup,xlow,maxeval,xstart):
    return func(x)
               
def firstChecks(xup,xlow,xlowr,xupr,xlowc,xupc): 
	# Check if xlow and xup are correct as in all values in xlow < xup even for positive and negative limits

    checkok = True
    if xlowr==0 and xupr==0: 
        print "Only a row vector is allowed. Make sure you have an row vector"; checkok = False #sys.exit(0)
    
    if not (xlowc==xupc):
        print "Sorry! The dimensions have to be the same"; checkok = False #sys.exit(0)    

    isgreater = xlow<xup

    for i in range(isgreater.shape[1]) :
      if not isgreater.item(i):
            print "Please check the upper bounds and the lower bounds"; checkok = False #sys.exit(0)
    
    return checkok

def checkdesignlimits(xlow,xup,x):
    # Check if the point x is within the design limits. If not it is pushed/pulled back into the design limits.
    # Evaluating the design limit constraints.
    t = np.array(x<xlow)
    for i in range(t.shape[1]):
        if t.item(i):
            x[0,i]=xlow[0,i]

    t1 = np.array(x>xup)
    # for the positive values
    for j in range(t1.shape[1]):
        if t1.item(j):
            x[0,j]=xup[0,j]; #print "x",x        
    return x
    
def complexpy_(obj,xlow,xup,samplingmethod="LHS"):
    """ The complexrf method 
    
    References

    1. Box, M.J., "A new method of constrained optimization and a comparison with other method," 
    Computer Journal, Vol. 8, No. 1, pp. 42-52, 1965.
    
    2. Andersson J, "Multiobjective Optimization in Engineering Design - Application to fluid Power Systems." 
    Doctoral thesis, Division of Fluid and Mechanical Engineering Systems, Department of Mechanical Engineering, 
    Linkping University, 2001 	

    3. Krus P., Andersson J., Optimizing Optimization for Design Optimization, 
    in Proceedings of ASME Design Automation Conference, Chicago, USA, September 2-6, 200i3
  
    4. Krus P., lvander J., Performance Index and Meta Optimization of a Direct Search Optimization Method, Engineering Optimization, Volume 45, Issue 10, pp 1167-1185, 2013.   
    """
    # Constants to be used in the complex algorithm
    
    Alfa = 1.3                # Reflection Distance
    IterMax = 30               # Maximum number of iterations for the correcting the reflection point.
    MaxEvals = 500          # Maximum number of complex iterations
    IterationsMax = 5000      # Maximum number of Iterations of the Complex method
    b = 4.0                   # Constant used when moving the newpoint towards the center and best
    TolFunc = 0.00001        # Tolerance for function convergence
    TolX = 0.0001             # Tolerance for parameter convergence - Not implemented
    Gamma = 0.3
    Rfak = 0.3;               # Radomization factor 
    NoEvals=0                 # Count of Number of Function evaluation
    Iterations=0              # Count of Number of Optimization iteration
    fmin=float("inf")
    
    conv_cond = 0      
    fminV=[];
    allx=[];
    allf=[];
    
    #Get the number of rows and columns of xlow, xup  
    xlowr,xlowc = xlow.shape[0],xlow.shape[1] 
    xupr,xupc = xup.shape[0],xup.shape[1]
    
    Nparams = xlowc;            # Number of optimization parameters
    xmin = np.zeros([xlowc]) 
    
    if Nparams == int(1):
		k=3;   
    else:
		k=2*Nparams;      
        
    kf = 1 - math.pow((Alfa/2),(Gamma/k))

    # Check if inputs are correct
    firstcheck = firstChecks(xup,xlow,xlowr,xupr,xlowc,xupc)
    if not firstcheck == True:
       print "Oops! Process terminated"
       sys.exit(0)
    
    # Create a random array, within the limits, to start the optimization Process (x)
    # Currently, there are three strategy to initialize the complex. Please see sampling.py
    if samplingmethod == "LHS":
      x = sample_vector.Sample_LHC(xlow,xup,k,shuffle=False)
    elif samplingmethod == "Debug":
      x = sample_vector.Sample_Debug(xlow,xup,k)
    else:
       x=sample_vector.Sample_Uniform(xlow,xup,k)
    

    
    # This is the starting function value of complex space 
    NoEvals = k
    f=np.zeros([k,1])
    for i in range(0,x.shape[0]):
		 f[i,0]=complex_func(obj,np.array(x[i,:]))
   
    allf = f.copy() # Maintain all function values
    allx = x.copy() # Maintain all design variable values
    
    fworstind,fbestind = f.argmax(),f.argmin()
    xworst,xbest = x[fworstind,:],x[fbestind,:]
    xmin = xbest   
        
    fmin,fmax = f[fbestind,0],f[fworstind,0]
    fminV=fmin
    
    if fmin == 0:
       if abs(abs(fmax)-abs(fmin)) < TolFunc:        
            conv_cond = 1 ; 
            print "Done -- No need to Optimize: abs(abs(fmax)-abs(fmin)) <=TolFunc" 
            print "xmin = ",xmin, "fmin = ",fmin," fmax =",fmax, " TolFunc = ",  abs(abs(fmax)-abs(fmin))                            
    elif abs(abs(fmax)-abs(fmin))/abs(fmin) <= TolFunc:    
        conv_cond = 1;         print "Done -- No need to Optimize, abs(abs(fmax)-abs(fmin)) <= TolFunc"
     	 
    while NoEvals < MaxEvals and conv_cond == 0 and Iterations < IterationsMax:
        #Increase all f-values with a factor kf. This is the forgetting principle.
        f = f + (fmax-fmin)*kf;
	
        # Complex Iterations
        Iterations += 1
        
        # Centroid calculation
        xc_=x.sum(0)
        xc=(xc_-xworst)/(k-1)   
        
        # Reflected point         
        x_1  = xc + (xc-xworst)*Alfa   
        
	# Add some noise to the Reflected Point
        xmax,xmin = x_1.item(x_1.argmax()),x_1.item(x_1.argmin()) 
        l1=(xmax-xmin)/(xup-xlow)
        ri = [random.uniform(-0.5,0.5) for _ in range(1,Nparams+1)]
        x_1=Rfak*(l1.item(l1.argmax())*(xup-xlow))*ri + x_1
        
        # Check if the reflected point is within the design limits. Push/Pull the points to the extremums if it crosses over
        xnew = checkdesignlimits(xlow,xup,x_1)
        
        # Substiture the point back into the complex
        x[fworstind]=xnew[0,:] 

        # Updating f with the reflected point
        f[fworstind,0] = complex_func(obj,xnew[0,:])
        NoEvals += 1

        # New function index calculation
        fworstind_new = f.argmax()
        fbestind_new  = f.argmin() 
        
        # Redo the reflection, if the reflected point remains the worst point 
        itera=1
        while (fworstind_new == fworstind) and (itera < IterMax) and (NoEvals < MaxEvals):  
            a = 1 - math.exp(-1.0*itera/b)
            xnew_ = ((xc*(1.0-a) + x[fworstind_new,:]*a) + xnew)/2.0
            
            xnew2 = checkdesignlimits(xlow,xup,np.array(xnew_))
            x[fworstind_new]=xnew2[0,:]
            
            xnew = xnew2;     

            # Updating f with the reflected point
            f[fworstind_new,0] = complex_func(obj,xnew2[0,:])
            allf = np.vstack((allf,f[fworstind_new,0]))
            NoEvals += 1
            
            # Function index calculation
            fworstind_new,fbestind_new =f.argmax(),f.argmin()
            
            itera += 1
                         
            if fmin > f[fworstind_new,0]: # Not needed in this while loop
                fmin = f[fworstind_new,0]
                xmin= x[fworstind_new,:]
        
        # Check if the following one line makes any diffeece to the code
        fworstind,fbestind=f.argmax(),f.argmin()

        fmin,fmax= f[fbestind,0],f[fworstind,0]
        xworst,xbest= x[fworstind,:],x[fbestind,:] 
        xmin=xbest.copy() 
        
        fminV= np.vstack((fminV,fmin))
        allf=np.vstack((allf,fmin))
        
        xbig = np.amax(x);
        xsmall = np.amin(x);
        if fmin == 0:
           if abs(abs(fmax)-abs(fmin)) <= TolFunc:
                conv_cond = 1 ;          #   print "Done 1"                         
        elif abs(abs(fmax)-abs(fmin))/abs(fmin) <= TolFunc:
            conv_cond = 1 ;           #  print "Done 2"  
        if TolX >= abs(np.amax(((xbig-xsmall)/(xup-xlow)))):
               conv_cond = 2 
    fmin=complex_func(obj,np.array(xmin))    # this does not make any sense here either
    return xmin,fmin,fminV,allf,Iterations
    
def apply(func, xlow, xup ,samplingmethod="LHS"): 
     return complexpy_(func,xlow,xup,samplingmethod) 
         
if __name__=="__main__":
  import objfunc4 as obj
  samplingmethod = "LHS"
  funcname=obj.install
  xlow=np.array([[-512,-512]])
  xup=np.array([[512,512]])
  
  for i in range(1):
    xmin,fmin,funcVector,allf,Iterations= apply(funcname,xlow,xup,samplingmethod)
    print xmin,fmin,Iterations
