import numpy as np

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

# Numerical integration of the density of a gas in thermal equilibrium
T = 150
mu = 0
m = 138
d = 1
eta = 0

from IntegrateGauss import *
# Precomute 32-point Gauss-Laguerre quadrature
laguerrexw32 = laguerrexw(32)

# Function for integration
def fThermal(x):
    x = float(x)
    return d * x**2 * np.exp(x) / (2 * np.pi**2) / (np.exp(np.sqrt((m/T)**2 + x**2) - mu/T) + eta)

def nIntegral(eps = 1e-6):
    def fInt(t):
        return g(t, fThermal, 0)
    return rectangle_rule_adaptive(fInt, 0., 1., 1, eps, 20)

def nIntegral(n_nodes = 32):
    quad = laguerrexw32
    if (n_nodes != 32):
        quad = laguerrexw(n_nodes)
    return integrate_quadrature(fThermal, quad)

def nT3num(inT, inMu, n_nodes = 32):
    global T, mu
    T = inT
    mu = inMu
    return nIntegral(n_nodes)

from scipy.special import kn

# Analytic expression for the density in the Maxwell-Boltzmann limit
def nT3analyt(T, mu, m, d = 1):
    return d * m**2 / (2 * np.pi**2 * T**2) * kn(2,m/T) * np.exp(mu/T)