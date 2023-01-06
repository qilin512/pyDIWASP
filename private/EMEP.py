import numpy as np
import warnings


def EMEP(xps, trm, kx, Ss, pidirs, miter, displ):

    szd = np.shape(xps)[0]
    ffreqs = np.shape(xps)[2]
    ddirs = np.shape(trm)[2]

    # ddir = 8 * np.arctan(1) / ddirs
    ddir = np.abs(pidirs[1] - pidirs[0])

    if displ < 2:
        warnings.simplefilter('ignore')

    Co = np.real(xps)
    Quad = -np.imag(xps)

    for ff in range(ffreqs):
        np.diagonal()


    Htemp = np.empty((ddirs, szd, szd), dtype='complex128')
    S = np.empty((ffreqs, ddirs), dtype='complex128')