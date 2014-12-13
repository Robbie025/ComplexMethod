% Dejong3.m      (OBJective function for DE JONG's Function 3)
%
% This function implements the DE JONG's Function 3.
%
% Syntax:  ObjVal = dejong3(x)
%
% Input parameters:
%    x          - A vector of real values
%
% Output parameters:
%    ObjVal    - One real value according to DeJong's function 3.
%                

% this can be donw much better without any for loop

function ObjVal = dejong3(x);

ObjVal = sum(floor(x));
%n= length(x);
%for i=1:n,
%    ObjVal = ObjVal + floor(x(i));
%end
