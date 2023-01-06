import numpy as np


def accy(ffreqs, dirs, wns, z, depth):
    Kz = np.cosh(z * wns) / np.sinh(depth * wns)
    #include a maximum cuttoff for the velocity response function
    Kz[Kz < 0.1] = 0.1
    trm = -1j * np.transpose(((ffreqs ** 2) * Kz, )) * np.sin(dirs)

    return trm
