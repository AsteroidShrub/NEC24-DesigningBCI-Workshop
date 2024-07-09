

import os
import logging
import subprocess
import re
import numpy as np

from random import shuffle

logger = logging.getLogger("timeflux")

crash_bad_param = bool(os.getenv("EXIT_ON_BAD_PARAMETER", "true"))


# Defining an easy to use function for error handling
def error_handling(key, msg, default, force_fail=False) -> None:
    if crash_bad_param or force_fail:
        raise ValueError(msg)
    else:
        logger.warning(f"{msg}, defaulting to {default}")
        os.environ[key] = default


# generic method to check the type of an environment variable
def check_type(key, t: type):
    if os.environ[key] is None:
        return False
    try:
        t(os.environ[key])
    except:
        return False
    return True


# Specific for int type checking
def check_int(key) -> bool:
    return check_type(key, int)


# Specific for float type checking
def check_float(key) -> bool:
    return check_type(key, float)


# Specific for bool type checking
def check_boolean(key) -> bool:
    return check_type(key, bool)


def check_flavor(flavor_keys):
    return any([os.environ[fk] is not None for fk in flavor_keys])


# Check that the device graph exists
os.environ["DEVICE"] = os.getenv("DEVICE")
if not os.path.exists(os.path.join("graphs", os.environ["DEVICE"] + ".yaml")):
    error_handling(
        "DEVICE",
        f"Could not find graph file {os.environ['DEVICE']}.yaml in the graph folder",
        "graphs/dummy",
    )

# Check that it is a coma separated list of electrode names, trim spaces
os.environ["CHANNELS"] = os.getenv("CHANNELS")
if not os.environ["CHANNELS"]:
    error_handling(
        "CHANNELS",
        "CHANNELS must a list of coma separated  name of electrodes (spaces are trimmed)",
        None,
        True,
    )

# Check that it is a coma separated list of electrode names, trim spaces
os.environ["BANDS"] = os.getenv("BANDS")
if not os.environ["BANDS"]:
    error_handling(
        "BANDS",
        "BANDS must a list of coma separated name of wave bands (spaces are trimmed)",
        ["alpha", "beta", "gamma", "delta", "theta"],
        True,
    )
else:
    bands_set = set() 
    for b in os.environ["BANDS"].split('.'):
        if b in ["alpha", "beta", "gamma", "delta", "theta"]
            bands_set.update({b})
    os.environ["BANDS"] = ','.join(bands_set)

# Timeflux
os.environ["RECORD_DATA"] = os.getenv("RECORD_DATA")
if not check_boolean("RECORD_DATA"):
    error_handling("RECORD_DATA", f"RECORD_DATA must be a boolean", "true")

logger.debug("Configuration file loaded successfully")
