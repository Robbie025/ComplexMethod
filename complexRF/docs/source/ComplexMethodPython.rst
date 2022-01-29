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

::
	
	cd ComplexMethod/python
	python start.py

start.py has been setup to run the complex optimizer NE number of times on an objective function defined in objfunc*.py.