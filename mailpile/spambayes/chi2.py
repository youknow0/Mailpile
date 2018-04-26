import math as _math
import random

def chi2Q(x2, v, exp=_math.exp, min=min):
    """Return prob(chisq >= x2, with v degrees of freedom).

    v must be even.
    """
    assert v & 1 == 0
    # XXX If x2 is very large, exp(-m) will underflow to 0.
    m = x2 / 2.0
    sum = term = exp(-m)
    for i in range(1, v//2):
        term *= m / i
        sum += term
    # With small x2 and large v, accumulated roundoff error, plus error in
    # the platform exp(), can cause this to spill a few ULP above 1.0.  For
    # example, chi2Q(100, 300) on my box has sum == 1.0 + 2.0**-52 at this
    # point.  Returning a value even a teensy bit over 1.0 is no good.
    return min(sum, 1.0)
