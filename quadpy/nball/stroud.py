# -*- coding: utf-8 -*-
#
from sympy import sqrt, Rational as fr

from . import hammer_stroud
from . import stenger
from . import stroud1957
from . import stroud1966
from . import stroud1967a
from . import stroud1967b

from .helpers import volume_unit_ball
from ..helpers import pm, untangle


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
        if index == 'Sn 2-1':
            self.set_data(stroud1957.Stroud1957(n))
        elif index == 'Sn 3-1':
            self.set_data(hammer_stroud.HammerStroud(n, '11-n', alpha=0.0))
        elif index == 'Sn 3-2':
            self.degree = 3
            r = sqrt(fr(1, n+2))
            data = [
                (fr(1, 2**n), pm(n, r))
                ]
            self.points, self.weights = untangle(data)
            self.weights *= volume_unit_ball(n)
        elif index == 'Sn 5-1a':
            self.set_data(stroud1967a.Stroud1967a(n, variant='a'))
        elif index == 'Sn 5-1b':
            self.set_data(stroud1967a.Stroud1967a(n, variant='b'))
        elif index == 'Sn 5-2':
            self.set_data(hammer_stroud.HammerStroud(n, '12-n', alpha=0.0))
        elif index == 'Sn 5-3':
            self.set_data(stroud1966.Stroud1966(n, variant='a'))
        elif index == 'Sn 5-4':
            self.set_data(stroud1966.Stroud1966(n, variant='b'))
        elif index == 'Sn 5-5':
            self.set_data(stroud1966.Stroud1966(n, variant='c'))
        elif index == 'Sn 5-6':
            self.set_data(stroud1966.Stroud1966(n, variant='d'))
        elif index == 'Sn 7-1a':
            self.set_data(stroud1967b.Stroud1967b(n, variant='a'))
        elif index == 'Sn 7-1b':
            self.set_data(stroud1967b.Stroud1967b(n, variant='b'))
        elif index == 'Sn 7-2':
            self.set_data(stroud1967b.Stroud1967b(n, variant='c'))
        elif index == 'Sn 7-3a':
            self.set_data(stenger.Stenger(n, degree=7, variant='a'))
        elif index == 'Sn 7-3b':
            self.set_data(stenger.Stenger(n, degree=7, variant='b'))
        elif index == 'Sn 9-1a':
            self.set_data(stenger.Stenger(n, degree=9, variant='a'))
        elif index == 'Sn 9-1b':
            self.set_data(stenger.Stenger(n, degree=9, variant='b'))
        elif index == 'Sn 11-1a':
            self.set_data(stenger.Stenger(n, degree=11, variant='a'))
        else:
            assert index == 'Sn 11-1b'
            self.set_data(stenger.Stenger(n, degree=11, variant='b'))
        return

    def set_data(self, scheme):
        self.degree = scheme.degree
        self.weights = scheme.weights
        self.points = scheme.points
        return
