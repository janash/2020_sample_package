"""
molecool
A python package for visualizing and analyzing molecular files. This is a sample package for a Best Practices Workshop from MolSSI.
"""

# Add imports here
from .functions import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
