Tutorials
=========

This chapter will detail the software tools needed to run the complex method algorithm. At the moment, there are two implementations of the algorithm: 1. Python and 2, Matlab.
The section **Software** will detail the  software you must have in order to run the code as well as document the code as you see on this site.

You will need to install the following software



	1. *Git*
	2. *Python* with *Numpy*
	
	#. Sphinx* for building the documentation
	#. *Matlab*


Software
********

GIT
----

To download the software software  into your system, you need to have git installed. Please read through to understand basics of git and how to work with github.com
	| http://git-scm.com/book/en/v2
	| https://guides.github.com/introduction/flow/index.html

Once you have git installed, then it is quite easy to download the code onto your local drivei. THis process is called *cloning* and it will create a clone of the ComplexMethod repository.

In a linux-terminal window:
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


More Information
-----------------

Most of information pertaining to the developement process came from this course
	http://sese.nu/scientific-software-development-toolbox/

If you interested in more information, please check out this site. It has tons of information to get you started on software development process.
	http://toolbox.readthedocs.org/en/latest/

Python
******

After you have installed python and numpy, to get stated run start.py after you have cd to the python folder

::
	
	cd ComplexMethod/python
	python start.py

start.py has been  setup to optimize the first four objective functions given in repo. The function description are given in the file objfun.py objfun2.py  objfunc3.py and objfunc4.py

You can also see the help from the python interpreter,

example:

::

	python
	import objfunc4
	help(objfunc4)

Matlab
******

.. note::

	Information comming soon.

