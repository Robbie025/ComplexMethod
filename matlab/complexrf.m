function [xopt,func,x_hist,f_hist,exitflag,output] = complexrf(Obj_fcn,x_lower,x_upper,varargin) 
% COMPLEXRF Multidimensional constrained nonlinear minimization using the Complex method.
%   Referens: Box M. J. (1965), A new method of constraint optimization and a comparison with other methods, 
%             Computer Journal 8:42-52
%             Krus P., Andersson J., Optimizing Optimization for Design Optimization, 
%             in Proceedings of ASME Design Automation Conference, Chicago, USA, September 2-6, 2003
%
%   Syntax:  [xopt,func,x_hist,f_hist,exitflag,output] = complexrf(Obj_fcn,x_lower,x_upper,'parameter name',parameter value, .....)
%
%      X = COMPLEXRF(OBJ_FCN,X_LOWER,X_UPPER) minimzes the function OBJ_FCN within the bounds given by X_LOWER and 
%      X_UPPER and returns the minimizer X. OBJ_FCN taxes X as an input and returns a scalar value. 
%      X, X_LOWER and X_UPPER could be scalars or vectors of the same size. 
%
%      X = COMPLEXRF(OBJ_FCN,X_LOWER,X_UPPER,'parameter_name',value,'parameter_name',value,..... )
%      minimizes with the default optimization parameters replaced by values given in the function call. 
%      Available parameters and their default values are: 
%                               'maxeval'     maximum number of evaluations [500]
%                               'k'           number of points in the complex [2*no_of_parameters]
%                               'tolx'        tolerance for convergence in parameter variation [0.0001]
%                               'tolfunc'     tolerance for convergence in function values [0.00001]
%                               'alfa'        reflection distance [1.3]
%                               'rfak'        randomization factor [0.3]
%                               'gamma'       forgetting factor [0.3]
%
%      [X,FVAL]= COMPLEXRF(OBJ_FCN,X_LOWER,X_UPPER) returns the value of the objective function,
%      described in OBJ_FCN, at X.
%
%      [X,FVAL,X_HIST] = COMPLEXRF(...) returns the history of the evolution for each of the optimization parameters and
%      the maximum normalized spread of the complex for each iteration. 
%      The normalized spread is also used as convergence criteria. X_HIST is a matrix with size [NoIterations,Noparams +1].
%
%      [X,FVAL,X_HIST,F_HIST] = COMPLEXRF(...) returns the history of the evolution of the objective function and
%      the spread of the objective function values in the complex for each iteration. 
%      F_HIST is a matrix with size [NoIterations,2].
%
%      [X,FVAL,X_HIST,F_HIST,EXITFLAG] = COMPLEXRF(...) returns a string EXITFLAG that 
%      describes the exit condition of COMPLEXRF.  
%      If EXITFLAG is:
%       -1 an error occurred
%        0 max number of function evaluations reached.
%        1 convergence in parameter values
%        2 convergence in function values.
%
%    [X,FVAL,X_HIST,F_HIST,EXITFLAG,OUTPUT] = COMPLEXRF(...) returns a structure OUTPUT with the number
%    of iterations taken in OUTPUT.iterations and the number of evaluations in OUTPUT.evaluations.
%
%    Example:
%
%       X_low = [-2.048 -2.048]
%       X_up =  [2.048 2.048]
%       [X,F] = COMPLEXRF('DeJong2',X_low,X_up,'maxeval',400)
%
%       minimzes the function DeJong2 within the limits X_low and X_up and returns the optimal parameters to X
%       and the minimal value of DeJong2 obtained at  X to F. The default number of maximum evaluations is set to 400.
%
%   COMPLEXRF uses the Complex-RF optimization method for direct search.
% Author: Johan Andersson, Department of Mechnical Engineering, Linköping University
% History: File created 2003-10-10
% Setting the default values for the algorithm
MaxEvals = 500;          % maximum Number of evaluations
Alfa = 1.3;             % Reflection distance
Rfak = 0.3;             % Randomization factor
Gamma = 0.3;            % Forgetting factor
TolFunc = 0.00001;        % Tolerance for function convergence
TolX = 0.0001;           % Tolerance for parameter convergence
IterMax = 30;           % Max iterations when moving the newpoint towards the center and best
b=4;                    % Constant used when moving the newpoint towards the center and best
% Check that we have sufficient input
if nargin < 3, 
   error('Complex requires at least three input arguments'); 
