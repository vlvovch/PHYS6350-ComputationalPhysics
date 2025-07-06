[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vlvovch/PHYS6350-ComputationalPhysics/nusteam)

# PHYS6350 Computational Physics (NuSTEAM edition)

This repository contains the lecture notes and computer code for the Computational Physics week at the [NuSTEAM program](http://nsmn1.uh.edu/cratti/NuSTEAM.html) at UH.

This a 3-day compressed version of the full course PHYS6350 Computational Physics taught at the University of Houston covering selected topics.
For full course see the main branch of the repository or the online textbook available at [https://vovchenko.net/computational-physics/](https://vovchenko.net/computational-physics/).

## Lecture notes and code

- Lecture slides: folder [``slides``](slides/)
- Sample programs and notebooks: folder  [``code``](code/)
<!-- - Jupyter Book: folder [``book``](book/) -->

## Course outline

0. Installing and using Thermal-FIST [Lecture ([pdf](slides/NuSTEAM-2025-FIST.pdf))]

1. Plotting [Lecture ([pdf](slides/NuSTEAM-2025-CompPhys-Lecture1.pdf)), 
Code ([ipynb](code/1_Plotting-NuSTEAM2025.ipynb))]

2. Floating-Point Precision [Lecture ([pdf](slides/NuSTEAM-2025-CompPhys-Lecture1.pdf)), 
Code ([ipynb](code/1_FloatingPointPrecision-NuSTEAM2025.ipynb))]

3. Numerical integration [Lecture ([pdf](slides/NuSTEAM-2025-CompPhys-Lecture2.pdf)), 
Code ([ipynb](code/2_NumericalIIntegration_NuSTEAM2025.ipynb))]

4. Numerical differentiation [Lecture ([pdf](slides/NuSTEAM-2025-CompPhys-Lecture2.pdf)), 
Code ([ipynb](code/2_NumericalDerivatives-NuSTEAM2025.ipynb))]

5. Non-linear equations [Lecture ([pdf](slides/NuSTEAM-2025-CompPhys-Lecture3.pdf)), 
Code ([ipynb](code/3_NonlinearEquations_NuSTEAM.ipynb))]

6. Random numbers and Monte Carlo methods [Code ([ipynb](code/3_RandomNumbers-NuSTEAM.ipynb))]

## Solved versions

For instructors, solved versions of the notebooks are available:
- [Floating point precision - solved](code/1_FloatingPointPrecision-NuSTEAM2025-solved.ipynb)
- [Numerical derivatives - solved](code/2_NumericalDerivatives-NuSTEAM2025-solved.ipynb)
- [Numerical integration - solved](code/2_NumericalIIntegration_NuSTEAM2025-solved.ipynb)
- [Non-linear equations - solved](code/3_NonlinearEquations_NuSTEAM-solved.ipynb)

## Environment setup

To run the notebooks, you may wish to create a conda environment using the provided environment file:

```bash
conda env create -f environment.yml
conda activate CompPhys
```

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
