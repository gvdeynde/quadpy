# -*- coding: utf-8 -*-
#
from math import pi
import numpy

from .. import helpers


def show(
        scheme,
        backend='mpl'
        ):
    '''Displays scheme for 3D ball quadrature.
    '''
    helpers.backend_to_function[backend](
            scheme.points,
            scheme.weights,
            volume=4.0/3.0*pi,
            edges=[],
            balls=[((0.0, 0.0, 0.0), 1.0)],
            )
    return


def integrate(f, center, radius, rule, sumfun=helpers.kahan_sum):
    flt = numpy.vectorize(float)

    center = numpy.array(center)
    rr = numpy.multiply.outer(radius, flt(rule.points))
    rr = numpy.swapaxes(rr, 0, -2)
    ff = numpy.array(f((rr + center).T))
    out = sumfun(flt(rule.weights) * ff, axis=-1)

    return numpy.array(radius)**3 * out
