
Software Prerequisites
==========
Git
----

To clone the complexmethod repository, git must be installed in your system. The following links will help you understand the basics of git, which is prerequisite if you would like to use the code and contribute to this project.

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

Links to install python and numpy:


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


Matlab
------
You need Matlab from mathworks to run the code. The intention is to have code compatible with both matlab and Octave. 


	https://www.mathworks.com/


More Information
-----------------

If you interested in more information, please check out this site. It has tons of information to get you started on the software development process.
	http://toolbox.readthedocs.org/en/latest/

 