end
% Make sure that the we have the right limits on the variables
n1=length(x_lower);
n2=length(x_upper);
if n1 ~= n2,
    error('Upper and lower limits must have the same number of arguments');
end
if ~min((max(x_upper,x_lower) == (x_upper))),
    error ('The upper limits must be larger then the lower limits');
end
Nparams = n1;            % Number of optimization parameters
k=2*Nparams;             % number of points in the Complex
if Nparams == 1,
    k=3;
end
fprintf('\n** Complex optimization started **\n')
% assign parameter values if they are given in the function call
if nargin > 3,
	[n2 n3] = size(varargin);
	%nn=floor(n3/2)
	fprintf('The following parameters have been supplied by the user.\n')
	for i=1:2:n3,
        if strcmpi(varargin{i},'alfa'),
            Alfa=varargin{i+1};
            fprintf('alfa = %g \n',varargin{i+1});
        end
        if strcmpi(varargin{i},'gamma'),
            Gamma=varargin{i+1};
            fprintf('gamma = %g \n',varargin{i+1});
        end
        if strcmpi(varargin{i},'maxeval'),
            MaxEvals=varargin{i+1};
            fprintf('maxeval = %g \n',varargin{i+1});
        end
        if strcmpi(varargin{i},'Rfak'),
            Rfak=varargin{i+1};
            fprintf('rfak = %g \n',varargin{i+1});
        end
        if strcmpi(varargin{i},'TolX'),
            TolX=varargin{i+1};
            fprintf('TolX = %g \n',varargin{i+1});
        end
        if strcmpi(varargin{i},'TolFunc'),
            TolFunc=varargin{i+1};
            fprintf('TolFunc = %g \n',varargin{i+1});
        end
        if strcmpi(varargin{i},'k'),
            k=varargin{i+1};
            fprintf('k = %g \n',varargin{i+1});
        end
	end
end
fprintf('\nNumber of evaluations \n');
fprintf('%5.0f ',0);
% Start of Complex method
exitflag = -1;
conv_cond = 0;
NoEvals = 0; 
Iterations = 0;
jfmin=1;
jfmax=1;
% kf implements the forgetting principle. Each objective value will be increased with kf each iteration
kf = 1 - (Alfa/2)^(Gamma/k);
% Create initial Complex
x=ones(k,1)*x_lower + ones(k,1)*(x_upper-x_lower).*rand(k,Nparams);
% Convert to inline function as needed.
Obj_fcn = fcnchk(Obj_fcn,length(varargin));
% Evaluate function values for initial complex
for i = 1:k,
    f(i)=feval(Obj_fcn,x(i,:));
    NoEvals = NoEvals + 1;
    fprintf('\b\b\b\b\b\b');
    fprintf('%5.0f ',NoEvals);
