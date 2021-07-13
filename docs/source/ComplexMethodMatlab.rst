Complex Method -- Matlab
==========

.. note::

	More information comming soon ....

		The complex method implemented in matlab is located in the ComplexMethod/matlab folder.  
Several sample functions are also provided. This code is part of the *TMKT48 - Design Optimization* given at the Division of Machine Design, Linköping University, Sweden. Documentation can also be found in the souce files.


example:

::

     X_low = [-2.048 -2.048]
     X_up =  [2.048 2.048]
     [X,F] = complexrf('dejong2',X_low,X_up,'maxeval',500)
