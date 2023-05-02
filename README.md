# Computational Physics course (PHYS 6350)

This repository contains the lecture notes and program code for the graduate course PHYS6350 Computational Physics at the University of Houston taught at the University of Houston.

The course is designed for graduate/advanced undergraduate physics students.
The focus is on the concepts behind the numerical methods used in computational physics over the implementation. For this reason, most of the code is in Python and uses Jupyter Notebooks for presentation. 
For the same reason, many standard routines (such as linear equation solvers are reimplemented).


## Textbooks
There is no assigned textbook but the following textbooks can be useful:
- [**Computational Physics**](https://www.amazon.com/Computational-Physics-Mark-Newman/dp/1480145513) by Mark Newman (Some parts of this text are available on the author’s website: http://www-personal.umich.edu/~mejn/cp/index.html)
- [**Numerical Recipes: The Art of Scientific Computing, Third Edition**](https://www.amazon.com/Numerical-Recipes-3rd-Scientific-Computing/dp/0521880688/) -	 by W.H. Press, et al.

Many of the problems and examples are taken from the first book, these are referenced in the lecture notes where applicable.

## Syllabus

The syllabus for the course taught in Sping 2023 is available [here](Syllabus_Phys6350_Spring23.pdf)

## Lecture notes and code

- Lecture notes: folder [``lectures``](lectures/)
- Sample programs and notebooks: folder  [``code``](code/)

## Course outline

1. Plotting [Lecture ([pdf](lectures/Lecture2-01-19-23-Plotting-MachinePrecision.pdf)), 
Code ([ipynb](code/1_Plotting/jupyter/1_Plotting.ipynb))]


2. Floating-point precision [Lecture ([pdf](lectures/Lecture2-01-19-23-Plotting-MachinePrecision.pdf)), 
Code ([ipynb](code/2_MachinePrecision/jupyter/2_FloatingPointPrecision.ipynb))]

3. Interpolation [Lecture ([pdf](lectures/Lecture3-01-24-23-Interpolation.pdf)), Code ([ipynb](code/3_Interpolation/jupyter/3_Interpolation.ipynb))]
    - Nearest-neighbor
    - Linear
    - Interpolating polynomial
    - Bilinear (two variables)

4. Non-linear equations 
    - Lecture 1 ([pdf](lectures/Lecture4-01-26-23-NonlinearEquations.pdf), [pptx](lectures/Lecture4-01-26-23-NonlinearEquations.pptx)), Code ([ipynb](code/4_NonlinearEquations/jupyter/4_NonlinearEquations.ipynb))
        - Bisection method
        - Secant and Newton-Raphson method
    - Lecture 2 ([pdf](lectures/Lecture5-01-31-23-NonlinearEquations-2.pdf), [pptx](lectures/Lecture5-01-31-23-NonlinearEquations-2.pptx))
        - Roots of a polynomial ([ipynb](code/4_NonlinearEquations/jupyter/4b_PolynomialRoots.ipynb))
        - Multi-dimenstional Newton and Broyden methods ([ipynb](code/4_NonlinearEquations/jupyter/4c_NonlinearEquationsMulti.ipynb))
        - Search for extrema (minimum/maximum) ([ipynb](code/4_NonlinearEquations/jupyter/4d_Minimization.ipynb))

5. Numerical integration
    - Lecture 1 ([pdf](lectures/Lecture6-01-31-23-NumericalIntegration.pdf), [pptx](lectures/Lecture6-01-31-23-NumericalIntegration.pptx)), Code ([ipynb](code/5_NumericalIntegration/jupyter/5_NumericalIntegration.ipynb))
        - Rectangle, trapezoidal, and Simpson rules
        - Composite and adaptive rules, error control
        - Improper integrals
    - Lecture 2 ([pdf](lectures/Lecture7-02-07-23-NumericalIntegration-2.pdf)), Code ([ipynb](code/5_NumericalIntegration/jupyter/5b_QuadraturesHighOrder.ipynb))
        - Newton-Cotes quadrature
        - Clenshaw-Curtis quadrature
        - Gaussian quadrature

6. Numerical differentiation [Lecture ([pdf](lectures/Lecture8-02-09-23-NumericalDerivatives.pdf)), 
Code ([ipynb](code/6_NumericalDerivatives/6_NumericalDerivatives.ipynb))]
    - Forward, backward, and central difference
    - High-order approximations and derivatives
    - Balancing truncation and round-off errors


7. Ordinary differential equations (ODE) [Code ([ipynb](code/7_OrdinaryDifferentialEquations/7_ODE.ipynb))]
    - Lecture 1 ([pdf](lectures/Lecture9-02-16-23-OrdinaryDifferentialEquations.pdf))
        - Euler, midpoint (RK2), and RK4 methods
        - Adaptive step
        - Stiff equations, stability, and implicit methods
        - Systems of ODEs
        - Simple pendulum
     - Lecture 2 ([pdf](lectures/Lecture10-02-21-23-OrdinaryDifferentialEquations-2.pdf)))
        - Leapfrog, modified midpoint and Bulirsch-Stoer methods
        - Simple pendulum
        - Comet motion, SIR model
        - Boundary value problems and the shooting method

8. Classical mechanics problems [Lecture ([pdf](lectures/Lecture11-02-23-23-ClassicalMechanicsProblems.pdf), [pptx](lectures/Lecture11-02-23-23-ClassicalMechanicsProblems.pptx)), Code ([ipynb](code/7_OrdinaryDifferentialEquations/7b_ClassicalMechanics.ipynb))]
    - Three-body problem
    - Non-linear pendulum
    - Double pendulum and chaotic motion (simulation + animation code ([ipynb](code/7_OrdinaryDifferentialEquations/DoublePendulumAnimate.ipynb)))


9. Molecular dynamics [Lecture ([pdf](lectures/Lecture12-02-28-23-MolecularDynamics.pdf)), Code ([ipynb](code/8_MolecularDynamics/8_MolecularDynamics.ipynb))]
    - Classical N-body problem
    - Lennard-Jones fluid
    - Equilibration and thermodynamics

10. Linear algebra [Code ([ipynb](code/8_MolecularDynamics/8_MolecularDynamics.ipynb))]
    - Lecture 1 ([pdf](lectures/Lecture13-03-02-23-LinearAlgebra.pdf))
        - Gaussian elimination
        - Pivoting
        - LU-decomposition
    - Lecture 2 ([pdf](lectures/Lecture14-03-07-23-LinearAlgebra-2.pdf))
        - Matrix inversion
        - Tri- and band-diagonal systems
        - QR decomposition
        - Eigenvalue problem

11. Partial differential equations (PDE) [Code ([ipynb](code/10_PartialDifferentialEquations/10_PDE.ipynb))]
    - Lecture 1 ([pdf](lectures/Lecture15-03-21-23-PartialDifferentialEquations.pdf))
        - Boundary value problems
        - Finite difference method
        - Jacobi and Gauss-Seidel methods
    - Lecture 2 ([pdf](lectures/Lecture16-03-23-23-PartialDifferentialEquations-2.pdf), [pptx](lectures/Lecture16-03-23-23-PartialDifferentialEquations-2.pptx))
        - Initial value problems
        - FTCS, implicit, and Crank-Nicolson schemes
        - Heat and wave equations

12. Random numbers and Monte Carlo methods  [Code ([ipynb](code/11_RandomNumbers/11_RandomNumbers.ipynb))]
    - Lecture 1 ([pdf](lectures/Lecture17-03-28-23-RandomNumbers.pdf))
        - Pseudo-random number generators
        - Computing integrals
            - As the area under the curve
            - Mean-value method
        - Sampling non-uniformly distributed random numbers
            - Inverse transform sampling
            - Rejection sampling
    - Lecture 2 ([pdf](lectures/Lecture18-03-30-23-RandomNumbers-2.pdf))
        - Multi-dimensional integrals
        - Importance sampling

13. Statistical physics problems
    - Lecture 1 ([pdf](lectures/Lecture19-04-04-23-StatisticalPhysics.pdf)), Code ([ipynb](code/12_StatisticalPhysics/12_StatisticalPhysics.ipynb))
        - Markov Chain Monte Carlo (MCMC)
        - Metropolis-Hastings algorithm
        - 2D Ising model
    - Lecture 2 ([pdf](lectures/Lecture20-04-06-23-StatisticalPhysics-2.pdf). [pptx](Lecture20-04-06-23-StatisticalPhysics-2.pptx)), Code ([ipynb](code/12_StatisticalPhysics/12_StatisticalPhysics-2.ipynb))
        - Simulated annealing
        - Percolation threshold simulation

14. Quantum mechanics [Lecture ([pdf](lectures/Lecture21-04-11-23-QuantumMechanics.pdf)), Code ([ipynb](code/13_QuantumMechanics/13_QuantumMechanics.ipynb))]
    - Matrix method for eigenenergies and eigenstates
    - Time-dependent Schroedinger equation

15. Fourier transform [Lecture ([pdf](lectures/Lecture22-04-18-23-Fourier.pdf)), Code ([ipynb](code/14_FFT/14_FFT.ipynb))]
    - Discrete Fourier Transform
    - Fast Fourier Transform

16. Introduction to Machine Learning [Lecture ([pdf](lectures/Lecture23-04-20-23-MLIntro.pdf))]
    - Based on Google machine learning crash course 
https://developers.google.com/machine-learning/crash-course


17. Introduction to Parallel Computing [Lecture ([pdf](lectures/Lecture24-04-25-23-ParallelComputingIntro.pdf))]
    - Basic terminology
    - OpenMP examples ([cpp](code/15_ParallelComputing))
    - Molecular dynamics with NVIDIA CUDA ([cpp](https://github.com/vlvovch/lennard-jones-cuda))

## Usage

Feel free to use and redistribute the material with an appropriate reference.

*Copyright (C) 2023 Volodymyr Vovchenko*