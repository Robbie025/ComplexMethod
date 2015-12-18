Tutorials
=========

This chapter will detail the software tools needed to run the complex method algorithm. Currently, there are two implementations of the algorithm: 1. Python and 2, Matlab.
The section **Software** will detail the  software you must have in order to run the code as well as document the code as you see on this site.


	1. *Git*
	2. *Python* with *Numpy*
	
	#. *Sphinx* for building the documentation
	#. *Matlab* to tun the  ***.m files


Software
********

Git
----

To clone the complexmethod repository, git must be installed in your system. The following links will help you understand the basics of git which is prerequite if you would like to use the code and contribute to this project.

	| http://git-scm.com/book/en/v2
	| https://guides.github.com/introduction/flow/index.html

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

The source files can be found in the *source* folder. To build the documentation, in a terminal window run:i

::
	
	$ make html



More Information
-----------------

If you interested in more information, please check out this site. It has tons of information to get you started on the software development process.
	http://toolbox.readthedocs.org/en/latest/

Python
******

The python version of the complexmehtod is divided into three.

	1. Complexpy.py - This source file contains the implemenation of the complex method in python. Typically, the user need not edit this file, unless there is a need to change certain parameter values such as tolerance limits, reflection distance etc. If you would like to read a theoritical decription of the complex method, please read the next section titled **Description**.
	2. objfunc*.py - This source file contains the implementation of the objective fuction that you would like to minimize. Currently, the file contains one function definition (install) that takes a numpy value and returns the objective function value.  The user should try to add your own objective fuction.
	3. start.py -This python file is used to run the optimiation values. You can think of it as the glue between the complexpy.py and objfunc.py. Of course there is no need to use this file as you can run the optimiztion process from a python interpreter.

After you have installed python and numpy, to get stated run start.py after you have cd to the python folder

::
	
	cd ComplexMethod/python
	python start.py

start.py has been  setup to optimize the first four objective functions given in repo. The function description are given in the file objfun.py objfun2.py  objfunc3.py and objfunc4.py

You can also see the help from the python interpreter,

example:

::

	import objfunc4
	help(objfunc4)

Matlab
******

.. note::

	More information comming soon ....

        This code is part of the *TMKT48 - Design Optimization* given at the Division of Machine Design, Linköping University, Sweden.


