%
% This function implements the ROSENBROCK valley (DE JONG's Function 2).
%
% Syntax:  ObjVal = dejong2(x)
%
% Input parameters:
%    x          - A pair of real values
%
% Output parameters:
%    ObjVal    - One real value according to Rosenbrock's function
%                


function ObjVal = dejong2(x);

ObjVal = 100*(x(1,1)^2-x(1,2))^2+(1-x(1,1))^2;

