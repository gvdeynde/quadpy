# -*- coding: utf-8 -*-
#
from __future__ import division

import warnings

import numpy
from sympy import sqrt, pi, sin, cos, Rational as fr

from .rabinowitz_richter import RabinowitzRichter
from .stroud_secrest import StroudSecrest

from ..helpers import untangle, fsd, pm


class Stroud(object):
    '''
    Arthur Stroud,
    Approximate Calculation of Multiple Integrals,
    Prentice Hall, 1971.
    '''
    def __init__(self, index):
        self.name = 'Stroud_E2r2({})'.format(index)
        if index == '4-1':
            self.degree = 4

            pts = sqrt(2) * numpy.array([
                [cos(2*i*numpy.pi / 5) for i in range(5)],
                [sin(2*i*numpy.pi / 5) for i in range(5)],
                ]).T
            data = [
                (fr(1, 2), numpy.array([[0, 0]])),
                (fr(1, 10), pts),
                ]

            self.points, self.weights = untangle(data)
            self.weights *= pi
        elif index == '5-1':
            self.set_data(StroudSecrest('V'))
        elif index == '5-2':
            # Cartesian product Gauss formula
            self.degree = 5

            r = sqrt(fr(3, 2))
            data = [
                (fr(4, 9), numpy.array([[0, 0]])),
                (fr(1, 9), fsd(2, (r, 1))),
                (fr(1, 36), pm(2, r)),
                ]

            self.points, self.weights = untangle(data)
            self.weights *= pi
        elif index == '7-1':
            self.set_data(StroudSecrest('VI'))
        elif index == '7-2':
            # Cartesian product Gauss formula
            warnings.warn(
                'Stroud\'s Gauss product formula has degree 1, not 7.'
                )
            self.degree = 1

            sqrt6 = sqrt(6)
            r, s = [sqrt((3 + p_m * sqrt6) / 2) for p_m in [+1, -1]]
            A, B = [(5 - p_m * 2 * sqrt6) / 48 for p_m in [+1, -1]]
            C = fr(1, 48)

            data = [
                (A, fsd(2, (r, 1))),
                (B, fsd(2, (s, 1))),
                (C, fsd(2, (r, 1), (s, 1))),
                ]

            self.points, self.weights = untangle(data)
            self.weights *= pi
        elif index == '9-1':
            self.set_data(RabinowitzRichter(1))
        elif index == '11-1':
            self.set_data(RabinowitzRichter(2))
        elif index == '11-2':
            self.set_data(RabinowitzRichter(3))
        elif index == '13-1':
            self.set_data(RabinowitzRichter(4))
        else:
            assert index == '15-1'
            self.set_data(RabinowitzRichter(5))
        return

    def set_data(self, scheme):
        self.degree = scheme.degree
        self.weights = scheme.weights
        self.points = scheme.points
        return
