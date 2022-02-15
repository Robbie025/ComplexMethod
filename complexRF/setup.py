import argparse
import concurrent.futures
from doctest import DocTestFailure
import importlib
import sys
import time as t
from locale import strcoll

import numpy as np

import src.complexpy as cp  # Implementation of complexpy

# USAGE:
# python3 setup.py --xup "512 512" --xlow '-512 -511'
# python3 setup.py --xup "512 512" --xlow '-512 -511' --objf 'src.testfunctions.objfunc5' --simple 'False'




def linearprocesscomplexserarch():
    return 0

def multiprocesscomplexserarch():
    return 0

def printresults():
    if n==1:
        print("Only the table header")
    if args.detailed == True:
        print('Current result')
    else:
            print('skik this')
    return 0



if __name__ == "__main__":

    """
    User can edit these default values when runing this file in a python interpretor. 
    TO DO: the if else statment to run either a default_process as well as dagult_simple
    """
    # Default values for lower bound e.g. '-512.0 -512.0'
    default_xlow = '-5.0 -5.0' 

    # Default values for upper bound  e.g. '512.0 512.0'
    default_xup =  '5.0 5.0'  
    
    # Sampling method. Two option right now: Uniform, LHC, DEBUG. Debug not implemented
    default_samplingmethod = 'uniform'
    default_samplingmethod_option = False # True for shuffling the initial sample. Does not really help?

    # relative to path of this file. Objective function definitions. more work to be done. see src/testfunctions. 
    default_objfunc = "src.testfunctions.objfunc5" 
    
    # n - How many runs do you want to run?
    default_n = 100 
    
    
    # ************************************************
    """ The arguments that can used to run setup.py """

    # This is for arguments that are passed in through a Terminal. Is this really useful?
    parser = argparse.ArgumentParser(description='test function')
    parser.add_argument('-l','--xlow', \
        type=str, \
            required=False, \
                default = default_xlow, \
                    help='Lower bound of the test function. This is a List; e.g.: [ -15, -15] ')

    parser.add_argument('-u','--xup', \
        type=str, \
            required=False, \
                default= default_xup, \
                    help='Upper bound of the test function. This is a List; e.g.: [15, 15] ')

    parser.add_argument('-n',\
        required=False,\
            default=default_n, \
                type=int, \
                    help ='Number of Runs of the complexRF')

    parser.add_argument('--sample', \
        choices = ['uniform','LHS','debug'], \
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
    # ************************************************
   
    #Getting the objective function handler from the arguments
    arg_function = args.objf    
    objfuncHandle = importlib.import_module(arg_function, ".")
    funcname = objfuncHandle.install # User might want to change this if they have a different name for function call.
  
    
    # Workaround to get the string xlow and xup into numpy arrays 
    smallx, largex= (args.xlow).split(), (args.xup).split()
    xlow, xup = np.zeros([len(smallx)]), np.zeros([len(largex)])
    for i in range(len(largex)):
        xlow[i], xup[i] = smallx[i], largex[i]
 

    """
    Variables to prepare for printout
    c = number of times complexpy has converged
    xprint = space for printing xmin
    """
    c=0
    np.set_printoptions(precision=4)
    startime = t.perf_counter()

    samplingmethod = args.sample
    print('first',samplingmethod)
    option=False

 
    if (not args.process):
        # Printing out the results
        print("{:12}".format("No."), '{:16}'.format("xmin"), "{:8}".format("fmin"), "{:10}".format("Iterations"), "{:7}".format("Evals"), "{:4}".format("conv") ) 
        
        for i in range(args.n):
            xmin,fmin,funcVector,allf,Iterations,conv,noofevaluations=  cp.complexpy_(funcname,xlow,xup,samplingmethod,option)
            if (args.detailed==False and  ( (i+1) == args.n)):
                    print("{:2}".format(i+1),"/",args.n,'{:>17}'.format(np.array2string(xmin)), "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) ) #,"\t","{:7.3f}".format(time.time()-start_))
            
            if (args.detailed == True):
                print("{:2}".format(i+1),'{:>17}'.format(np.array2string(xmin)), "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) ) #,"\t","{:7.3f}".format(time.time()-start_))
               
            if conv>1:
                c=c+1

    print("Number of times that it has converged c= %s out of %s"%(c,i+1))
    endtime = t.perf_counter()
    print(f'Total time taken is  {round(endtime-startime,2)}') # works only in python> 3.x
    

    if args.process:
        print("ahshit")
        with concurrent.futures.ProcessPoolExecutor() as executor:
            arg=[funcname,xlow,xup,samplingmethod,option]
            e1 = [executor.submit(cp.complexpy_,*arg) for _ in range(args.n)]
          
            i, c = 0, 0 # i is counter for number of runs; c is the number of converged runs
            np.set_printoptions(precision=3)
            print("{:12}".format("No."), '{:15}'.format("xmin"), "{:8}".format("fmin"), "{:12}".format("Iterations"), "{:7}".format("Evals"), "{:4}".format("conv") ) 
            
            for f in concurrent.futures.as_completed(e1):
                resultf = f.result()
                
                xmin,fmin,funcvector, allf, Iterations,conv,noofevaluations = resultf[0],resultf[1],resultf[2],resultf[3],resultf[4] ,resultf[5],resultf[6]
                if conv>1:
                    c=c+1

                if (args.detailed==False and  ( (i+1) == args.n)):
                    print("{:2}".format(i+1),"/",args.n,'{:>17}'.format(np.array2string(xmin)), "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) ) #,"\t","{:7.3f}".format(time.time()-start_))
            
                if (args.detailed == True):
                    print("{:2}".format(i+1),'{:>17}'.format(np.array2string(xmin)), "{:>12}".format(np.array2string(fmin)),"{:8}".format(Iterations), "{:10}".format(noofevaluations), "{:4}".format(conv) ) #,"\t","{:7.3f}".format(time.time()-start_))
                i=i+1
            
        print("Number of times that it has converged c= %s out of %s"%(c,i+1))
        endtime = t.perf_counter()
        print(f'Total time taken is  {round(endtime-startime,2)}') # works only in python> 3.x
               

     
 