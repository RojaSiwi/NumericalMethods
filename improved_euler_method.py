import numpy as np

# Routine to Determine Derivative
def derivs(x, y, dydx):
    dydx[0] = x + y[0]

# Euler's Method for a Single ODE
def euler(x, y, h):
    dydx = np.zeros_like(y)
    derivs(x, y, dydx)
    ynew = y + dydx * h
    x = x + h
    return x, ynew

# Improved Euler's Method for a Single ODE
def improved_euler(x, y, h):
    dydx = np.zeros_like(y)
    derivs(x, y, dydx)
    y_temp = y + dydx * h/2.0
    dydx = np.zeros_like(y)
    derivs(x + h/2.0, y_temp, dydx)
    ynew = y + dydx * h
    x = x + h
    return x, ynew

# Routine to Take One Output Step
def integrator(x, y, h, xend, method=euler):
    x_values = [x]
    y_values = [y.copy()]

    while x < xend:
        if xend - x < h:
            h = xend - x
        x, y = method(x, y, h)
        x_values.append(x)
        y_values.append(y.copy())

    return x_values, y_values

# Main or "Driver" Program
def main():
    problems = [
        (np.array([0.0, 0.2, 0.4]), np.array([0.0, 0.74140, 1.3718])),
        (np.array([1.1, 1.2, 1.3, 1.4]), np.array([9.025013, 11.02318, 13.46374, 16.4465])),
        (np.array([2.1, 2.2, 2.3, 2.4, 2.5, 2.6]), np.array([-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.6015966]))
    ]

    for problem_num, (x, y) in enumerate(problems, start=1):
        xi = x[0]
        xf = x[-1]
        dx = x[1] - x[0]
        xout = 0.2 

        x_vals, y_vals = integrator(xi, y.copy(), dx, xf, method=improved_euler)

        print(f"Result for Problem {problem_num}:")
        for i in range(len(x_vals)):
            print(f"Step {i + 1} - x = {x_vals[i]}, y = {y_vals[i]}")

if __name__ == "__main__":
    main()
