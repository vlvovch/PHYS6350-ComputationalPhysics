# Generic integration using quadratures
def integrate_quadrature(
    f,   # Function to be integrated 
    quad # A pair of lists (x,w) where x are the integration nodes and w are the weights 
                        ):
    ret = 0.
    n = len(quad[0])
    for k in range(n):
        xk = quad[0][k]
        wk = quad[1][k]
        ret += wk * f(xk)
    return ret

######################################################################
#
# Functions to calculate integration points and weights for Gaussian
# quadrature
#
# x,w = gaussxw(N) returns integration points x and integration
#           weights w such that sum_i w[i]*f(x[i]) is the Nth-order
#           Gaussian approximation to the integral int_{-1}^1 f(x) dx
# x,w = gaussxwab(N,a,b) returns integration points and weights
#           mapped to the interval [a,b], so that sum_i w[i]*f(x[i])
#           is the Nth-order Gaussian approximation to the integral
#           int_a^b f(x) dx
#
# This code finds the zeros of the nth Legendre polynomial using
# Newton's method, starting from the approximation given in Abramowitz
# and Stegun 22.16.6.  The Legendre polynomial itself is evaluated
# using the recurrence relation given in Abramowitz and Stegun
# 22.7.10.  The function has been checked against other sources for
# values of N up to 1000.  It is compatible with version 2 and version
# 3 of Python.
#
# Written by Mark Newman <mejn@umich.edu>, June 4, 2011
# You may use, share, or modify this file freely
#
######################################################################

from numpy import ones,copy,cos,tan,pi,linspace

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

def gaussxwab(gaussxwin,a,b):
    x,w = gaussxwin
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

# gaussxw32 = gaussxw(32)

# def gaussxwab32(a,b):
#     x,w = gaussxw32
#     return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

import sympy as sympy
import math

# Nodes and weight for n-point Gauss-Hermite quadrature
def hermitexw(n):
    x = sympy.Symbol("x")
    roots = sympy.Poly(sympy.hermite(n, x)).all_roots()
    x_i = [float(rt.evalf(20)) for rt in roots]
    w_i = [float(2**(n-1) * math.factorial(n) * np.sqrt(np.pi) / ((n**2) * sympy.hermite(n - 1, rt)**2).evalf(20)) for rt in roots]
    return x_i, w_i


# Nodes and weight for n-point Gauss-Laguerre quadrature
def laguerrexw(n):
  x = sympy.Symbol("x")
  roots = sympy.Poly(sympy.laguerre(n, x)).all_roots()
  x_i = [float(rt.evalf(20)) for rt in roots]
  w_i = [float((rt / ((n + 1) * sympy.laguerre(n + 1, rt)) ** 2).evalf(20)) for rt in roots]
  return x_i, w_i
