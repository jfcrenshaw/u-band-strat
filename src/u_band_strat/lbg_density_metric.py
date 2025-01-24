"""Function to calculate the LBG number density metric."""

import numpy as np

from .density_interpolator import interpolate_number_density


def calc_lbg_density_metric(
    band: str,
    drop_map: np.ma.array,
    det_map: np.ma.array,
    dropout: float = 1,
    snr_min: float = 3,
    f_wfd: float = 0.75,
) -> float:
    """Calculate the LBG density metric.

    Parameters
    ----------
    band : str
        Name of the dropout band
    drop_map : np.ma.array
        Map of 5-sigma depths in the dropout band
    det_map : np.ma.array
        Map of 5-sigma depths in the detection band
    dropout : float, optional
        Dropout threshold. Default is 1.
    snr_min : float, optional
        SNR floor in the dropout band. Default is 3.
    f_wfd : float, optional
        Deepest fraction of WFD footprint to use. Default is 0.75.

    Returns
    -------
    float
        LBG number density
    """
    # If the dropout band is deeper
    if np.ma.median(drop_map) > np.ma.median(det_map):
        # Cutout deepest fraction
        deep_cut = np.quantile(det_map[~det_map.mask], 1 - f_wfd)

        # Determine the cut
        cut = deep_cut - dropout + 2.5 * np.log10(5 / snr_min)

        # Determine survey mask
        mask = det_map.mask | drop_map.mask | (det_map < deep_cut)

    # If the detection band is deeper
    else:
        # Cutout deepest fraction
        deep_cut = np.quantile(drop_map[~drop_map.mask], 1 - f_wfd)

        # Determine the cut
        cut = deep_cut - dropout + 2.5 * np.log10(5 / snr_min)

        # Determine survey mask
        mask = det_map.mask | drop_map.mask | (drop_map < deep_cut)

    # Get density of un-masked region
    density = interpolate_number_density(band, cut, det_map[~mask])

    # Return the mean
    return np.nanmean(density)
