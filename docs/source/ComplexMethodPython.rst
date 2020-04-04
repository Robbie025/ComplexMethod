Complex Method -- Python
=========

The python version of the complexmethod is divided into four.


1. Complexpy.py - This source file contains the implemenation of the complex method in python. Typically, the user need not edit this file, unless there is a need to change certain parameter values such as tolerance limits, reflection distance etc. If you would like to read a theoritical decription of the complex method, please read the next section titled **Description**.
2. objfunc*.py - This source file contains the implementation of the objective function that you would like to minimize. Currently, the file contains one function definition (install) that takes a numpy value and returns the objective function value.  The user can try to add their own objective fuction. The user can simply use the existing file as a template. There is an excellant wiki where mathematical test functions are listed -- search for *optimization test function*.

3. start.py - This python file is used to run the optimiation. You can think of it as the glue between the complexpy.py and objfunc.py. Of course there is no need to use this file as you can run the optimiztion process from a python interpreter. For example, to run the optimization with complexmethod on objfunc, run the following commands in a terminal window

 ::

   $ python
   $ import objfunc
   $ import complexpy
   $ import numpy as np
   $ xlow=np.array([[-5,-5]])
   $ xup=np.array([[5,5]])
   $ samplingmethod="LHS"
   $ xmin,fmin,funcvector,allf,Iterations=complexpy.complexpy_(objfunc.install,xlow,xup,samplingmethod)

       
4. sampling.py - The complex method requires a set of starting values which should lie within variable limits. The easiest way is to have the user start the optimization with a user-defined starting points. However, there are other stratergies that can be employed. This python file has the following: a. uniform distribution (Sample_Uniform) b. Latin-hypercube distribution (Sample_LHC) and c. user defined starting point for debuging the code (Sample_Debug). Sampling.py contains more information regarding these methods.

After you have installed python and numpy, to get stated run start.py after you have cd to the python folder.

::
	
	cd ComplexMethod/python
	python start.py

start.py has been  setup to optimize the first four objective functions given in repo. The function description are given in the file objfun.py, objfun2.py, objfunc3.py and objfunc4.py.
You can also see the help from the python interpreter. 

example:

::

	python
	import objfunc4
	help(objfunc4)

 