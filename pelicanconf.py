#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Jacques Kvam'
# AUTHOR = 'Newfing'
SITENAME = 'Nothing New'
# SITEURL = ''
HIDE_SITENAME = False

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

ABOUT_ME = None
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
# SOCIAL = (('You can add links in your config file', 'google.com'),
#           ('Another social link', '#'),)
# GITHUB_URL = 'github.com/jwkvam'
# TWITTER_USERNAME = 'jwkvam'

# SOCIAL = (('twitter', 'http://twitter.com/jwkvam'),
#           ('github', 'http://github.com/jwkvam'),
#           ('linkedin', 'http://www.linkedin.com/in/jwkvam'))

DIRECT_TEMPLATES = ['index', 'authors', 'archives']
SHOW_ARTICLE_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

STATIC_PATHS = ['notebooks', 'logos', 'custom']
NOTEBOOK_DIR = 'notebooks'

PLUGIN_PATHS = ['plugins/pelican-plugins']
PYGMENTS_STYLE = 'solarizedlight'
FAVICON = 'logos/logo.png'
SITELOGO = '' #'logos/ilogo.png'
SITELOGO_SIZE = 30
PLUGINS = ['summary', 'liquid_tags.notebook']
THEME = 'themes/bootstrap/'

CUSTOM_CSS = 'custom/custom.css'
BOOTSTRAP_THEME = 'readable'
# Tell Pelican to change the path to 'static/custom.css' in the output dir
# EXTRA_PATH_METADATA = {
#     'static/custom.css': {'path': 'static/custom.css'}
# }

# if not os.path.exists('_nb_header.html'):
#     import warnings
#     warnings.warn("_nb_header.html not found.  "
#                   "Rerun make html to finalize build.")
# else:
#     EXTRA_HEADER = open('_nb_header.html').read() #.decode('utf-8')
