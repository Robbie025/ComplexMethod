import numpy as np
import math

def install(a):
        """ Egg Holder function  f(512, 404.2319)=-959.6407

Also known as Rosenbrock banana function or Rosenbrock Valley function 
http://en.wikipedia.org/wiki/Test_functions_for_optimization

f(x1,x2) = -(x2+47) * sin( sqrt( abs(x2+x1/2+47) ))- x1 * sin( sqrt( abs(x1 - (x2+47) )))


 Input parameters:  x - A numpy array of real values
 Output			 :  One real value 

 Suggested limits -512 <= xi <= 512  i = (1,2)  
 x*= [512,404.2319] f*= -959.6407;

 
 Usage:
 >> python objfunc4.py

 or
 >> import numpy as np
 >> import objfunc4

 >> x=np.array([[1.2,2.2,-1.]])
 >> print objfunc4.install(x)    
 
        """
        x1=a.item(0)
        x2=a.item(1)
        a1 = -1 * (x2+47) * math.sin( math.pow(abs(x2+x1/2+47),0.5));
        a2 = -1 * x1 * math.sin(math.pow(abs(x1-(x2+47)),0.5));
        objval= a1 + a2        
        return objval
 
if __name__ == "__main__":
 x =np.array([512,404.2319])
 print "x= ",x," func value = ",install(x)," should be -959.6407 for [[512,404.23]] " 
