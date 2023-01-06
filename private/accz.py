import numpy as np


def accz(ffreqs, dirs, wns, z, depth):
    Kz = np.sinh(z * wns) / np.sinh(depth * wns)
    #include a maximum cuttoff for the velocity response function
    Kz[Kz < 0.1] = 0.1
    trm = -np.transpose(((ffreqs ** 2) * Kz, )) * np.ones_like(dirs)

    return trm
