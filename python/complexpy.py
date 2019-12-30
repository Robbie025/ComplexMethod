import math,sys,random
import numpy as np
import sampling as sample_vector
import pdb
def complex_func(func,x): #func,xup,xlow,maxeval,xstart):
    return func(x)
               
def firstChecks(xup,xlow): 
	# Check if xlow and xup are correct as in all values in xlow < xup even for positive and negative limits
    xlowr,xupr = xlow.shape[0],xup.shape[0]
    checkok = True
    if xlowr==0 and xupr==0: 
        print "Only a row vector is allowed. Make sure you have an row vector"; checkok = False #sys.exit(0)
    
    if not np.all(xlow<xup):
            print "Please check the upper bounds and the lower bounds"; checkok = False #sys.exit(0)
    
    return checkok

def checkdesignlimits(xlow,xup,x):
    # Check if the point x is within the design limits. If not it is pushed/pulled back into the design limits.
    # Evaluating the design limit constraints.
    t = np.array(x<xlow)
    #print "t", t
    #print "x", x 
    for i in range(t.shape[0]):
        if t.item(i):
            x[i]=xlow[i]

    t1 = np.array(x>xup)
    # for the positive values
    for j in range(t1.shape[0]):
        if t1.item(j):
            x[j]=xup[j]; #print "x",x        
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
  
    4. Krus P., Olvander J., Performance Index and Meta Optimization of a Direct Search Optimization Method, Engineering Optimization, Volume 45, Issue 10, pp 1167-1185, 2013.   
    """


    # Constants to be used in the complex algorithm
    
    Alfa = 1.3                # Reflection Distance
    IterMax = 30               # Maximum number of iterations for the correcting the reflection point.
    MaxEvals = 500         # Maximum number of complex iterations
    IterationsMax = 700      # Maximum number of Iterations of the Complex method
    b = 4                   # Constant used when moving the newpoint towards the center and best
    TolFunc = 0.000001        # Tolerance for function convergence
    TolX = 0.00001             # Tolerance for parameter convergence - Not implemented
    Gamma = 0.3             # Forgetting Factor
    Rfak = 0.3;               # Randomization factor 
    
    
    # some initial values
    NoEvals=0                 # Count of Number of Function evaluation
    Iterations=1              # Count of Number of Optimization iteration
    #fmin=float("inf")
    conv_cond = 0      
    fminV=[]
    allx=[]
    allf=[]

        
    # Only for debug modes.
    if samplingmethod == "Debug":
        MaxEvals = 20  
        debugnow = True    # True to run in debug mode
        checkpdb = 1        # which iteration to print out debug values
    else:
        debugnow = False    # True to run in debug mode
        checkpdb = 1        # which iteration to print out debug values

    # Number of optimization parameters
    Nparams = xlow.shape[0]            
    
    if Nparams == int(1):
		k=3;   
    else:
		k=2*Nparams;      

    # kf implements the forgetting principle. Each objective value will be increased with kf each iteration
    kf = 1 - math.pow( (Alfa/2),(Gamma/k) )
 
    # Check if inputs are correct
    firstcheck = firstChecks(xup,xlow)
    if not firstcheck == True:
       print "Checks not passed. Review Code! Process terminated"
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
    f=np.zeros([k,1])
    for i in range(0,k):
        f[i,0]=complex_func(obj,np.array(x[i,:]))
        NoEvals += 1
  
    allf = f.copy() # Maintain all function values.... 23/12 2019 does not make sense
    allx = x.copy() # Maintain all design variable values.... 23/12 2019 does not make sense
    
    # Calculate some values to start the complex optimization
    fworstind,fbestind = f.argmax(), f.argmin()   # Indicies for the worst and best function values
    fmin,fmax = f[fbestind,0], f[fworstind,0]     # min and max function values
        
    xworst,xbest = x[fworstind,:], x[fbestind,:] # x values corresponding to the worst and best function values
    xmax,xmin = np.amax(x,0), np.amin(x,0)       # numberically minimum and maximum x values

    initialspreadoff= f.copy()                      # placeholder variable to store f values for each iteraction and its spread
    initialspreadoff[0:k,0] = abs( abs(fmax) - abs(fmin) ) # Calculation of spread in function values
    allf = np.hstack( (allf, initialspreadoff) )     # allf stores function and spread 

    initialspreadofx= np.zeros([k,1])
    initialspreadofx[0:k,0] =  max( (xmax -xmin) / (xup-xlow) )
    allx = np.hstack( (allx, initialspreadofx) )

    # Start the complex search
    while NoEvals < MaxEvals: 
 
        # This if statment is only if you want to run in the debug mode. 
        # This prints relevant values to debug the complex run for a specific run. checkpdb=2 (see above).
        if (Iterations == checkpdb)  and debugnow:
            print "\nI am in the outer loop now ", NoEvals, Iterations
            print "\n x", x 
            print "\n f",f
            print "the f values will increase now"

        # Check for convergence of the function and parameter values
        if fmin == 0:
           if abs(abs(fmax)-abs(fmin)) <= TolFunc:
                conv_cond = 1
                break
        if abs( ( abs(fmax)-abs(fmin) ) / abs(fmin) ) <= TolFunc:
                conv_cond = 1
                break
        
        if abs(max( (xmax -xmin) / (xup-xlow) )) <= TolX:
                conv_cond = 2
                break

        #Increase all f-values with a factor kf. This is the forgetting principle.
        f = f + ( f[f.argmax(),0] - f[f.argmin(),0] ) * kf

        fworstind,fbestind = f.argmax(), f.argmin()
        xworst,xbest = x[fworstind,:], x[fbestind,:]
        fmin,fmax = f[fbestind,0],f[fworstind,0]

        # Centroid calculation
        xc_ = x.sum(0)
        xc = (xc_-xworst) / (k-1)   
        
        # Reflected point         
        x_1  = xc + ((xc-xworst) * Alfa)

        if Iterations == checkpdb and debugnow:
            print "\nSome inner checks"
            print "xworst", xworst
            print "Reflected point x_1", x_1 
            print "xc", xc
            print "\n"
 
	    # Add some noise to the Reflected Point
        xmax,xmin = np.amax(x,0),np.amin(x,0)
        l1 = max( (xmax-xmin) / (xup-xlow) )

        ri = np.random.rand(Nparams)-0.5

        if Iterations == checkpdb or debugnow:
            ri = [-0.3, 0.5] # debug values 

        x_11 = x_1 + (Rfak * (xup-xlow) * l1 * ri)

        # Check if the reflected point is within the design limits. Push/Pull the points to the extremums if it crosses over
        xnew = checkdesignlimits(xlow,xup,x_11)

        # Substiture the point back into the complex
        x[fworstind] = xnew[:] 

        if Iterations == checkpdb and debugnow:
            print "\nOuter loop inner checks"
            print "max( (xmax-xmin) / (xup-xlow) ) or hahaha1", max( (xmax-xmin) / (xup-xlow) )
            print "xup-xlow",(xup-xlow)
            print "Rfak * (xup-xlow)",Rfak * (xup-xlow)
            print "Rfak * (xup-xlow) * l1",Rfak * (xup-xlow) * l1
            print "Rfak * (xup-xlow) * l1 *  ri", Rfak * (xup-xlow) * l1 * ri
            print "x_11 + above", x_1 + Rfak * (xup-xlow) * l1 * ri
            print "xnew", xnew
            print " "

        # Updating f with the reflected point        
        f[fworstind,0] = complex_func(obj,xnew[:])  # update function value of the new point
        NoEvals += 1 # update number of evaluations

        fworstind_new,fbestind_new = f.argmax(), f.argmin() # Update worst and best indice in the function space
        xworst,xbest = x[fworstind_new,:], x[fbestind_new,:]
        
        # Redo the reflection, if the reflected point remains the worst point 
        if Iterations == checkpdb and debugnow:
            print "I am just before the inner loop now \n", NoEvals, Iterations
            print "fworstind_new", fworstind_new, "\n"
            print "\n x",x
            print "\n f",f
            print "fmax",f[fworstind_new,0],"\n", fworstind_new

        itera=0
        while (fworstind_new == fworstind) and (itera < IterMax) and (NoEvals < MaxEvals):  
            a = 1 - math.exp(-1.0*itera/b)


            if Iterations == checkpdb and debugnow:
                print "\n\nI am in the inner loop now:", NoEvals
                print "xnew",xnew
                print "Evals and iter" , NoEvals, itera
                print "fworstind & fworstind_new", fworstind, fworstind_new
                print "a", a

           
            xmax,xmin = np.amax(x,0),np.amin(x,0)
            l1 = max( (xmax -xmin) / (xup-xlow) )
            ri = np.random.rand(Nparams) - 0.5
            
            if Iterations == checkpdb or debugnow:
                ri = [-0.3, 0.5] # debug values 

            x_11 = (Rfak * (xup-xlow)) * l1 * ri
            xnew_ =  ( ( (xc*(1.0-a) + xbest * a) + xnew) * 0.5 ) + x_11
            
            # Check if the reflected point is within the design limits. Push/Pull the points to the extremums if it crosses over
            xnew = checkdesignlimits(xlow,xup,np.array(xnew_))
            x[fworstind,:] = xnew[:]

            if Iterations == checkpdb and debugnow:
                print "\nInner working of the inner loop"
                print "\nmax( (xmax -xmin)/(xup-xlow) )", max( (xmax -xmin)/(xup-xlow) )
                print "\n(Rfak * (xup-xlow)) ", (Rfak * (xup-xlow)) 
                print "\n(Rfak * (xup-xlow)) * l1 * ri", (Rfak * (xup-xlow)) * l1 * ri
                print "\nxc", xc
                print "\nxbest", xbest
                print "\n( (xc*(1.0-a) + xbest * a) + xnew) * 0.5 ", ( (xc*(1.0-a) + xbest * a) + xnew) * 0.5  
                print "\nxnew ", xnew
                print "\nxnew_", xnew_,"\n"

            # Updating f with the reflected point
            f[fworstind,:] = complex_func(obj,xnew)
            NoEvals += 1

            # Function index calculation
            fworstind_new,fbestind_new = f.argmax(), f.argmin()
            fmin,fmax = f[fbestind_new,0], f[fworstind_new,0]
            xmax,xmin = x.item(x.argmax()), x.item(x.argmin())

            if Iterations == checkpdb and debugnow:
                 print "\n x",x
                 print "\n f",f
                 print "fmax index and fmax",f[fworstind_new,0], fmax, "\n"
            
            itera += 1 # end of inner loop

        Iterations += 1                  # Complex Iterations
        allf = np.vstack( (allf,[f[fbestind,0], abs( abs(fmax) - abs(fmin) ) ] ) )
        xappend = np.hstack( (x[fbestind], l1 ) )
        allx = np.vstack( (allx, xappend ) )
 
    return x[fbestind,:], fmin, fminV, allf, Iterations, conv_cond, NoEvals
    
def apply(func, xlow, xup ,samplingmethod="LHS"): 
     return complexpy_(func,xlow,xup,samplingmethod) 
         
if __name__=="__main__":
  import objfunc4 as obj
  samplingmethod = "LHS"
  funcname=obj.install
  xlow=np.array([-512,-512])
  xup=np.array([512,512])

  xmin,fmin,funcVector,allf,Iterations,condition, NoEvaluations= apply(funcname,xlow,xup,samplingmethod)
  print xmin,fmin,Iterations