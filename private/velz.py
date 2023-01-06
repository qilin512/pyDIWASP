import numpy as np


def velz(ffreqs, dirs, wns, z, depth):
    Kz = np.sinh(z * wns) / np.sinh(depth * wns)
    # include a maximum cutoff for the velocity response function
    Kz[Kz < 0.1] = 0.1
    trm = -1j * np.transpose((ffreqs * Kz, )) * np.ones_like(dirs)

    return trm