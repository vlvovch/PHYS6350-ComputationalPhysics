# Broyden's Method: An In-Depth Explanation

Broyden's method is a powerful quasi-Newton technique for solving systems of nonlinear equations in multiple dimensions. It's particularly valuable because it approximates the Jacobian matrix without requiring explicit derivative calculations at each iteration.

## Relationship to the Secant Method

As shown in the slide, Broyden's method is a multi-dimensional generalization of the secant method. Let's compare them:

### Secant Method (1D):
The secant method for a single variable function approximates the derivative using:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

where the derivative is approximated by:
$$f'(x_n) \approx \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$$

### Broyden's Method (Multi-dimensional):
Broyden's method extends this concept to vector functions:
$$\mathbf{x}_{n+1} = \mathbf{x}_n - J^{-1}(\mathbf{x}_n)\mathbf{f}(\mathbf{x}_n)$$

where the Jacobian approximation satisfies:
$$J(\mathbf{x}_n)(\mathbf{x}_n - \mathbf{x}_{n-1}) \approx \mathbf{f}(\mathbf{x}_n) - \mathbf{f}(\mathbf{x}_{n-1})$$

## The Jacobian Approximation

The key insight of Broyden's method is how it updates the Jacobian approximation. Rather than recalculating the entire Jacobian matrix at each step (which would be computationally expensive), Broyden's method uses a rank-one update:

$$J_n = J_{n-1} + \frac{\Delta \mathbf{f}_n - J_{n-1}\Delta \mathbf{x}_n}{\|\Delta \mathbf{x}_n\|^2}\Delta \mathbf{x}_n^T$$

Where:
- $\Delta \mathbf{x}_n = \mathbf{x}_n - \mathbf{x}_{n-1}$ (the step in x)
- $\Delta \mathbf{f}_n = \mathbf{f}_n - \mathbf{f}_{n-1}$ (the change in function values)
- $J_n$ is the approximation of the Jacobian at step n

This update formula ensures that the new Jacobian approximation $J_n$ satisfies the secant equation:
$$J_n \Delta \mathbf{x}_n = \Delta \mathbf{f}_n$$

## Initial Jacobian

For the initial Jacobian $J_0$, there are two common approaches:

1. **Calculate the exact Jacobian** at the initial point $J(\mathbf{x}_0)$ - This requires derivatives but provides more accurate initial steps and potentially faster convergence.

2. **Initialize with the identity matrix** $J(\mathbf{x}_0) = I$ - This requires no derivative calculations but may converge more slowly.

## Algorithm Steps

1. Choose an initial guess $\mathbf{x}_0$ and initialize the Jacobian $J_0$ (either by calculation or using the identity matrix)
2. For each iteration until convergence:
   - Compute $\mathbf{f}(\mathbf{x}_n)$
   - Solve the linear system $J_n \mathbf{s}_n = -\mathbf{f}(\mathbf{x}_n)$ for the step $\mathbf{s}_n$
   - Update $\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{s}_n$
   - Compute $\Delta \mathbf{x}_n = \mathbf{x}_{n+1} - \mathbf{x}_n$ and $\Delta \mathbf{f}_n = \mathbf{f}(\mathbf{x}_{n+1}) - \mathbf{f}(\mathbf{x}_n)$
   - Update the Jacobian using the Broyden formula
   - Check for convergence

## Advantages and Limitations

### Advantages:
- Requires only one Jacobian evaluation (or none if using identity matrix initialization)
- Converges superlinearly under appropriate conditions
- Significantly reduces computational cost compared to Newton's method for large systems

### Limitations:
- The solution for $J(\mathbf{x}_n)$ is not unique
- Convergence is typically slower than Newton's method
- May fail to converge for poorly conditioned problems

## Implementation Considerations

When implementing Broyden's method:
- Avoid explicitly computing $J^{-1}$ - instead solve the linear system $J_n \mathbf{s}_n = -\mathbf{f}(\mathbf{x}_n)$
- Store and update the Jacobian efficiently, especially for large systems
- Consider using a line search or trust region approach to improve robustness
- Implement appropriate stopping criteria based on function value, step size, or both

Broyden's method is particularly valuable when derivative calculations are expensive or unavailable, making it an important tool in numerical optimization and nonlinear equation solving.
