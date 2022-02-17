ComplexRF Package
============

The complexpy.py implements the complexrf optimization algorithm. A theoretical description of the method is provided in chapter **Description**. The software prerequisite are descibed in chapter **Software Prerequisites**.

The complexrf package is logically divided into three:

Source Files 
----

The source files can be found under ComplexMeethod/complexrf/ and ComplexMeethod/complexrf/src/.

Complexpy.py - This file contains the implemenation of the complexrf method. Typically, the user need not edit this file, unless to play around with speciifc parameter values such as tolerance limits, reflection distance etc.  

Sampling.py - This file contains couple of sampling methods that are used in Complexpy.py. Generally, a user need not edit this file.

setup.py - This python file is used to run the optimiation. You can think of it as the glue between the complexpy.py and an objective function. Currently, there are several ways to run setup.py which are descibed in chapter **Complex Method -- Python**.


Test functions
----

The source files can be found under ComplexMeethod/complexrf/src/testfunctions

This folder contains several testfunctions that can used to test the complexrf with. They are named objfunc*.py. The user can simply use the existing file as a template. There is an excellant wiki where mathematical test functions are listed -- search for *optimization test function*.


Documentation
----

The source files can be found under ComplexMeethod/complexrf/docs/

Restructured text is used for documentation along with sphinx engine. The site is hosted on readthedocs, which is where you are probably reading this text.




Software Prerequisites
==========

There are two version of the ComplexMethod available. 
An implementation in python as well as in Matlab. 
To use the python code, Python 3.8.x (or higher) along with numpy are needed. The matlab source files require Matlab from MathWorks. 

The terminal based installation given here are for ubuntu based systems. Nonetheless, the source code for python and matlab should work in mac and windows systems, provided the necessary packages are installed.

Git
----

Git is optional and is not required to run the optimizer. To clone the complexmethod repository, git must be installed in your system. The following links will help you understand the basics of git, which is prerequisite if you would like to use the code and contribute to this project.

	| http://git-scm.com/book/en/v2
	| https://guides.github.com/introduction/flow/index.html

To install git from a terminal run:

::

	$ sudo apt-get install git 

Once you have git installed, clone a copy of the repository from github. 

In a terminal window:
 ::
 
	 $ mkdir complexmethod 
	 $ cd complexmethod
	 $ git clone https://github.com/Robbie025/ComplexMethod.git


Python
------

A version of complex method written in python  is available in the git repository in the folder *python*.

Links to install python, numpy and matplotlib:


	| https://www.python.org/downloads/
	| http://www.numpy.org/


Sphinx
------

Sphinx is used for documentation of the project and is not needed to run the complexmethod. If you commit the changes properly, readthedocs will update the documentaiton automatically. To install sphinx, in a ubuntu terminal window run:

::

	$ sudo apt-get install python-sphinx
For installation on other platforms see :

	|  https://www.sphinx-doc.org
The source files can be found in the *source* folder. To build the documentation, in a terminal window run:

:: 
	
	make html
Remember that latex must be installed for building the math equations. For ubuntu pcs: 

::

	$ sudo apt-get install texlive-full






More Information
-----------------

If you are interested in more information, please check out this site. It has tons of information to get you started on the software development process.
	http://toolbox.readthedocs.org/en/latest/

 
