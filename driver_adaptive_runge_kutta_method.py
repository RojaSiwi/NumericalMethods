import numpy as np
from scipy.interpolate import CubicSpline

def interpolate_derivatives(x, y):
    cs = CubicSpline(x, y)
    return cs.derivative()

# Derivative function
def Derivs(x, y, dy):
    dy[0] = interpolator(x)  

# Runge-Kutta method with adaptive step size
def RKkc(y, dy, x, h, ytemp, yerr):
    k1 = h * dy[0]
    k2 = h * (dy[0] + k1/2)
    k3 = h * (dy[0] + k2/2)
    k4 = h * (dy[0] + k3)
    ytemp[0] = y[0] + (k1 + 2*k2 + 2*k3 + k4)/6
    yerr[0] = np.abs((k1 - k4)/6)

# Adaptive Step Routine
def Adapt(x, y, dy, htry, yscal, eps):
    safety = 0.9
    econ = 1.89e-4
    h = htry

    ytemp = np.zeros_like(y)
    yerr = np.zeros_like(y)

    max_iter = 100
    iter_count = 0

    while iter_count < max_iter:
        RKkc(y, dy, x, h, ytemp, yerr)
        emax = np.max(np.abs(yerr / yscal / eps))

        if emax <= 1:
            break

        htemp = safety * h * emax**(-0.25)
        h = max(abs(htemp), 0.1 * abs(h))
        xnew = x + h

        if xnew == x:
            print("Error: Step size became too small.")
            break

        iter_count += 1

    if iter_count == max_iter:
        print("Error: Maximum number of iterations reached in adaptive step routine.")

    if emax > econ:
        hnxt = safety * h * emax**(-0.2)
    else:
        hnxt = 4.0 * h

    x += h
    y[0] = ytemp[0]

    return hnxt

# Driver Program
def driver(xi, xf, yi):
    maxstep = 100
    hi = 0.1
    tiny = 1.0e-30
    eps = 0.00005

    print(xi, yi)
    x = xi
    y = np.array([yi])
    h = hi
    istep = 0
    dy = np.zeros_like(y)

    while x < xf:
        if istep >= maxstep:
            print("Error: Maximum number of steps reached.")
            break

        istep += 1
        Derivs(x, y, dy)
        yscal = np.abs(y) + np.abs(h * dy) + tiny

        hnxt = Adapt(x, y, dy, htry=h, yscal=yscal, eps=eps)
        print(x, y[0])

        h = hnxt

# Example usage
# 1.1
x_data = np.array([0.0, 0.2, 0.4])
y_data = np.array([0.00000, 0.74140, 1.3718])

xi = x_data[0]
xf = x_data[-1]
yi = y_data[0]

# Interpolate derivatives at data points
interpolator = interpolate_derivatives(x_data, y_data)

# Run the driver with the given data
driver(xi, xf, yi)

# 1.2
x_data = np.array([1.1, 1.2, 1.3, 1.4])
y_data = np.array([9.025013, 11.02318, 13.46374, 16.4465])

xi = x_data[0]
xf = x_data[-1]
yi = y_data[0]

# Interpolate derivatives at data points
interpolator = interpolate_derivatives(x_data, y_data)

# Run the driver with the given data
driver(xi, xf, yi)

# 1.3
x_data = np.array([2.1, 2.2, 2.3, 2.4, 2.5, 2.6])
y_data = np.array([-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.6015966])

xi = x_data[0]
xf = x_data[-1]
yi = y_data[0]

# Interpolate derivatives at data points
interpolator = interpolate_derivatives(x_data, y_data)

# Run the driver with the given data
driver(xi, xf, yi)
