Complex Method -- Matlab
==========

.. note::

	More information comming soon ....

		The complex method in matlab is provided in the /matlab folder for matlab users. complexrf.m contains the complex method.
Several sample functions are also provided. This code is part of the *TMKT48 - Design Optimization* given at the Division of Machine Design, Linköping University, Sweden. Documentation can also be found in the souce files.


example:

::

     X_low = [-2.048 -2.048]
     X_up =  [2.048 2.048]
     [X,F] = complexrf('dejong2',X_low,X_up,'maxeval',500)
