import argparse
import concurrent.futures
import importlib
import sys
import time as t

import numpy as np

import src.complexpy as cp  # Implementation of complexpy

# USAGE: from terminal window
# python3 setup.py --xup '512 512' --xlow '-512 -511'
# python3 setup.py --xup '512 512' --xlow '-512 -511' --objf 'src.testfunctions.objfunc5' -p



def printouttoterminal(i,xmin,fmin,Iterations,noofevaluations,conv):
    if i == 1:
        print("{:12}".format("No."), '{:16}'.format("xmin"), "{:8}".format("fmin"), "{:10}".format("Iterations"), "{:7}".format("Evals"), "{:4}".format("conv") )         

    print("{:2}".format(i),'{:>17}'.format(np.array2string(xmin)), \
         "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) )



if __name__ == "__main__":

    """ User can edit these default values when runing this file in a python interpretor. """
    # Default values for lower bound e.g. '-512.0 -512.0'
    default_xlow = '-5.0 -5.0' 

    # Default values for upper bound  e.g. '512.0 512.0'
    default_xup =  '5.0 5.0'  
    
    # Sampling method. Two option right now: Uniform, LHC.
    default_samplingmethod = 'uniform'
    default_samplingmethod_option = False # True for shuffling the initial sample. Does not really help?

    # relative to path of this file. Objective function definitions. more work to be done. see src/testfunctions. 
    default_objfunc = "src.testfunctions.objfunc2" 
    
    # n - How many runs do you want to run?
    default_n = 100 

    
    """ The arguments that can used to run setup.py and passed through a terminal"""
    parser = argparse.ArgumentParser(description='Setup file for complexpy. Run this either from a commanf line wiht arguments \
        or simply python3 setup.py')
    parser.add_argument('-l','--xlow', \
        type=str, \
            required=False, \
                default = default_xlow, \
                    help='Lower bound of the test function. This is a List; e.g.:' +'-5.0 -5.0')

    parser.add_argument('-u','--xup', \
        type=str, \
            required=False, \
                default= default_xup, \
                    help='Upper bound of the test function. This is a List; e.g.:'+'5.0 5.0' )

    parser.add_argument('-n',\
        required=False,\
            default=default_n, \
                type=int, \
                    help ='Number of Runs of the complexRF')

    parser.add_argument('--sample', \
        choices = ['uniform','LHS'], \
            type = str, \
                required=False,\
                    default = default_samplingmethod, \
                        help='--sample -lhc or --sample -uniform will tell complexpy which start vector to use.')

    parser.add_argument('-o',"--objf", \
        type = str, \
            required=False,\
                default=default_objfunc,\
                    help='Define where you have the objective function. Usually in the testfunction folder. e.g. src.testfunctions.objfunc')
        
    parser.add_argument('-d','--detailed', \
        dest='detailed', \
            action='store_true',\
                help='Switch on this flag to show all the results. Could be interesting.',\
                    default=False)

    parser.add_argument('-p','--process', \
        help='Add this flag if you want to run many runs (>1000s) in multithreaded mode. ', \
            action='store_true', \
                dest ='process', \
                    default=False)

    args = parser.parse_args()

    #Getting the objective function handler from the arguments
    arg_function = args.objf    
    objfuncHandle = importlib.import_module(arg_function, ".")
    funcname = objfuncHandle.install # User might want to change this if they have a different name for function call.
      
    # Workaround to get the string xlow and xup into numpy arrays 
    smallx, largex= (args.xlow).split(), (args.xup).split()
    xlow, xup = np.zeros([len(smallx)]), np.zeros([len(largex)])
    for i in range(len(largex)):
        xlow[i], xup[i] = smallx[i], largex[i]
 
    i, c = 0, 0 # i is counter for number of runs; c is the number of converged runs
    startime = t.perf_counter()

    samplingmethod = args.sample
    option=False
    
    """The sequential call to complexrf"""
    if (not args.process):          

        for i in range(1,args.n+1):
            xmin,fmin,funcVector,allf,Iterations,conv,noofevaluations=  cp.complexpy_(funcname,xlow,xup,samplingmethod,option)

            if (args.detailed == True): # Print all values only for -d flag
                printouttoterminal(i,xmin,fmin,Iterations,noofevaluations,conv)
               
            if conv>1:
                c=c+1
                
            if i==1:
                    f_best, x_best, i_best = fmin, xmin, i
            elif fmin <= f_best:
                    f_best, x_best, i_best = fmin, xmin, i          

    """The Concurrent call to complexrf"""
    if args.process:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            arg=[funcname,xlow,xup,samplingmethod,option]
            e1 = [executor.submit(cp.complexpy_,*arg) for _ in range(args.n)]  

        for f in concurrent.futures.as_completed(e1):
            resultf = f.result()
            xmin,fmin,funcvector,allf,Iterations,conv,noofevaluations = resultf[0],resultf[1],resultf[2],resultf[3],resultf[4] ,resultf[5],resultf[6]
            i=i+1
            
            if conv>1:
                c=c+1
            
            if i==1:
                        f_best, x_best, i_best = fmin, xmin, i
            elif fmin <= f_best:
                        f_best, x_best, i_best = fmin, xmin, i 
                
            if (args.detailed == True):
                    printouttoterminal(i,xmin,fmin,Iterations,noofevaluations,conv)
                            

    print("\nResult Summary")
    print("1. Objective function:",arg_function)
    print("2. x* = ",x_best)
    print("3. f* = ",f_best)
    print("4. x* and f* found at run",i_best,"/",i)
    print("5. Convergence rate c= %s / %s"%(c,i))
    
    print("\n *********** Other details")
    if (not args.process):
        print("The complexRF runs wewre run sequentially. Try --process to make it slightly faster")
    else: 
        print("Process was run multithreaded mode. ")
    print(f'Total time taken is  {round(t.perf_counter()-startime,2)}') # works only in python> 3.x