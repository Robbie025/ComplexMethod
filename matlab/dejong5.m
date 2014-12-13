% Dejong5.m      (OBJective function for DE JONG's Function 5)
%
% This function implements the DE JONG's Function 5.
%
% Syntax:  ObjVal = dejong5(x)
%
% Input parameters:
%    x          - A vector of real values
%
% Output parameters:
%    ObjVal    - One real value according to DeJong's function 5.
%                
function ObjVal=dejong5(x);

a=[-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32,-32, -16, 0, 16, 32, -32, -16, 0, 16, 32;-32, -32, -32, -32, -32, -16, -16, -16, -16, -16,16, 16, 16, 16, 16, 32, 32, 32, 32, 32,0,0,0,0,0];

slask=0.002;

for j = 1:25, 
    slask = slask + 1./( j + (x(1)-a(1,j)).^6 + (x(2)-a(2,j)).^6);
end



ObjVal=500 - 1/slask;

ObjVal = - ObjVal;


