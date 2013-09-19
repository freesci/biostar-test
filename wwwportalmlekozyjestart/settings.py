# Django settings for wwwportalmlekozyjestart project.
import os, sys, re, south


def path(*args):
    "Generates absolute paths"
    return os.path.abspath(os.path.join(*args))



DEBUG = True
TEMPLATE_DEBUG = DEBUG

# admin site may fail if this setting is active
TEMPLATE_STRING_IF_INVALID = "*** MISSING ***"

# the time in seconds between session updates
SESSION_UPDATE_TIME = 10 * 60  # in seconds


ADMINS = (
	('Pawel', 'szczesny.pawel@googlemail.com'),
    # ('Your Name', 'your_email@example.com'),
)

# how many post per page to show
POSTS_PER_PAGE = 15

# feed delay in minutes
FEED_DELAY = 10

AD_MIN_REP = 10
AD_MOD_REP = 20



MANAGERS = ADMINS
__CURR_DIR = path(os.path.dirname(__file__))

# set location relative to the current file directory
HOME_DIR = path(__CURR_DIR)
DATABASE_DIR = path(HOME_DIR, 'db')
DATABASE_NAME = path(DATABASE_DIR, 'biostar.db')
TEMPLATE_DIR = path(HOME_DIR, 'server', 'templates')
STATIC_DIR = path(HOME_DIR, 'static')
EXPORT_DIR = path(HOME_DIR, '..', 'apache', 'export')
WHOOSH_INDEX = path(HOME_DIR, 'db', 'index')
PLANET_DIR = path(HOME_DIR, 'db', 'planet')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DATABASE_NAME, # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

__ZIP_LIBS = [
    path(__CURR_DIR, '..', 'libs'),
    path(__CURR_DIR, '..', 'libs', 'libraries.zip'),
]
sys.path.extend(__ZIP_LIBS)


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

SITE_ID = 1
SITE_DOMAIN = 'www.portalmlekozyje.megiteam.pl'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '.'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_ROOT = path(EXPORT_DIR, "static")

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	STATIC_DIR,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',

)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1i6kk35_@zce8j4zkil8@n&amp;wu*688oms*k^&amp;%yw+-gt*bhsnai'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'wwwportalmlekozyjestart.middleware.XForwardedForMiddleware',
    'wwwportalmlekozyjestart.middleware.LastVisit',

]
COMPRESS_ENABLED=False
COMPRESS_PRECOMPILERS = (
    #('text/coffeescript', 'coffee --compile --stdio'),
    #('text/less', 'lessc {infile} {outfile}'),
)


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache' if DEBUG else 'django.core.cache.backends.locmem.LocMemCache',
        #'BACKEND':  'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}


ROOT_URLCONF = 'wwwportalmlekozyjestart.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wwwportalmlekozyjestart.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	TEMPLATE_DIR,
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    "wwwportalmlekozyjestart.context.extras",
    "wwwportalmlekozyjestart.context.popular_tags"
)
AUTH_PROFILE_MODULE = "server.UserProfile"


AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

OPENID_CREATE_USERS = True
OPENID_UPDATE_DETAILS_FROM_SREG = True
OPENID_USE_AS_ADMIN_LOGIN = True

# allow migration based on user email
ALLOW_OPENID_MIGRATION = True

LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'



INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'south',
    'compressor',
    'wwwportalmlekozyjestart.server',
    'django_openid_auth',
    'django.contrib.sitemaps',

]

# add debugging tools
if DEBUG:
    MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.append('debug_toolbar')

# don't allow mutating this
MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES)



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

GOOGLE_TRACKER = ""
GOOGLE_DOMAIN = ""

# needs to be turned on explicitly
CONTENT_INDEXING = True

# rank gains expressed in hours
POST_UPVOTE_RANK_GAIN = 1
POST_VIEW_RANK_GAIN = 0.1
BLOG_VIEW_RANK_GAIN = 0.1

# if this is set together with the DEBUG mode allows test logins
# don't turn it on in production servers!
SELENIUM_TEST_LOGIN_TOKEN = None

# no external authentication by default
# dictionary keyed by name containing the tuple of (secret key, template)
EXTERNAL_AUTHENICATION = {

}

