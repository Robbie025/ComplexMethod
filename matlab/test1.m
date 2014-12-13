% Syntax:  obj = test1(x)
% Input parameters:
%    x          - A vector of real values
% Output parameters:
%    obj        - the objective function value 
%
function obj=test1(x)
obj=(x(1)-5)^2+(x(2)-5)^2+0.1*x(1)*x(2);

