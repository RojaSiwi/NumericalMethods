import numpy as np

def Derivs(x, y, dydx):
    pass

# Heun's method without corrector
def Heun(x, y, h):
    dy1dx = np.zeros_like(y)
    Derivs(x, y, dy1dx)
    ye = y + dy1dx * h
    dy2dx = np.zeros_like(y)
    Derivs(x + h, ye, dy2dx)
    slope = (dy1dx + dy2dx) / 2
    ynew = y + slope * h
    x = x + h
    return x, ynew

# Midpoint method
def Midpoint(x, y, h):
    dydx = np.zeros_like(y)
    Derivs(x, y, dydx)
    ym = y + dydx * h / 2
    dymdx = np.zeros_like(y)
    Derivs(x + h / 2, ym, dymdx)
    ynew = y + dymdx * h
    x = x + h
    return x, ynew

# Heun's method with corrector
def HeunIter(x, y, h):
    es = 0.01
    maxit = 20
    dy1dx = np.zeros_like(y)
    Derivs(x, y, dy1dx)
    ye = y + dy1dx * h
    iter = 0
    while True:
        yeold = ye
        dy2dx = np.zeros_like(y)
        Derivs(x + h, ye, dy2dx)
        slope = (dy1dx + dy2dx) / 2
        ye = y + slope * h
        iter += 1
        ea = np.abs((ye - yeold) / ye).max() * 100
        if ea <= es or iter > maxit:
            break
    ynew = ye
    x = x + h
    return x, ynew

# Example usage with the provided data
# Choose the appropriate x, y, and h based on the problem
x1 = np.array([0.0, 0.2, 0.4])
y1 = np.array([0.00000, 0.74140, 1.3718])
h1 = 0.2

x2 = np.array([1.1, 1.2, 1.3, 1.4])
y2 = np.array([9.025013, 11.02318, 13.46374, 16.4465])
h2 = 0.1

x3 = np.array([2.1, 2.2, 2.3, 2.4, 2.5, 2.6])
y3 = np.array([-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.6015966])
h3 = 0.1

# Example usage for Heun's method without corrector
x1, ynew1 = Heun(x1, y1, h1)
print("Heun's method without corrector:", x1, ynew1)

# Example usage for Midpoint method
x2, ynew2 = Midpoint(x2, y2, h2)
print("Midpoint method:", x2, ynew2)

# Example usage for Heun's method with corrector
x3, ynew3 = HeunIter(x3, y3, h3)
print("Heun's method with corrector:", x3, ynew3)
