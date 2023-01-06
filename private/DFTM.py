import numpy as np
import warnings


def DFTM(xps, trm, kx, Ss, W, miter, displ):

    szd = np.shape(xps)[0]
    ffreqs = np.shape(xps)[2]
    ddirs = np.shape(trm)[2]
    ddir = 8 * np.arctan(1) / ddirs

    if displ < 2:
        warnings.simplefilter('ignore')

    Htemp = np.empty((ddirs, szd, szd), dtype='complex128')
    S = np.empty((ffreqs, ddirs), dtype='complex128')

    for ff in range(ffreqs):
        if displ >= 1:
            print('calculating for frequency {} of {}'.format(ff + 1, ffreqs))

        nxps = xps[:, :, ff]
        Sftmp = np.zeros(ddirs, dtype='complex128')
        for m in range(szd):
            for n in range(szd):
                H = trm[n, ff, :]
                Hs = np.conj(trm[m, ff, :])
                expx = np.exp(1j * kx[m, n, ff, :])
                Htemp[:, m, n] = H * Hs * expx
                xtemp = nxps[m, n] * H * Hs * expx
                Sftmp = Sftmp + xtemp

        E = Sftmp
        E = E / (ddir * np.sum(E))
        S[ff, :] = Ss[0, ff] * E

    return S
