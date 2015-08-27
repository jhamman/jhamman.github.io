#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Joe Hamman'
SITENAME = u'Hydro-Logic'
SITESUBTITLE = u'A few thoughts on how I do things'

SITEURL = ''

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('Archives', './archives.html'),
             ('Home Page', 'http://www.hydro.washington.edu/~jhamman/'),
             ('Research Updates', 'http://www.hydro.washington.edu/~jhamman/updates')]
NEWEST_FIRST_ARCHIVES = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Hydrocomputing', 'http://hydrocomputing.wordpress.com/'),)
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# This requires Pelican 3.3+
STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
THEME = os.path.join(os.environ.get('DROPBOX'),
                     'Opensource/pelican-themes/octopress')
print("---->THEME = " + THEME)

PLUGIN_PATH = os.path.join(os.environ.get('DROPBOX'),
                           'Opensource/pelican-plugins')
print("---->PLUGIN_PATH = " + PLUGIN_PATH)
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

# Sharing
# TWITTER_USER = 'jhamman'
GOOGLE_PLUS_USER = 'jhamman'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = False
# TWITTER_TWEET_BUTTON = True
# TWITTER_LATEST_TWEETS = True
# TWITTER_FOLLOW_BUTTON = True
# TWITTER_TWEET_COUNT = 3
# TWITTER_SHOW_REPLIES = 'false'
# TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
SEARCH_BOX = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