end
allx=x;         % Store all x values 
allf=f';        % Store all f values
allx(:,Nparams+1) = abs(max((max(x)-min(x))./(x_upper-x_lower)));   % store the spread of the initial comlex
allf(:,2) = abs(max(f)-min(f));                                     % store the spread in function values
%Do the Complex iteration
while NoEvals < MaxEvals,
    % Check convergence
    if min (f) == 0,
        if abs(max(f)-min(f)) <= TolFunc,
            conv_cond = 1;
            break;
        end
    elseif abs(max(f)-min(f))/abs(min(f)) <= TolFunc,
            conv_cond = 1;
            break;
    end
    if abs((max((max(x)-min(x))./(x_upper-x_lower)))) <= TolX,
        conv_cond = 2;
        break;
    end
    % Increase all f-values with a factor kf. This is the forgetting principle.
    f = f + (max(f)-min(f))*kf;
    % Identify best and worst point
    [fmin jfmin] = min(f);
    [fmax jfmax] = max(f);
    % Calculate centroid
    xc = (sum(x) - x(jfmax,:)) / (k-1);
    %refelct worst point through centroid 
    xnew_1 = xc + (xc-x(jfmax,:)).*Alfa;
    % Add some random noise to the new point
    xnew_2 = xnew_1 + Rfak.*(x_upper -x_lower)*max((max(x)-min(x))./(x_upper-x_lower)).*(rand(1,Nparams)-0.5);
    % Make sure that xnew_2 is within the limits
     xnew_3=min(xnew_2,x_upper);
     xnew=max(xnew_3,x_lower);
    %Replace the worst point by the new one
    x(jfmax,:) = xnew;
    % Evaluate the new point
    f(jfmax)=feval(Obj_fcn,x(jfmax,:));
    NoEvals = NoEvals + 1;
        
    % See if the new point is still the worst.
    [fmax jfmax_new] = max(f);
    iter = 0;
    while (jfmax_new == jfmax) & (iter < IterMax) & (NoEvals < MaxEvals),
        a1 = 1 -exp(-iter/b);
        xnew_2 = ((xc*(1-a1) + x(jfmin,:)*a1) + xnew)./2 + Rfak.*(x_upper -x_lower)*max((max(x)-min(x))./(x_upper-x_lower)).*(rand(1,Nparams)-0.5);
        % Make sure that xnew_2 is within the limits
        xnew_3=min(xnew_2,x_upper);
        xnew=max(xnew_3,x_lower);
        %Replace the worst point by the new one
        x(jfmax,:) = xnew;
        % Evaluate the new point
        f(jfmax)=feval(Obj_fcn,x(jfmax,:));
        % See if the new point is still the worst.
        [fmax jfmax_new] = max(f);
        iter = iter + 1;
        NoEvals = NoEvals + 1;
               
        fprintf('\b\b\b\b\b\b');
        fprintf('%5.0f ',NoEvals);
    end         % Keep on reflecting the worst point until it is not worst any more.
    Iterations = Iterations + 1;
%     store the evolution of the optimization in the variables allx and allf
    allx(Iterations+k,1:Nparams)=x(jfmax,:);
    allf(Iterations+k,1)=f(jfmax);
    allx(Iterations+k,Nparams+1) = abs(max((max(x)-min(x))./(x_upper-x_lower)));
    allf(Iterations+k,2) = abs(max(f)-min(f));
    fprintf('\b\b\b\b\b\b');
    fprintf('%5.0f ',NoEvals);
end % Main Complex loop
% Identify best and worst point
[fmin jfmin] = min(f);
[fmax jfmax] = max(f);

fprintf('\n\n** Optimization stopped **\n\n')
if conv_cond == 2
    fprintf('Convergence in parameter values\n\n')
    output.convergence = 'Convergence in parameter values';
elseif conv_cond == 1
    fprintf('Convergence in function values\n\n')
    output.convergence = 'Convergence in function values';
else
    fprintf('Max number of evaluation reached\n\n')
    output.convergence = 'Max number of evaluation reached';
end
fprintf('Number of evaluations = %g.\n', NoEvals)
fprintf('Number of iterations = %g.\n', Iterations)
fprintf('Minimum function value = %g.\n',f(jfmin))
fprintf('Maximum function value = %g.\n',f(jfmax))
fprintf('Best point found at: \t \t min(x)    max(x) \n')
for i=1:Nparams,
    fprintf('x(%g) = %8.4g           %8.4g \t %8.4g\n',i,x(jfmin,i),min(x(:,i)),max(x(:,i)));
end
xopt = x(jfmin,:);
func = f(jfmin);
x_hist=allx;
f_hist=allf;
output.iterations = Iterations;
output.funcCount = NoEvals;
output.algorithm = 'Complex algorithm direct search';
output.fmin = f(jfmin);
output.fmax = f(jfmax);
if NoEvals >= MaxEvals, 
   exitflag = 0;
elseif (conv_cond == 2) 
    exitflag = 1;
elseif (conv_cond == 1),
    exitflag = 2;
end
