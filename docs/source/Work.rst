Introduction
=========

The Complex Method is an optimization algorithm and is based on the Simplex method. The complex method has been applied to a wide range of problems such as physics
, structural engineering, fluid power system design and aerospace engineering. The aim of the project is to make the complex method source code available to the general public. At the moment, the code is available in two implementations: python and matlab. 

Software Prerequisites
=========

This chapter will detail the software tools needed to run the complex method algorithm. Currently, there are two implementations of the algorithm: 1. Python and 2, Matlab.
The section **Software** will detail the  software you must have in order to run the code as well as document the code as you see on this site.


	1. *Git*
	2. *Python* with *Numpy*
	
	#. *Sphinx* for building the documentation
	#. *Matlab* to run the  ***.m files


Software
********

Git
----

To clone the complexmethod repository, git must be installed in your system. The following links will help you understand the basics of git, which is prerequisite if you would like to use the code and contribute to this project.

	| http://git-scm.com/book/en/v2
	| https://guides.github.com/introduction/flow/index.html

To install git from a terminal run:

::

	$ sudo apt-get install git 

Once you have git installed, then it is quite easy to download the code onto your local drive. This process is called *cloning* and it will create a clone of the ComplexMethod repository.

In a terminal window:
 ::
 
	 $ mkdir complexmethod
	 $ cd complexmethod
	 $ git clone https://github.com/Robbie025/ComplexMethod.git


Python
------

A version of complex method written in python  is available in the git repository in the folder *python*.

Links to install python and numpy:

:: 

	https://www.python.org/downloads/
	http://www.numpy.org/

Sphinx
------

Sphinx is used for documentation of the project. To install sphinx, in a terminal window run:

::

	$ sudo apt-get install python-sphinx

The source files can be found in the *source* folder. To build the documentation, in a terminal window run:

::
	
	$ make html

Remember that latex must be installed for building the math equations. For ubuntu pcs: 

::

	$ sudo apt-get install texlive-full

More Information
-----------------

If you interested in more information, please check out this site. It has tons of information to get you started on the software development process.
	http://toolbox.readthedocs.org/en/latest/

Python
******

The python version of the complexmethod is divided into four.


1. Complexpy.py - This source file contains the implemenation of the complex method in python. Typically, the user need not edit this file, unless there is a need to change certain parameter values such as tolerance limits, reflection distance etc. If you would like to read a theoritical decription of the complex method, please read the next section titled **Description**.
2. objfunc*.py - This source file contains the implementation of the objective function that you would like to minimize. Currently, the file contains one function definition (install) that takes a numpy value and returns the objective function value.  The user can try to add your own objective fuction. The user can simply use the existing file as a template. There is an excellant wiki where mathematical test functions are listed -- search for *optimization test function*.

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

Matlab
******

.. note::

	More information comming soon ....

        This code is part of the *TMKT48 - Design Optimization* given at the Division of Machine Design, Linköping University, Sweden.


