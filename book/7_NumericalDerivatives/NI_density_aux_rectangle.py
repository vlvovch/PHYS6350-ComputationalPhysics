import numpy as np

# Numerical integration using the rectangle rule

rectangle_rule_verbose = False

# Rectangle rule for numerical integration 
# of function f(x) over (a,b) using n subintervals
def rectangle_rule(f, a, b, n):
    h = (b - a) / n
    ret = 0.0
    xk = a + h / 2.
    for k in range(n):
        ret += f(xk) * h
        xk += h
    return ret


# Rectangle rule for numerical integration with adaptive step
def rectangle_rule_adaptive(f, a, b, nst = 1, tol = 1.e-8, max_iterations = 16):
    Iprev = 0.
    n = nst
    Iprev = rectangle_rule(f, a, b, n)
    if rectangle_rule_verbose: 
        print("Iteration: {0:5}, I = {1:20.15f}".format(1, Iprev))
    for k in range(1, max_iterations):
        n *= 2
        Inew = rectangle_rule(f, a, b, n)
        ek = (Inew - Iprev) / 3.
        if rectangle_rule_verbose: 
            print("Iteration: {0:5}, I = {1:20.15f}, error estimate = {2:10.15f}".format(k+1, Inew, ek))
        if (abs(ek) < tol):
            return Inew
        Iprev = Inew
        
    print("Failed to achieve the desired accuracy after", max_iterations,"iterations")
    return Inew

# Numerical integration of the density of a gas in thermal equilibrium

T = 150
mu = 0
m = 138
d = 1
eta = 0

def fThermal(x):
    return d * x**2 / (2 * np.pi**2) / (np.exp(np.sqrt((m/T)**2 + x**2) - mu/T) + eta)

def g(t, f, a = 0.):
    return f(a + t / (1. - t)) / (1. - t)**2

def nIntegral(eps = 1e-6):
    def fInt(t):
        return g(t, fThermal, 0)
    return rectangle_rule_adaptive(fInt, 0., 1., 1, eps, 20)

def nIntegralNrect(Nrect = 100):
    def fInt(t):
        return g(t, fThermal, 0)
    return rectangle_rule(fInt, 0., 1., Nrect)

def nT3num(inT, inMu, eps):
    global T, mu
    T = inT
    mu = inMu
    return nIntegral(eps)

def nT3numNrect(inT, inMu, Nrect):
    global T, mu
    T = inT
    mu = inMu
    return nIntegralNrect(Nrect)

from scipy.special import kn

# Analytic expression for the density in the Maxwell-Boltzmann limit
def nT3analyt(T, mu, m, d = 1):
    return d * m**2 / (2 * np.pi**2 * T**2) * kn(2,m/T) * np.exp(mu/T)