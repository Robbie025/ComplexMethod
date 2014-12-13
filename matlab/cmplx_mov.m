function M = cmplx_mov(cplx,k,n1,n2)
% This function creates a movie that describes the evolution of the complex method.
%
% Syntax: M = cmplx_mov(CPLX,K,N1,N2)
%
%   M is a movie object created from the optimization history presented in CPLX performed with
%   K points in the complex and ploted in the dimensions described by N1
%   and N2. 

% Author: Johan Andersson, Department of Mechanical Engineering Linköping University
% File created: 2003-10-22
%       modified 2004-11-18

[Iterations,N] = size(cplx);
figure
xlow_1=min(cplx(:,n1));
xlow_2=min(cplx(:,n2));
xup_1=max(cplx(:,n1));
xup_2=max(cplx(:,n2));

axis([xlow_1 xup_1 xlow_2 xup_2]);

hold;
plot(cplx(1:k,n1),cplx(1:k,n2),'.')
M(1) = getframe;
for j=2:(Iterations - k),
    clf;
    plot(cplx(j:j+k-1,n1),cplx(j:j+k-1,n2),'.')
    %axis([x_low(n1) x_up(n1) x_low(n2) x_up(n2)]);
    axis([xlow_1 xup_1 xlow_2 xup_2]);
    M(j) = getframe;
end

