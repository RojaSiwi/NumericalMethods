import math

# Constants
g = 9.8  # gravitational constant (m/s^2)
m = 68.1  # mass of parachutist (kg)
c = 12.5  # drag coefficient (kg/s)

# Velocity function
def v(t):
    return (g * m / c) * (1 - math.exp(-(c / m) * t))

# Trapezoidal rule
def trap(h, f0, f1):
    return h * (f0 + f1) / 2

# Multiple-segment trapezoidal rule
def trapm(h, n, f):
    sum_result = f[0]
    for i in range(1, n - 1):
        sum_result += 2 * f[i]
    sum_result += f[n - 1]
    return h * sum_result / 2

# Single-application Simpson's 1/3 rule
def simp13(h, f0, f1, f2):
    return 2 * h * (f0 + 4 * f1 + f2) / 6

# Single-application Simpson's 3/8 rule
def simp38(h, f0, f1, f2, f3):
    return 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8

# Multiple-application Simpson's 1/3 rule
def simp13m(h, n, f):
    sum_result = f[0]
    for i in range(1, n - 2, 2):
        sum_result += 4 * f[i] + 2 * f[i + 1]
    sum_result += 4 * f[n - 1 - 1] + f[n - 1]
    return h * sum_result / 3

# Multiple-application Simpson's rule for both odd and even number of segments
def simpint(a, b, n, f):
    h = (b - a) / n
    sum_result = 0
    if n == 1:
        sum_result = trap(h, f[n - 2], f[n - 1])
    else:
        m = n
        odd = n % 2
        if odd > 0 and n > 1:
            sum_result = sum_result + simp38(h, f[n - 3], f[n - 2], f[n - 1], f[n])
            m = n - 3
        if m > 1:
            sum_result = sum_result + simp13m(h, m, f)
    return sum_result

# Trapezoidal rule for unequally spaced data
def trapun(x, y, n):
    sum_result = 0
    for i in range(n - 1):
        sum_result += (x[i + 1] - x[i]) * (y[i] + y[i + 1]) / 2
    return sum_result

# Combination of Simpson's and trapezoidal rules for unequally spaced data
def uneven(n, x, f):
    h = x[1] - x[0]
    k = 1
    sum_result = 0
    for j in range(n - 1):
        hf = x[j + 1] - x[j]
        if abs(h - hf) < 0.000001:
            if k == 3:
                sum_result += simp13(h, f[j - 2], f[j - 1], f[j])
                k = k - 1
            else:
                k = k + 1
        else:
            if k == 1:
                sum_result += trap(h, f[j], f[j + 1])
            else:
                if k == 2:
                    sum_result += simp13(h, f[j - 1], f[j], f[j + 1])
                else:
                    sum_result += simp38(h, f[j - 2], f[j - 1], f[j], f[j + 1])
                k = 1
        h = hf
    return sum_result

# Analytical solution for comparison
def analytical_solution():
    return 289.43515

# Time values for testing
time_values = [i for i in range(0, 21)]

# Velocity values
velocity_values = [v(t) for t in time_values]

# Integration using trapezoidal rule with different numbers of segments
segments_list = [1, 2, 4, 8, 16]

print("Trapezoidal Rule:")
for segments in segments_list:
    h = (time_values[-1] - time_values[0]) / segments
    integral_result = trapm(h, segments, velocity_values)
    print(f"Segments: {segments}, Result: {integral_result}")

# Integration using Simpson's rule with different numbers of segments
print("\nSimpson's Rule:")
for segments in segments_list:
    integral_result = simpint(time_values[0], time_values[-1], segments, velocity_values)
    print(f"Segments: {segments}, Result: {integral_result}")

# Integration for unequally spaced data using trapezoidal rule
x_values_uneven = [i for i in range(0, 21, 2)]
y_values_uneven = [v(t) for t in x_values_uneven]

integral_result_uneven_trapezoidal = trapun(x_values_uneven, y_values_uneven, len(x_values_uneven) - 1)
print(f"\nTrapezoidal Rule for Unequally Spaced Data: {integral_result_uneven_trapezoidal}")

# Integration for unequally spaced data using a combination of Simpson's and trapezoidal rules
integral_result_uneven_combined = uneven(len(x_values_uneven), x_values_uneven, y_values_uneven)
print(f"Combined Rule for Unequally Spaced Data: {integral_result_uneven_combined}")

# Analytical solution for comparison
analytical_result = analytical_solution()
print(f"\nAnalytical Solution: {analytical_result}")
