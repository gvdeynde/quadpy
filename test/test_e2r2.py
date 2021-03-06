# -*- coding: utf-8 -*-
#
import pytest
import quadpy

from helpers import check_degree, integrate_monomial_over_enr2


@pytest.mark.parametrize(
    'scheme,tol',
    [(quadpy.e2r2.Stroud(index), 1.0e-14) for index in [
        '4-1',
        '5-1', '5-2',
        '7-1', '7-2',
        '9-1',
        '11-1', '11-2',
        '13-1',
        '15-1',
        ]]
    + [(quadpy.e2r2.StroudSecrest(k), 1.0e-14) for k in ['V', 'VI']]
    )
def test_scheme(scheme, tol):
    degree = check_degree(
            lambda poly: quadpy.e2r2.integrate(poly, scheme),
            integrate_monomial_over_enr2,
            2,
            scheme.degree + 1,
            tol=tol
            )
    assert degree == scheme.degree, \
        'Observed: {}   expected: {}'.format(degree, scheme.degree)
    return


@pytest.mark.parametrize(
    'scheme',
    [quadpy.e2r2.RabinowitzRichter(1)]
    )
def test_show(scheme):
    quadpy.e2r2.show(scheme)
    return


if __name__ == '__main__':
    scheme_ = quadpy.e2r2.Stroud('7-2')
    test_scheme(scheme_, 1.0e-14)
    test_show(scheme_)
