from typing import Optional, Tuple, Union
import numpy as np

def calc_FWHM(x:np.ndarray, y:np.ndarray, with_locs:bool=False)->Union[
    Optional[float],
    Tuple[Optional[float], Tuple[Optional[float], Optional[float]]]
    ]:
    
    peak_height, peak_loc = np.max(y), np.argmax(y)
    peak_loc_value = x[peak_loc]

    x_lower = x[x < peak_loc_value]
    x_upper = x[x > peak_loc_value]

    y_lower = np.flip(y[x < peak_loc_value])
    y_upper = y[x > peak_loc_value]

    interval_low = None
    interval_high = None

    # Find lower
    for i, loc in enumerate(reversed(x_lower)):
        if y_lower[i] <= 0.5*peak_height:
            interval_low = loc
            break

    # Find upper
    for i, loc in enumerate(x_upper):
        if y_upper[i] <= 0.5*peak_height:
            interval_high = loc
            break
    
    FWHM = (interval_high - interval_low) if interval_low is not None and interval_high is not None else None
    
    if with_locs:
        return FWHM, (interval_low, interval_high)
    else:
        return FWHM