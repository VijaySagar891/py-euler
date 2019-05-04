import numpy as np
# 11 terms in polynomial


# Steps:
# Solve equation a00 = p0(1), a11 = p1(1) a12 = p1(2), a21 = p2(1), a22 = p2(2) a23 = p2(3)


def evaluate(poly, i):
    print "Polyval %s at %s" % (poly, i)
    return np.polyval(poly, i)


def find_approx_poly(poly, degree):
    a = []
    b = []
    for i in range(1, degree + 1):
        b.append(evaluate(poly, i))
        coeffs = []
        for c in range(0, degree):
            coeffs.append(i ** c)
        a.append(coeffs)
    print "Solving equation for a = %s and b = %s" % (a, b) 
    return np.linalg.solve(a, b)[::-1]


def compute_fit_sums(polynomial):
    sum = 0
    poly_degree = len(polynomial) 

    for degree in range(1, poly_degree):
        print "Calculating fit for degree %s" % degree
        approx_poly = find_approx_poly(polynomial, degree)
        print "Approx poly: %s" % approx_poly
        fit = evaluate(approx_poly, degree + 1)
        print "Fit: %s" % fit
        sum += fit
    return sum


print compute_fit_sums([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
