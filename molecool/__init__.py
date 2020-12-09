"""
molecool
A python package for visualizing and analyzing molecular files. This is a sample package for a Best Practices Workshop from MolSSI.
"""

# Add imports here
from .functions import *

# Handle versioneer
from ._version import get_versions
# Add imports here
from .functions import *
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram
from .io import *

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
