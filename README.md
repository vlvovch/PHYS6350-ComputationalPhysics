[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vlvovch/PHYS6350-ComputationalPhysics/spring2025)

# PHYS6350 Computational Physics (Spring 2025)

This repository contains the lecture notes and computer code for the graduate course PHYS6350 Computational Physics taught at the University of Houston in Spring 2023 \& Spring 2025.

The course is designed for graduate/advanced undergraduate physics students.
The focus is on the concepts behind the numerical methods used in computational physics over the implementation. For this reason, most of the code is in Python and uses Jupyter Notebooks for presentation. 
For the same reason, many standard routines (such as linear equation solvers) are reimplemented.

The materials presented in this repository should be useful both for self-study, as a reference for the course PHYS6350 Computational Physics, and for instructors to use as a reference for their own courses.

## Online textbook (lecture notes)

The lecture notes have been done in Jupyter notebook format and converted to HTML using Jupyter Book. 
The online version of the lecture notes is available at [https://vovchenko.net/computational-physics/](https://vovchenko.net/computational-physics/)


## Other textbooks
There is no assigned textbook but the following textbooks can be useful:
- [**Computational Physics**](https://www.amazon.com/Computational-Physics-Mark-Newman/dp/1480145513) by Mark Newman (Some parts of this text are available on the author’s website: http://www-personal.umich.edu/~mejn/cp/index.html)
- [**Numerical Recipes: The Art of Scientific Computing, Third Edition**](https://www.amazon.com/Numerical-Recipes-3rd-Scientific-Computing/dp/0521880688/) -	 by W.H. Press, et al.

Many of the problems and examples are taken from the first book, these are referenced in the lecture notes where applicable.

## Syllabus

The syllabus for the course is available for [Spring 2023](syllabus/Syllabus_Phys6350_Spring2023.pdf) and [Spring 2025](syllabus/Syllabus_Phys6350_Spring2025.pdf) editions.

## Lecture notes and code

- Lecture slides: folder [``slides``](slides/)
- Sample programs and notebooks: folder  [``code``](code/)
- Jupyter Book: folder [``book``](book/)

## Course outline

1. Plotting [Lecture ([pdf](slides/Lecture2-Plotting-MachinePrecision.pdf)), Code ([ipynb](code/1_Plotting/1_Plotting.ipynb))]

2. Floating-Point Precision [Lecture ([pdf](slides/Lecture2-Plotting-MachinePrecision.pdf)), 
Code ([ipynb](code/2_FloatingPointPrecision/2_FloatingPointPrecision.ipynb))]

3. Function Interpolation [Lecture ([pdf](slides/Lecture3-Interpolation.pdf)), Code ([ipynb](code/3_Interpolation/3_Interpolation.ipynb))]
    - Linear interpolation
    - Polynomial Interpolation in Lagrange and Newton forms
    - Bilinear interpolation (two variables)

4. Linear Algebra and Matrices
    - Lecture 1 [[pdf](slides/Lecture4-LinearAlgebra.pdf), Code ([ipynb](code/4_LinearAlgebra/4_LinearAlgebra.ipynb))]
        - Gaussian elimination
        - Pivoting
        - LU-decomposition
    - Lecture 2 [[pdf](slides/Lecture5-LinearAlgebra-2.pdf), Code ([ipynb](code/4_LinearAlgebra/4_LinearAlgebra.ipynb))]
        - Matrix inversion
        - Tri- and band-diagonal systems
        - QR decomposition
        - Eigenvalue problem

5. Non-Linear Equations
    - Lecture 1 [[pdf](slides/Lecture6-NonlinearEquations.pdf), [pptx](slides/Lecture6-NonlinearEquations.pptx) (for animations), Code ([ipynb](code/5_NonlinearEquations/5_NonlinearEquations.ipynb)), Generate Animations ([ipynb](code/5_NonlinearEquations/5_NonlinearEquations-Animation.ipynb))]
        - Bisection method
        - Secant and Newton-Raphson method
    - Lecture 2 [[pdf](slides/Lecture7-NonlinearEquations-2.pdf), [pptx](slides/Lecture7-NonlinearEquations-2.pptx) (for animations)]
        - Roots of a polynomial (Code ([ipynb](code/5_NonlinearEquations/5b_PolynomialRoots.ipynb))
        - Multi-dimenstional Newton and Broyden methods (Code ([ipynb](code/5_NonlinearEquations/5c_NonlinearEquationsMulti.ipynb))
        - Search for extrema (minimum/maximum) (Code ([ipynb](code/5_NonlinearEquations/5d_SearchForExtrema.ipynb))

6. Numerical integration
    - Lecture 1 [Lecture ([pdf](slides/Lecture8-NumericalIntegration.pdf), [pptx](slides/Lecture8-NumericalIntegration.pptx) (for animations), Code ([ipynb](code/6_NumericalIntegration/6_NumericalIntegration.ipynb)))]
        - Rectangle, trapezoidal, and Simpson rules
        - Composite and adaptive rules, error control
        - Improper integrals
    - Lecture 2 [Lecture ([pdf](slides/Lecture9-NumericalIntegration-2.pdf), [pptx](slides/Lecture9-NumericalIntegration-2.pptx)), Code ([ipynb](code/6_NumericalIntegration/6b_QuadraturesHighOrder.ipynb))]
        - Newton-Cotes quadrature
        - Clenshaw-Curtis quadrature
        - Gaussian quadrature

7. Numerical differentiation [Lecture ([pdf](slides/Lecture10-NumericalDifferentiation.pdf)), Code ([ipynb](code/7_NumericalDerivatives/7_NumericalDerivatives.ipynb))]
    - Forward, backward, and central difference
    - High-order approximations and derivatives
    - Balancing truncation and round-off errors
    - Automatic differentiation


8. Ordinary differential equations (ODE)
    - Lecture 1 [[pdf](slides/Lecture11-OrdinaryDifferentialEquations.pdf), [pptx](slides/Lecture11-OrdinaryDifferentialEquations.pptx), Code ([ipynb](code/8_OrdinaryDifferentialEquations/8_ODE.ipynb))]
        - Euler, midpoint (RK2), and RK4 methods
        - Adaptive step
        - Stiff equations, stability, and implicit methods
        - Systems of ODEs
        - Simple pendulum
     - Lecture 2 [[pdf](slides/Lecture12-OrdinaryDifferentialEquations-2.pdf), [pptx](slides/Lecture12-OrdinaryDifferentialEquations-2.pptx), Code ([ipynb](code/8_OrdinaryDifferentialEquations/8_ODE.ipynb))]
        - Leapfrog, modified midpoint and Bulirsch-Stoer methods
        - Simple pendulum
        - Comet motion, SIR model
        - Boundary value problems and the shooting method

9. Classical mechanics problems [Lecture ([pdf](slides/Lecture13-ClassicalMechanicsProblems.pdf), [pptx](slides/Lecture13-ClassicalMechanicsProblems.pptx)), Code ([ipynb](code/8_OrdinaryDifferentialEquations/8b_ClassicalMechanics.ipynb))]
    - Three-body problem
    - Non-linear pendulum
    - Double pendulum and chaotic motion (simulation + animation code)

10. Molecular dynamics [Lecture ([pdf](slides/Lecture14-MolecularDynamics.pdf), [pptx](slides/Lecture14-MolecularDynamics.pptx)), Code ([ipynb](code/9_MolecularDynamics/9_MolecularDynamics.ipynb))]
    - Classical N-body problem
    - Lennard-Jones fluid
    - Equilibration and thermodynamics


11. Partial differential equations (PDE)
    - Lecture 1 [[pdf](slides/Lecture15-PartialDifferentialEquations.pdf), [pptx](slides/Lecture15-PartialDifferentialEquations.pptx), Code ([ipynb](code/10_PDE/10_PDE.ipynb))]
        - Boundary value problems
        - Finite difference method
        - Jacobi and Gauss-Seidel methods
    - Lecture 2 [[pdf](slides/Lecture16-PartialDifferentialEquations-2.pdf), [pptx](slides/Lecture16-PartialDifferentialEquations-2.pptx), Code ([ipynb](code/10_PDE/10_PDE.ipynb))]
        - Initial value problems
        - FTCS, implicit, and Crank-Nicolson schemes
        - Heat equation 
        - Wave equation

12. Random numbers and Monte Carlo methods
    - Lecture 1 [[pdf](slides/Lecture17-RandomNumbers.pdf), [pptx](slides/Lecture17-RandomNumbers.pptx), Code ([ipynb](code/11_RandomNumbers/11_RandomNumbers.ipynb))]
        - Pseudo-random number generators
        - Computing integrals
            - As the area under the curve
            - Mean-value method
        - Sampling non-uniformly distributed random numbers
            - Inverse transform sampling
            - Rejection sampling
    - Lecture 2 [[pdf](slides/Lecture18-RandomNumbers-2.pdf), [pptx](slides/Lecture18-RandomNumbers-2.pptx), Code ([ipynb](code/11_RandomNumbers/11_RandomNumbers.ipynb))]
        - Multi-dimensional integrals
        - Importance sampling

13. Statistical physics problems
    - Lecture 1 [[pdf](slides/Lecture19-StatisticalPhysics.pdf), [pptx](slides/Lecture19-StatisticalPhysics.pptx), Code ([ipynb](code/12_StatisticalPhysics/12_StatisticalPhysics.ipynb))]
        - Markov Chain Monte Carlo (MCMC)
        - Metropolis-Hastings algorithm
        - Simulation of the 2D Ising model
    - Lecture 2 [[pdf](slides/Lecture20-StatisticalPhysics-2.pdf), [pptx](slides/Lecture20-StatisticalPhysics-2.pptx), Code ([ipynb](code/12_StatisticalPhysics/12_StatisticalPhysics-2.ipynb))]
        - Simulated annealing
        - Percolation threshold simulation

14. Quantum mechanics
    - Matrix method for eigenenergies and eigenstates
    - Time-dependent Schroedinger equation
    - Variational method
    [[pdf](slides/Lecture21-QuantumMechanics.pdf), [pptx](slides/Lecture21-QuantumMechanics.pptx), Code ([ipynb](code/13_QuantumMechanics/13_QuantumMechanics.ipynb))]

15. Fourier transform [Lecture ([pdf](slides/Lecture22-Fourier.pdf)), Code ([ipynb](code/14_FFT/14_FFT.ipynb))]
    - Discrete Fourier Transform
    - Fast Fourier Transform

16. Introduction to Machine Learning
    [[pdf](slides/SpecialLecture-MLIntro.pdf), [pptx](slides/SpecialLecture-MLIntro.pptx)]
