# -*- coding: utf-8 -*-
#
import numpy
from sympy import factorial, Rational as fr, sqrt

from ..helpers import untangle


class Walkington(object):
    '''
    Noel J. Walkington,
    Quadrature on simplices of arbitrary dimension,
    Technical Report,
    CMU, 2000,
    <http://www.math.cmu.edu/~nw0z/publications/00-CNA-023/023abs/>.
    '''
    def __init__(self, d, index):
        self.name = 'Walkington({})'.format(index)
        self.dim = d
        if index == 1:
            self.degree = 1
            data = [(fr(1, factorial(d)), _c(d))]
        elif index == 2:
            # The article claims order 2, but tests really only show order 1.
            # Also, the article says:
            #
            # > The points are inside the simplex when the positive square root
            # > is selected.
            #
            # Not sure what this means, but for d>=2, the points are outside
            # the simplex.
            self.degree = 1
            data = [
                (fr(1, factorial(d+1)), _xi1(d, 1/sqrt(d+1)))
                ]
        elif index == 3:
            self.degree = 3
            data = [
                (fr(-(d+1)**3, 4 * factorial(d+2)), _c(d)),
                (fr(+(d+3)**3, 4 * factorial(d+3)), _xi1(d, fr(1, (d+3)))),
                ]
        elif index == 5:
            self.degree = 5
            w0 = fr(+(d+1)**5, 32 * factorial(d+3))
            w1 = fr(-(d+3)**5, 16 * factorial(d+4))
            w2 = fr(+(d+5)**5, 16 * factorial(d+5))
            data = [
                (w0, _c(d)),
                (w1, _xi1(d, fr(1, d+3))),
                (w2, _xi1(d, fr(1, d+5))),
                (w2, _xi11(d, fr(1, d+5))),
                ]
        else:
            assert index == 7
            self.degree = 7
            w0 = -fr(1, 384) * fr((d+1)**7, factorial(d+4))
            w1 = +fr(1, 128) * fr((d+3)**7, factorial(d+5))
            w2 = -fr(1, 64) * fr((d+5)**7, factorial(d+6))
            w3 = +fr(1, 64) * fr((d+7)**7, factorial(d+7))
            data = [
                (w0, _c(d)),
                (w1, _xi1(d, fr(1, d+3))),
                (w2, _xi1(d, fr(1, d+5))),
                (w2, _xi11(d, fr(1, d+5))),
                (w3, _xi1(d, fr(1, d+7))),
                (w3, _xi21(d, fr(1, d+7))),
                (w3, _xi111(d, fr(1, d+7))),
                ]

        self.bary, self.weights = untangle(data)
        self.points = self.bary[:, 1:]
        # normalize weights
        self.weights /= numpy.sum(self.weights)
        return


def _c(d):
    return numpy.array([
        numpy.full(d+1, fr(1, d+1))
        ])


def _xi1(d, a):
    out = numpy.full((d+1, d+1), a)
    b = 1 - d*a
    numpy.fill_diagonal(out, b)
    return out


def _xi11(d, a):
    assert d > 1
    b = fr(1 - (d-1) * a, 2)
    if d == 2:
        out = numpy.array([
            [b, b, a],
            [b, a, b],
            [a, b, b],
            ])
    else:
        assert d == 3
        out = numpy.array([
            [b, b, a, a],
            [b, a, b, a],
            [b, a, a, b],
            [a, b, a, b],
            [a, a, b, b],
            [a, b, b, a],
            ])
    return out


def _xi21(d, a):
    assert d > 1
    b = fr(1 - (d-2) * a, 3)
    # ERR Note that the article wrongly states (d-2) the the expression for c.
    c = 1 - (d-1) * a - b
    if d == 2:
        out = numpy.array([
            [b, c, a],
            [c, b, a],
            [c, a, b],
            [b, a, c],
            [a, b, c],
            [a, c, b],
            ])
    else:
        assert d == 3
        out = numpy.array([
            [b, c, a, a],
            [b, a, c, a],
            [b, a, a, c],
            [a, b, a, c],
            [a, a, b, c],
            [a, b, c, a],
            [c, b, a, a],
            [c, a, b, a],
            [c, a, a, b],
            [a, c, a, b],
            [a, a, c, b],
            [a, c, b, a],
            ])

    return out


def _xi111(d, a):
    assert d == 3
    b = fr(1 - (d-2) * a, 3)
    out = numpy.array([
        [b, b, b, a],
        [b, b, a, b],
        [b, a, b, b],
        [a, b, b, b],
        ])
    return out
