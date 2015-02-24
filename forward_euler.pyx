import cython
import numpy as np
cimport numpy as np

cdef extern from "c_forward_euler.hpp":
    ctypedef double (*Callback)(void *feval, const double &y, const double &t)

    void forward_euler(Callback callback, void *feval, double *y, double *t, int nt)


@cython.boundscheck(False)
@cython.wraparound(False)
def solve(f,np.ndarray[double,ndim=1,mode="c"] y not None,
            np.ndarray[double,ndim=1,mode="c"] t not None,
            y0):
    cdef int n
    n = y.shape[0]
    y[0] = y0
    forward_euler(cb,<void*> f, &y[0], &t[0],n)
    return None

cdef double cb(void* f, const double &y, const double &t): 
    return (<object>f)(y,t)

