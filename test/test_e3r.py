# -*- coding: utf-8 -*-
#
import pytest
import quadpy

from helpers import check_degree, integrate_monomial_over_enr


@pytest.mark.parametrize(
    'scheme,tol',
    [(quadpy.e3r.Stroud(key), 1.0e-14) for key in quadpy.e3r.Stroud.keys]
    )
def test_scheme(scheme, tol):
    degree = check_degree(
            lambda poly: quadpy.e3r.integrate(poly, scheme),
            integrate_monomial_over_enr,
            3,
            scheme.degree + 1,
            tol=tol
            )
    assert degree == scheme.degree, \
        'Observed: {}   expected: {}'.format(degree, scheme.degree)
    return


@pytest.mark.parametrize(
    'scheme',
    [quadpy.e3r.StroudSecrest('X')]
    )
def test_show(scheme, backend='mpl'):
    quadpy.e3r.show(scheme, backend=backend)
    return


if __name__ == '__main__':
    scheme_ = quadpy.e3r.Stroud('5-1')
    test_scheme(scheme_, 1.0e-14)
    test_show(scheme_, backend='vtk')
