from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = 1  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "metaVis: An integrated data upload and interactive heatmap visualization tool built for exploratory data analysis and introspection."
# Long description will go up on the pypi page
long_description = """
metaVis
========
metaVis is a heatmap visualization tool that enables users to interactively interface with their data that centers around the inclusion of "metadata" 
\- supplementary information behind each data point that characterizes and contextualizes it. 
metaVis comprises two main components: a server and web portal that provides flexible data upload and the heatmap visualization tool itself in the form of a generated standalone html file. 
The metaVis visualization tool is meant to enable scientists and researchers to more easily visualize their datasets, recontextualize and gain a wider perspective 
of their data through the integration of "metadata", and interactively perform exploratory data analysis. 


License
=======
``metaVis`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.
"""

NAME = "metaVis"
MAINTAINER = "Michael Zhao"
MAINTAINER_EMAIL = "mzhao@fredhutch.org"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/agartland/metadataVis"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Michael Zhao"
AUTHOR_EMAIL = "mzhao@fredhutch.org"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {}
REQUIRES = ['numpy', 'scipy', 'pandas', 'sklearn', 'bokeh', 'twisted', 'jinja2']