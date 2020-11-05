import numpy

from fteikpy import EikonalSolver2D, EikonalSolver3D

numpy.random.seed(42)


eik2d = EikonalSolver2D(
    grid=numpy.ones((16, 16), dtype=numpy.float64),
    gridsize=(1.0, 1.0),
)


eik3d = EikonalSolver3D(
    grid=numpy.ones((16, 16, 16), dtype=numpy.float64),
    gridsize=(1.0, 1.0, 1.0),
)


def allclose(a, b, bfun, atol=1.0e-8):

    def allclose_nan(a, b):
        try:
            if numpy.isnan(a):
                assert numpy.isnan(b)

            else:
                assert numpy.allclose(a, b, atol=atol)

        except AssertionError:
            raise AssertionError(f"{a} != {b}")

    ndim = numpy.ndim(a)

    if ndim == 0:
        allclose_nan(a, bfun(b))

    elif ndim == 1:
        for aa, bb in zip(a, b):
            allclose_nan(aa, bfun(bb))

    else:
        raise ValueError()


def tana(x, y, v=1.0):
    return numpy.linalg.norm(x - y) / v
