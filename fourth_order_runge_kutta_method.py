import numpy as np

def main_program(n, yi, xi, xf, dx, xout, x_data, y_data):
    x = xi
    m = 0
    xpm = x

    for i in range(n):
        yi[i] = yi[i]

    while True:
        xend = x + xout
        if xend > xf:
            xend = xf
        h = dx
        integrator(x, yi, n, h, xend)
        m = m + 1
        xpm = x
        print(f"At x = {x}: {yi}") 
        for i in range(n):
            ypi_m = yi[i]

        if x >= xf:
            break
        x = x + xout

    print(f"At x = {x}: {yi}")  

def integrator(x, y, n, h, xend):
    while True:
        if xend - x < h:
            h = xend - x
        x = rk4(x, y, n, h)  
        if x >= xend:
            break

def rk4(x, y, n, h):
    k1 = derivs(x, y)
    ym = [0] * (n + 1)

    for i in range(n):
        ym[i] = y[i] + k1[i] * h / 2

    k2 = derivs(x + h / 2, ym)

    for i in range(n):
        ym[i] = y[i] + k2[i] * h / 2

    k3 = derivs(x + h / 2, ym)

    for i in range(n):
        ym[i] = y[i] + k3[i] * h

    k4 = derivs(x + h, ym)

    for i in range(n):
        slope_i = (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) / 6
        y[i] = y[i] + slope_i * h

    x_new = x + h  
    return x_new

def derivs(x, y):
    dy = [0] * len(y)

    coefficients = np.polyfit(x_data, y_data, deg=len(y) - 1)
    for i in range(1, len(dy)):
        dy[i] = np.polyval(np.polyder(coefficients, m=i), x)

    return dy

# Problem 1.1
n = 1
yi = [0]
xi = 0
xf = 0.4
dx = 0.1
xout = 0.2
x_data = np.array([0.0, 0.2, 0.4])
y_data = np.array([0.00000, 0.74140, 1.3718])

main_program(n, yi, xi, xf, dx, xout, x_data, y_data)

# Problem 1.2
n = 1
yi = [0]
xi = 1.1
xf = 1.4
dx = 0.1
xout = 0.2
x_data = np.array([1.1, 1.2, 1.3, 1.4])
y_data = np.array([9.025013, 11.02318, 13.46374, 16.4465])

main_program(n, yi, xi, xf, dx, xout, x_data, y_data)

# Problem 1.3
n = 1
yi = [0]
xi = 2.1
xf = 2.6
dx = 0.1
xout = 0.2
x_data = np.array([2.1, 2.2, 2.3, 2.4, 2.5, 2.6])
y_data = np.array([-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.6015966])

main_program(n, yi, xi, xf, dx, xout, x_data, y_data)
