[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vlvovch/PHYS6350-ComputationalPhysics/spring2025)

# PHYS6350 Computational Physics (Spring 2025)

This repository contains the lecture notes and computer code for the graduate course PHYS6350 Computational Physics taught at the University of Houston taught in Spring 2025.

The course is designed for graduate/advanced undergraduate physics students.
The focus is on the concepts behind the numerical methods used in computational physics over the implementation. For this reason, most of the code is in Python and uses Jupyter Notebooks for presentation. 
For the same reason, many standard routines (such as linear equation solvers) are reimplemented.


## Textbooks
There is no assigned textbook but the following textbooks can be useful:
- [**Computational Physics**](https://www.amazon.com/Computational-Physics-Mark-Newman/dp/1480145513) by Mark Newman (Some parts of this text are available on the author’s website: http://www-personal.umich.edu/~mejn/cp/index.html)
- [**Numerical Recipes: The Art of Scientific Computing, Third Edition**](https://www.amazon.com/Numerical-Recipes-3rd-Scientific-Computing/dp/0521880688/) -	 by W.H. Press, et al.

Many of the problems and examples are taken from the first book, these are referenced in the lecture notes where applicable.

## Syllabus

The syllabus for the Spring 2025 edition of the course is available [here](Syllabus_Phys6350_spring2025.pdf)

## Lecture notes and code

- Lecture slides: folder [``slides``](slides/)
- Sample programs and notebooks: folder  [``code``](code/)

## Course outline

1. Plotting [Lecture ([pdf](slides/Lecture2-01-16-25-Plotting-MachinePrecision.pdf)), 
Code ([ipynb](code/1_Plotting/1_Plotting.ipynb))]

2. Floating-Point Precision [Lecture ([pdf](slides/Lecture2-01-16-25-Plotting-MachinePrecision.pdf)), 
Code ([ipynb](code/2_FloatingPointPrecision/2_FloatingPointPrecision.ipynb))]

3. Function Interpolation [Lecture ([pdf](slides/Lecture3-01-23-25-Interpolation.pdf)), Code ([ipynb](code/3_Interpolation/3_Interpolation.ipynb))]
    - Linear interpolation
    - Polynomial Interpolation in Lagrange and Newton forms
    - Bilinear interpolation (two variables)

4. Linear Algebra and Matrices
    - Lecture 1 [[pdf](slides/Lecture4-01-28-25-LinearAlgebra.pdf), Code ([ipynb](code/4_LinearAlgebra/4_LinearAlgebra.ipynb))]
        - Gaussian elimination
        - Pivoting
        - LU-decomposition
    - Lecture 2 [[pdf](slides/Lecture5-01-30-25-LinearAlgebra-2.pdf), Code ([ipynb](code/4_LinearAlgebra/4_LinearAlgebra.ipynb))]
        - Matrix inversion
        - Tri- and band-diagonal systems
        - QR decomposition
        - Eigenvalue problem

5. Non-Linear Equations
    - Lecture 1 [[pdf](slides/Lecture6-02-04-25-NonlinearEquations.pdf), [pptx](slides/Lecture6-02-04-25-NonlinearEquations.pptx) (for animations), Code ([ipynb](code/5_NonlinearEquations/5_NonlinearEquations.ipynb)), Generate Animations ([ipynb](code/5_NonlinearEquations/5_NonlinearEquations-Animation.ipynb))]
        - Bisection method
        - Secant and Newton-Raphson method
    - Lecture 2 [[pdf](slides/Lecture7-02-06-25-NonlinearEquations-2.pdf), [pptx](slides/Lecture7-02-06-25-NonlinearEquations-2.pptx) (for animations)]
        - Roots of a polynomial (Code ([ipynb](code/5_NonlinearEquations/5b_PolynomialRoots.ipynb))
        - Multi-dimenstional Newton and Broyden methods (Code ([ipynb](code/5_NonlinearEquations/5c_NonlinearEquationsMulti.ipynb))
        - Search for extrema (minimum/maximum) (Code ([ipynb](code/5_NonlinearEquations/5d_SearchForExtrema.ipynb))

6. Numerical integration
    - Lecture 1 [[pdf](slides/Lecture8-02-11-25-NumericalIntegration.pdf), [pptx](slides/Lecture8-02-11-25-NumericalIntegration.pptx) (for animations)]
        - Rectangle, trapezoidal, and Simpson rules
        - Composite and adaptive rules, error control
        - Improper integrals
    - Lecture 2 [[pdf](slides/Lecture9-02-13-25-NumericalIntegration-2.pdf), [pptx](slides/Lecture9-02-13-25-NumericalIntegration-2.pptx)]
        - Newton-Cotes quadrature
        - Clenshaw-Curtis quadrature
        - Gaussian quadrature

7. Numerical differentiation [[pdf](slides/Lecture10-02-18-25-NumericalDifferentiation.pdf)]
    - Forward, backward, and central difference
    - High-order approximations and derivatives
    - Balancing truncation and round-off errors
    - Automatic differentiation


8. Ordinary differential equations (ODE)
    - Lecture 1 [[pdf](slides/Lecture11-02-20-25-OrdinaryDifferentialEquations.pdf), [pptx](slides/Lecture11-02-20-25-OrdinaryDifferentialEquations.pptx)]
        - Euler, midpoint (RK2), and RK4 methods
        - Adaptive step
        - Stiff equations, stability, and implicit methods
        - Systems of ODEs
        - Simple pendulum
     - Lecture 2 [[pdf](slides/Lecture12-02-25-25-OrdinaryDifferentialEquations-2.pdf), [pptx](slides/Lecture12-02-25-25-OrdinaryDifferentialEquations-2.pptx)]
        - Leapfrog, modified midpoint and Bulirsch-Stoer methods
        - Simple pendulum
        - Comet motion, SIR model
        - Boundary value problems and the shooting method

9. Classical mechanics problems [[pdf](slides/Lecture13-02-27-25-ClassicalMechanicsProblems.pdf), [pptx](slides/Lecture13-02-27-25-ClassicalMechanicsProblems.pptx)]
    - Three-body problem
    - Non-linear pendulum
    - Double pendulum and chaotic motion (simulation + animation code)

10. Molecular dynamics [[pdf](slides/Lecture14-03-03-25-MolecularDynamics.pdf), [pptx](slides/Lecture14-03-03-25-MolecularDynamics.pptx)]
    - Classical N-body problem
    - Lennard-Jones fluid
    - Equilibration and thermodynamics


11. Partial differential equations (PDE)
    - Lecture 1 [[pdf](slides/Lecture15-03-18-25-PartialDifferentialEquations.pdf), [pptx](slides/Lecture15-03-18-25-PartialDifferentialEquations.pptx)]
        - Boundary value problems
        - Finite difference method
        - Jacobi and Gauss-Seidel methods
    - Lecture 2 [[pdf](slides/Lecture16-03-20-25-PartialDifferentialEquations-2.pdf), [pptx](slides/Lecture16-03-20-25-PartialDifferentialEquations-2.pptx)]
        - Initial value problems
        - FTCS, implicit, and Crank-Nicolson schemes
        - Heat equation 
        - Wave equation

12. Random numbers and Monte Carlo methods
    - Lecture 1 [[pdf](slides/Lecture17-03-27-25-RandomNumbers.pdf), [pptx](slides/Lecture17-03-27-25-RandomNumbers.pptx)]
        - Pseudo-random number generators
        - Computing integrals
            - As the area under the curve
            - Mean-value method
        - Sampling non-uniformly distributed random numbers
            - Inverse transform sampling
            - Rejection sampling
    - Lecture 2 [[pdf](slides/Lecture18-04-01-25-RandomNumbers-2.pdf), [pptx](slides/Lecture18-04-01-25-RandomNumbers-2.pptx)]
        - Multi-dimensional integrals
        - Importance sampling

13. Statistical physics problems
    - Lecture 1 [[pdf](slides/Lecture19-04-03-25-StatisticalPhysics.pdf), [pptx](slides/Lecture19-04-03-25-StatisticalPhysics.pptx)]
        - Markov Chain Monte Carlo (MCMC)
        - Metropolis-Hastings algorithm
        - Simulation of the 2D Ising model
    - Lecture 2 [[pdf](slides/Lecture20-04-06-25-StatisticalPhysics-2.pdf), [pptx](slides/Lecture20-04-06-25-StatisticalPhysics-2.pptx)]
        - Simulated annealing
        - Percolation threshold simulation

14. Quantum mechanics
    - Matrix method for eigenenergies and eigenstates
    - Time-dependent Schroedinger equation

15. Data Analysis and Curve Fitting, Parameter Estimation
    - Data and Uncertainties
    - chi2 minimization
    - Maximum likelihood
    - Bayesian analysis

16. Introduction to Machine Learning (tentative)


17. Introduction to Parallel Computing (tentative)
    - Basic terminology
    - OpenMP examples
    - Molecular dynamics with NVIDIA CUDA ([cpp](https://github.com/vlvovch/lennard-jones-cuda))
