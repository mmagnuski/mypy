# this file is just to easily get most common imports at once
# by writing: `from mypy.init import *

import os
import os.path as op
from glob import glob

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy.io import loadmat, savemat
from scipy import stats, signal

# from scipy.stats import distributions as dist
# from scipy import fftpack

try:
  from showit import image
except ImportError:
  pass

# import seaborn as sns?
# maybe seaborn.apionly?

from mypy.utils import find_index
from mypy.freq import dB
