# -*- coding: utf-8 -*-
#
import numpy
from sympy import sqrt, Rational as fr

from . import ewing
from . import hammer_stroud
from . import mustard_lyness_blatt
from . import phillips
from . import stroud1957
from . import stroud1966
from . import stroud1968
from . import thacher
from . import tyler

from ..helpers import fsd, pm


class Stroud(object):
    '''
    Arthur Stroud,
    Approximate Calculation of Multiple Integrals,
    Prentice Hall, 1971.
    '''
    # pylint: disable=too-many-locals
    def __init__(self, n, index):
        self.name = 'Stroud({})'.format(index)
        self.dim = n
        reference_volume = 2**n
        if index == 'Cn 1-1':
            # centroid formula
            self.degree = 1
            self.weights = numpy.array([reference_volume])
            self.points = numpy.full((1, n), 0)
        elif index == 'Cn 1-2':
            # product trapezoidal formula
            self.degree = 1
            self.weights = numpy.full(2**n, 1)
            self.points = pm(n, 1)
        elif index == 'Cn 2-1':
            self.set_data(stroud1957.Stroud1957(n, 2))
        elif index == 'Cn 2-2':
            self.set_data(thacher.Thacher(n))
        elif index == 'Cn 3-1':
            self.set_data(stroud1957.Stroud1957(n, 3))
        elif index == 'Cn 3-2':
            self.degree = 3
            self.weights = numpy.full(2*n, fr(reference_volume, 2*n))
            r = sqrt(fr(n, 3))
            self.points = fsd(n, (r, 1))
        elif index == 'Cn 3-3':
            self.set_data(tyler.Tyler(n))
        elif index == 'Cn 3-4':
            # product Gauss formula
            self.degree = 3
            self.weights = numpy.full(2**n, fr(reference_volume, 2**n))
            r = sqrt(3) / 3
            self.points = pm(n, r)
        elif index == 'Cn 3-5':
            self.set_data(ewing.Ewing(n))
        elif index == 'Cn 3-6':
            # product Simpson's formula
            self.degree = 3
            lst = n * [[fr(1, 3), fr(4, 3), fr(1, 3)]]
            self.weights = numpy.product(
                numpy.array(numpy.meshgrid(*lst)).T.reshape(-1, n),
                axis=-1
                )
            lst = n * [[-1, 0, +1]]
            self.points = numpy.array(numpy.meshgrid(*lst)).T.reshape(-1, n)
        # elif index == 'Cn 5-1':
        # Cn 5-1 is not implemented because it's based on explicit values only
        # given for n=4,5,6.
        elif index == 'Cn 5-2':
            self.set_data(hammer_stroud.HammerStroud(n, '2-n'))
        elif index == 'Cn 5-3':
            self.set_data(stroud1968.Stroud1968(n))
        elif index == 'Cn 5-4':
            self.set_data(stroud1966.Stroud1966(n, 'a'))
        elif index == 'Cn 5-5':
            self.set_data(mustard_lyness_blatt.MustardLynessBlatt(n))
        elif index == 'Cn 5-6':
            self.set_data(stroud1966.Stroud1966(n, 'b'))
        elif index == 'Cn 5-7':
            self.set_data(stroud1966.Stroud1966(n, 'c'))
        elif index == 'Cn 5-8':
            self.set_data(stroud1966.Stroud1966(n, 'd'))
        elif index == 'Cn 5-9':
            # product Gauss formula
            self.degree = 5
            lst = n * [[fr(5, 9), fr(8, 9), fr(5, 9)]]
            self.weights = numpy.product(
                numpy.array(numpy.meshgrid(*lst)).T.reshape(-1, n),
                axis=-1
                )
            sqrt35 = sqrt(fr(3, 5))
            lst = n * [[-sqrt35, 0, sqrt35]]
            self.points = numpy.array(numpy.meshgrid(*lst)).T.reshape(-1, n)
        else:
            assert index == 'Cn 7-1'
            self.set_data(phillips.Phillips(n))
        return

    def set_data(self, scheme):
        self.degree = scheme.degree
        self.weights = scheme.weights
        self.points = scheme.points
        return
