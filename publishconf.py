#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.hydro.washington.edu/~jhamman/hydro-logic'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ATOM = '~jhamman/hydro-logic/atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

GOOGLE_ANALYTICS = 'UA-6032956-6'
DISQUS_SITENAME = 'hydro-logic'
