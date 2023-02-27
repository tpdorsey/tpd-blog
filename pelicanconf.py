AUTHOR = 'Terrence Dorsey'
SITENAME = 'TPD'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 
                'extras',
                'files',]
EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
}
THEME = 'theme/mynewidea'
MENUITEMS = [('Home', '/'),]

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS_WIDGET_NAME = 'Links'
LINKS = (("Prefect.io - Coordinating the world's dataflows", 'https://prefect.io/'),)

# Social widget
SOCIAL_WIDGET_NAME = 'Social'
SOCIAL = (('GitHub', 'https://github.com/tpdorsey'),
          ('Twitter', 'http://twitter.com/tpdorsey'),
          ('LinkedIn', 'http://www.linkedin.com/in/terrencedorsey'),
          ('Mastodon', 'https://vermont.masto.host/@tpdorsey'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True