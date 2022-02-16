Complex Method -- Python
=========

The complex-rf package is logically divided into three:


1. Complexpy.py - This source file contains the implemenation of the complex method in python. Typically, the user need not edit this file, unless there is a need to change certain parameter values such as tolerance limits, reflection distance etc. A theoritical decription of the complex-rf method is provided in chapter **Description**.
2. objfunc*.py - This source file contains the implementation of the objective function that you would like to minimize. Currently, there are multiple test functions provided. The user can simply use the existing file as a template. There is an excellant wiki where mathematical test functions are listed -- search for *optimization test function*.

3. start.py - This python file is used to run the optimiation. You can think of it as the glue between the complexpy.py and objfunc.py. Alternatively, you can start the optimiztion from a python interpreter. For example, to run an optimization run with complexmethod on objfunc, run the following commands in a terminal window:

 ::

   $ python 
   $ import objfunc
   $ import complexpy
   $ import numpy as np
   $ xlow=np.array([-15,-15])
   $ xup=np.array([15,15])
   
   $ samplingmethod="LHS"
   $ xmin,fmin,funcvector,allf,Iterations=complexpy.complexpy_(objfunc.install,xlow,xup,samplingmethod)

       
After you have installed python and numpy, to get stated run start.py at the CompleMethod/python folder.





Arguments  
------

::

  python3 -h

  optional arguments:
  -h, --help            show this help message and exit
  -l XLOW, --xlow XLOW  Lower bound of the test function. This is a List; e.g.:-5.0 -5.0
  -u XUP, --xup XUP     Upper bound of the test function. This is a List; e.g.:5.0 5.0
  -n N                  Number of Runs of the complexRF
  --sample {uniform,LHS}
                        --sample -lhc or --sample -uniform will tell complexpy which start vector to use.
  -o OBJF, --objf OBJF  Define where you have the objective function. Usually in the testfunction folder. e.g.
                        src.testfunctions.objfunc
  -d, --detailed        Switch on this flag to show all the results. Could be interesting.
  -p, --process         Add this flag if you want to run many runs (>1000s) in multithreaded mode.



You can using the above flags to customize your run. Exmaple of using setup.py is shown below. 

::

  python3 setup.py --xup '512 512' --xlow '-512 -511'
  python3 setup.py --xup '512 512' --xlow '-512 -511' --objf 'src.testfunctions.objfunc5' -p

.. note::

	The objfunc5 is the objective function. The function install() from objfunc5 is called from setup.py



Running direclty
------

You can run setup.py directly where the default values can be modified as in the example below.


:: 
    default_xlow = '-5.0 -5.0' 
    default_xup =  '5.0 5.0'  
    default_objfunc = "src.testfunctions.objfunc2" 
    default_n = 100 


to run:
::
  python3 setup.py 


Complexpy.py
------

You can run complexpy.py directly as well. The default values can be modified as in the example below.

to run:
::
  python3 complexpy.py 

