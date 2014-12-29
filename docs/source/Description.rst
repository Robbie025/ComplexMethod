Description
===========
The Complex method was first presented by Box [1], and later improved by Guin [36]. The method is a constraint simplex method, hence the name Complex, developed from the Simplex method by Spendley et al [79] and Nelder Mead, [64]. Similar related methods go under names such as Nelder-Mead Simplex. The main difference between the Simplex method and the complex method is that the Complex method uses more points during the search process.

In the Complex method the word complex refers to a geometric shape with k>=n+1, points in an n-dimensional space. These k points are known as vertices of the complex. To make the explanation of the algorithm simple we will focus on a two-dimensional space and a complex consisting of four vertices, i.e. n=2 and k=4. Typically the number of points in the complex, k, is twice as many as the number of design variables, n. The starting points are generated using random numbers. Each of the k points in the complex could be expressed according to (43) where x l and x u are the upper and lower variable limits and R a random number in the interval [0, 1].

.. math::  x_{i} =&x_{j}^i  + R ( x_{j}^u -  x_{j}^l) \\  i&=1,2,3...k\\j & =1,2...n

In the Complex method the word complex refers to a geometric shape with k  n+1
points in an n-dimensional space. These k points are known as vertices of the complex.
To make the explanation of the algorithm simple we will focus on a two-dimensional
space and a complex consisting of four vertices, i.e. n=2 and k=4. Typically the number
of points in the complex, k, is twice as many as the number of design variables, n. The
starting points are generated using random numbers. Each of the k points in the complex
could be expressed according to (43) where x l and x u are the upper and lower variable
limits and R a random number in the interval [0, 1].


The main idea of the algorithm is to replace the worst point by a new point obtained
by reflecting the worst point through the centroid of the remaining points in the complex,
as illustrated in Figure 18.
The centroid, x c , of the points in the complex excluding the worst point x w could be
calculated according to

.. math::  x_{c,j} &= \frac{1}{k-1}  (\sum_{i=1}^k x_{i,j}) - x_{w,j} \\ j& = 1,2,..n

The new point is now calculated as the reflection of the worst point through the centroid
by a factor

.. math:: x_{new} = x_{c} +  \alpha * (x_{c}-x_{w})

The reflection coefficient :math:`\alpha` should equal 1.3 according to Box. If the new point is better
than the worst, x w is replaced by x new and the procedure starts over by reflecting the point
that is worst in the new complex.
If the new point is still the worst it is moved halfway towards the centroid according
to

.. math:: x_{new}^{'} = x_{c} +  \frac{\alpha}{2}(x_{c}-x_{w})

Equitation (46) could be rearranged by substituting :math:`\alpha * (x_{c}-x_{w}) =  x_{new} - x_{c}` from equation (45) yielding

.. math:: x_{new}^{'} = \frac{\alpha}{2}(x_{c} + x_{new})

The procedure of moving the worst point towards the centroid is repeated until the new
points stop repeating as the worst.


The procedure outlined is carried out until the complex has converged or until a pre
described number of evaluations is reached. Convergence could be measured either in the
function space or in variable space. In the function space the complex is considered
converged if the difference between the maximum and minimum function values of all
the points in the complex is less then a pre described measure,  f , see equation (48).
Likewise, the complex has converged in the variable space if the maximum difference in all dimensions is less that a certain value  v, see equation (49). Equation (48) thus
constitutes a measure of the spread of the complex in function space whereas equation
(49) expresses the spread in parameter space As has been stated earlier, the complex is designed to handle constraints. Constraints
in the form of limits on the design variables is handle by checking if the new point is
within the variable limits. If not it is move to the feasible side of the limit. If the new
points is violating any other constraint it is moved halfway towards the centroid.

The working principle of the complex method is here outlined using pseudo code.

#Generate starting points
Calculate objective function
Evaluate constraints
Identify the worst point
While stop criteria is not meet
Calculate centroid
Reflect worst point through centroid
Make sure the new point is within the variable limits
Calculate objective function for the new point
Evaluate constraints
Identify the worst point
While the new point is the worst or a constraint is violated
Move the new point towards the centroid
Calculate the objective function
Evaluate constraints
end while
Identify the worst point in the new complex
Check stop criteria
end while
Output the optimal point