# setting the session for multiple servers
SESSION_COOKIE_DOMAIN = ""

MIN_POST_SIZE = 15
MAX_POST_SIZE = 20000

RECENT_VOTE_COUNT = 10
RECENT_TAG_COUNT = 30
# set the tag names are to be displayed on the main page
IMPORTANT_TAG_NAMES = "rna-seq chip-seq assembly snp metagenomics vcf cnv mirna indel bwa bowtie bedtools biopython bioperl".split()

# the interval specified in hours
# that user activity throttling is computed over
TRUST_INTERVAL = 3

# how many posts may a new user make in a trust interval
# new user means a user that joined within a trust interval time
TRUST_NEW_USER_MAX_POST = 3

# how many posts may a trusted user make withing a trust in
TRUST_USER_MAX_POST = 15

COUNT_INTERVAL_WEEKS = 25

# the time between registering two post views
# from the same IP, in minutes
POST_VIEW_UPDATE = 30

# TEMPLATE LAYOUT,
# One may override these variables from the settings file
# 

#s data governs the layout of the PILL_BAR    
# bar name, link url, link name, counter key
ANON_PILL_BAR = [
    ("all", "/", "Show&nbsp;All", "" ),
    ("best", "/show/best", "Popular", "Popular"),
    ("bookmarked", "/show/bookmarked", "Bookmarked", "Bookmarked"),
    ("questions", "/show/questions/", "Questions", "Question" ),
    ("unanswered", "/show/unanswered/", "Unanswered", "Unanswered" ),
    ("forum", "/show/forum/", "Forum", "Forum" ),
    ("howto", "/show/howto/", "How To", "howto" ),
    #("galaxy", "/show/galaxy/", "Galaxy", "Galaxy" ),
    ("jobs", "/show/jobs/", "Jobs", "Job" ),
    ("planet", "/show/planet/", "Planet", "Blog" ),

]

USER_PILL_BAR = [

    ("myposts", "/show/myposts/", '<i class="icon-user tx" data-toggle="tooltip" title="Your posts"></i>', "" ),
    ("mytags", "/show/mytags/", '<i class="icon-tags tx" data-toggle="tooltip" title="Your tags"></i>', "" ),
    ("mybookmarks", "/show/mybookmarks/", '<i class="icon-bookmark tx" data-toggle="tooltip" title="Your bookmarks"></i>', "" ),
    ("myvotes", "/show/myvotes/", '<i class="icon-heart tx" data-toggle="tooltip" title="Up votes"></i>', "vote_count", "" ),
    ("messages", "/show/messages/", '<i class="icon-envelope tx" data-toggle="tooltip" title="Messages"></i>', "message_count", "" ),
("all", "/", "Show&nbsp;All", "" ),

    ("best", "/show/best", "Popular", "Popular"),
    ("questions", "/show/questions/", "Questions", "Question" ),
    ("unanswered", "/show/unanswered/", "Unanswered", "Unanswered" ),
    ("forum", "/show/forum/", "Forum", "Forum" ),
    ("howto", "/show/howto/", "How To", "howto" ),
    #("galaxy", "/show/galaxy/", "Galaxy", "Galaxy" ),
    ("jobs", "/show/jobs/", "Jobs", "Job" ),
    ("planet", "/show/planet/", "Planet", "Blog" ),

]

SHOW_ADS = False

#
# remapping the templates to local versions
# a row is the way a post is rendered on a page
# list below the templates to be loaded for a post type
# to reduce clutter there is a default mapper that
# for missing types attempts to map each type to rows/row.type.html
# django template lookup rules apply
#
TEMPLATE_ROWS = {
    'job': "rows/row.job.html",
}

# how long will an ad be active by default
DEFAULT_AD_EXPIRATION = 1


import os
import os.path

try:
    import dj_database_url
except ImportError:
    pass
else:
    try:
        with open(os.environ['DATABASE_PATH_WWWPORTALMLEKOZYJESTART'], 'r') as url_file:
            url = url_file.read()
    except (IOError, KeyError):
        pass
    else:
        DATABASES['default'] = dj_database_url.parse(url)

if STATIC_ROOT == '':
   STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
