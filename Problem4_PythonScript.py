#!/usr/bin/env python
# Your code here
# A) You will need to install healpy from the bash console with pip3.5 install --user healpy
# B) Next run the code
# C) Put the body of the code in a function that has one parameter: the title of the plot. Give this parameter a default equal to the current plot title
# D) Practice calling your function.
# E) Use sys.argv (don't forget to import sys first) to access arguments from the commandline. When the function is called as a script, require one argument the plot title, and access it with sys.argv
# F) Now make the argument on the commandline optional.

# Author: Jake VanderPlas
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com
#   To report a bug or issue, use the following forum:
#    https://groups.google.com/forum/#!forum/astroml-general
import numpy as np
from matplotlib import pyplot as plt
# warning: due to a bug in healpy, importing it before pylab can cause
#  a segmentation fault in some circumstances.
import healpy as hp

from astroML.datasets import fetch_wmap_temperatures

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=True)

#------------------------------------------------------------
# First plot an example pixellization

# Prepare the healpix pixels
NSIDE = 4
m = np.arange(hp.nside2npix(NSIDE))
print("number of pixels:", len(m))

# Plot the pixelization
fig = plt.figure(1, figsize=(5, 3.75))
hp.mollview(m, nest=True, title="HEALPix Pixels (Mollweide)", fig=1)

# remove colorbar: we don't need it for this plot
fig.delaxes(fig.axes[1])

#------------------------------------------------------------
# Next plot the wmap pixellization
wmap_unmasked = fetch_wmap_temperatures(masked=False)

# plot the unmasked map
fig = plt.figure(2, figsize=(5, 3.75))
hp.mollview(wmap_unmasked, min=-1, max=1, title='Raw WMAP data',
            unit=r'$\Delta$T (mK)', fig=2)
fig.axes[1].texts[0].set_fontsize(8)

fig.savefig("problem4.png")

if __name__=='__main__':
    # your code here
    pass

