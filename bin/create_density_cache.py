"""Cache slow calculations so they can be quickly interpolated across m5 maps"""

import numpy as np
from lbg_tools import TomographicBin

from u_band_strat import data_dir

# Cache number density calculations
m5s = np.arange(22, 29, 0.1)
cache_number_density = {}
for band in "ugr":
    vals0 = []
    for mag_cut in m5s:
        vals1 = []
        for m5_det in m5s:
            vals1.append(
                TomographicBin(band=band, mag_cut=mag_cut, m5_det=m5_det).number_density
            )
        vals0.append(vals1)
    cache_number_density[band] = np.array(vals0)
np.savez(
    data_dir / "cache_number_density.npz",
    m5=m5s,
    n=cache_number_density,
)
