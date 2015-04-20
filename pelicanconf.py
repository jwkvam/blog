#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Jacques Kvam'
SITENAME = 'Nothing New'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAG_CLOUD_MAX_ITEMS = 0
# BOOTSTRAP_FLUID = True
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
HIDE_SIDEBAR = True
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

STATIC_PATHS = ['notebooks', 'logo.png']
NOTEBOOK_DIR = 'notebooks'

PLUGIN_PATHS = ['plugins/pelican']
PYGMENTS_STYLE = 'solarizedlight'
# PYGMENTS_STYLE = 'autumn'
PLUGINS = ['summary', 'liquid_tags.notebook']
THEME = 'themes/bootstrap/'
FAVICON = 'logo.png'

# if not os.path.exists('_nb_header.html'):
#     import warnings
#     warnings.warn("_nb_header.html not found.  "
#                   "Rerun make html to finalize build.")
# else:
#     EXTRA_HEADER = open('_nb_header.html').read() #.decode('utf-8')
