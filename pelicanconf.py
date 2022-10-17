AUTHOR = 'Terrence Dorsey'
SITENAME = 'tpd'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 
                'extras',
                'files',]
EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
}

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Prefect.io - Coordinating your dataflows', 'https://prefect.io/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/tpdorsey'),
          ('Twitter', 'http://twitter.com/tpdorsey'),
          ('LinkedIn', 'http://www.linkedin.com/in/terrencedorsey'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True