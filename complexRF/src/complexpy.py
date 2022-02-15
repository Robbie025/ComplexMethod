import argparse
import importlib
import math
import pdb
import random
import sys

import matplotlib.pyplot as plt
import numpy as np


try:
  import src.sampling as sample_vector
except:
  import sampling as sample_vector


def complex_func(func,x): #func,xup,xlow,maxeval,xstart):
    return func(x)
               
def firstChecks(xup,xlow): 
	# Check if xlow and xup are correct as in all values in xlow < xup even for positive and negative limits
    xlowr,xupr = xlow.shape[0],xup.shape[0]
    checkok = True
    if xlowr==0 and xupr==0: 
        print("Only a row vector is allowed. Make sure you have an row vector"); checkok = False #sys.exit(0)
    
    if not np.all(xlow<xup):
        print("Please check the upper bounds and the lower bounds"); checkok = False #sys.exit(0)
    
    return checkok

def checkdesignlimits(xlow,xup,x):
    # Check if the point x is within the design limits. If not it is pushed/pulled back into the design limits.
    # Evaluating the design limit constraints.
    t = np.array(x<xlow)

    for i in range(t.shape[0]):
        if t.item(i):
            x[i]=xlow[i]

    t1 = np.array(x>xup)
    # for the positive values
    for j in range(t1.shape[0]):
        if t1.item(j):
            x[j]=xup[j]      
    return x
    
def complexpy_(obj,xlow,xup,samplingmethod="LHS",optionsample=False):

    # Constants to be used in the complex algorithm
    
    Alfa = 1.3                # Reflection Distance
    IterMax = 30               # Maximum number of iterations for the correcting the reflection point.
    MaxEvals = 500         # Maximum number of complex iterations
    b = 4                   # Constant used when moving the newpoint towards the center and best
    TolFunc = 0.00001        # Tolerance for function convergence
    TolX = 0.0001             # Tolerance for parameter convergence - Not implemented
    Gamma = 0.3             # Forgetting Factor
    Rfak = 0.3               # Randomization factor 
    
    
    # some initial values
    NoEvals=0                 # Count of Number of Function evaluation
    Iterations=1              # Count of Number of Optimization iteration
    conv_cond = 0      
    fminV=[]
    allx=[]
    allf=[]


    # Number of optimization parameters
    Nparams = xlow.shape[0]  
        
    if Nparams == int(1):
	    k=3
    else:
	    k=2*Nparams      

    # kf implements the forgetting principle. Each objective value will be increased with kf each iteration
    kf = 1 - math.pow( (Alfa/2),(Gamma/k) )
 
    # Check if inputs are correct
    firstcheck = firstChecks(xup,xlow)
    if not firstcheck == True:
       print("Checks not passed. Review Code! Process terminated")
       sys.exit(0)
    
    # Create a random array, within the limits, to start the optimization run. See sampling.py
    x = sample_vector.Sample_choice(samplingmethod,xlow,xup,k,optionsample)
    
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
    fminV = fmin.copy()
    
    xworst,xbest = x[fworstind,:], x[fbestind,:] # x values corresponding to the worst and best function values
    xmax,xmin = np.amax(x,0), np.amin(x,0)       # numberically minimum and maximum x values

    initialspreadoff= f.copy()                                  # Variable to store f values for each iteraction and its spread
    initialspreadoff[0:k,0] = abs( abs(fmax) - abs(fmin) )      # Calculation of spread in function values
    allf = np.hstack( (allf, initialspreadoff) )                # allf stores function and spread 

    initialspreadofx= np.zeros([k,1])
    initialspreadofx[0:k,0] =  max( (xmax -xmin) / (xup-xlow) )
    allx = np.hstack( (allx, initialspreadofx) )

    # Start the complex search
    while NoEvals < MaxEvals: 
 
        # Check for convergence of the function and parameter values
        if fmin == 0:
           if abs(abs(fmax)-abs(fmin)) <= TolFunc:
                conv_cond = 1
                break
            
        elif abs( ( abs(fmax)-abs(fmin) ) / abs(fmin) ) <= TolFunc:
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

 
	    # Add some noise to the Reflected Point
        xmax,xmin = np.amax(x,0),np.amin(x,0)
        l1 = max( (xmax-xmin) / (xup-xlow) )

        ri = np.random.rand(Nparams)-0.5

        x_11 = x_1 + (Rfak * (xup-xlow) * l1 * ri)

        # Check if the reflected point is within the design limits. Push/Pull the points to the extremums if it crosses over
        xnew = checkdesignlimits(xlow,xup,x_11)

        # Substiture the point back into the complex
        x[fworstind] = xnew[:] 

        # Updating f with the reflected point        
        f[fworstind,0] = complex_func(obj,xnew[:])  # update function value of the new point
        NoEvals += 1 # update number of evaluations

        fworstind_new,fbestind_new = f.argmax(), f.argmin() # Update worst and best indice in the function space
        xworst,xbest = x[fworstind_new,:], x[fbestind_new,:]
        

        itera=0
        while (fworstind_new == fworstind) and (itera < IterMax) and (NoEvals < MaxEvals):  
            a = 1 - math.exp(-1.0*itera/b)

         
            xmax,xmin = np.amax(x,0),np.amin(x,0)
            l1 = np.array(max( (xmax -xmin) / (xup-xlow) ))
            ri = np.random.rand(Nparams) - 0.5
            
            x_11 = (Rfak * (xup-xlow)) * l1*ri
            xnew_ =  ( ( (xc*(1.0-a) + xbest * a) + xnew) * 0.5 ) + x_11
            
            # Check if the reflected point is within the design limits. Push/Pull the points to the extremums if it crosses over
            xnew = checkdesignlimits(xlow,xup,np.array(xnew_))
            x[fworstind,:] = xnew[:]

             # Updating f with the reflected point
            f[fworstind,:] = complex_func(obj,xnew)
            NoEvals += 1

            # Function index calculation
            fworstind_new,fbestind_new = f.argmax(), f.argmin()
            fmin,fmax = f[fbestind_new,0], f[fworstind_new,0]
            xmax,xmin = x.item(x.argmax()), x.item(x.argmin())
            itera += 1 # end of inner loop

        Iterations += 1                  # Complex Iterations
        allf = np.vstack( (allf,[f[fbestind,0], abs( abs(fmax) - abs(fmin) ) ] ) )
        xappend = np.hstack( (x[fbestind], l1 ) )
        allx = np.vstack( (allx, xappend ) )
        fminV = np.vstack( (fminV, fmin ) )
 
    return x[fbestind,:], fmin, fminV, allf, Iterations, conv_cond, NoEvals
      
if __name__=="__main__":
    from testfunctions import objfunc
    xlow = np.array([ -1.2, -1.2 ])
    xup = np.array([1.2,1.2 ])
    funcname = objfunc.install    
    samplingmethod = "LHS"
    option=False

    np.set_printoptions(precision=3)
    print("{:12}".format("No."), '{:15}'.format("xmin"), "{:8}".format("fmin"), "{:12}".format("Iterations"), "{:7}".format("Evals"), "{:4}".format("conv") ) 
    xmin,fmin,funcVector,allf,Iterations,conv,noofevaluations=  complexpy_(funcname,xlow,xup,samplingmethod,option)
    print("{:4}".format(1), '{:>17}'.format(np.array2string(xmin)), "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) ) 

    line, = plt.plot(funcVector, '--', linewidth=2)
    dashes = [10, 5, 100, 5] 
    line.set_dashes(dashes)
    plt.show()