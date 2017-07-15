#!/usr/bin/env python
# PART 1:
# Run the code, save the file, exit, then execute from the bash console:
# python3.5 Problem1_Testing.py
# You WILL get a crash. We will fix this as an exercise in PART 3.

# PART 2:
# Wrap the entire code after the imports in a try/except block. 
# The exception should print the error and then on a new line "still working on it"

# PART 3: 
# There is something wrong with the astroML package that is causing it to crash! We will fix this error and then try again
# A)
# B) Reinstall astroML by executing on the bash console:
# python3.5 setup.py install --user
# C) Execute this file again. Look at the image that the code prints out

# PART 4:
# A) Put all the code after the imports in a function that takes a single argument, the projection
# B) Add documentation to your function indicating what values of the projection are allowed. Options are:
# 'hammer', 'aitoff', 'mollweide', 'lambert'
# C) Call your new function with each projection one at a time, verify it is working
# D) Change your function to change the name of the figure depending on the projection, so that when you
# call it 4 times you get 4 figures
# E) Add an assertion to check to make sure that the projection is one of the options
# F) Call your function with the argument "sillyprojection" and verify your assertion cause the code to crash

# The following code works with the SDSS Survey
# License: BSD
#   The figure is an example from astroML: see http://astroML.github.com
import numpy as np
from matplotlib import pyplot as plt

from astroML.datasets import fetch_sdss_specgals

data = fetch_sdss_specgals()

#------------------------------------------------------------
# plot the RA/DEC in an area-preserving projection

RA = data['ra']
DEC = data['dec']

# convert coordinates to degrees
RA -= 180
RA *= np.pi / 180
DEC *= np.pi / 180

ax = plt.axes(projection='mollweide')

ax = plt.axes()
ax.grid()
plt.scatter(RA, DEC, s=1, lw=0, c=data['z'], cmap=plt.cm.copper,
            vmin=0, vmax=0.4)

plt.title('SDSS DR8 Spectroscopic Galaxies')
cb = plt.colorbar(cax=plt.axes([0.05, 0.1, 0.9, 0.05]),
                  orientation='horizontal',
                  ticks=np.linspace(0, 0.4, 9))
cb.set_label('redshift')



plt.savefig("Problem1_SDSS.png")
