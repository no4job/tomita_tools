__author__ = 'mdu'
"""Common settings and globals."""
from os.path import abspath, basename, dirname, join, normpath

########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory.
SCRIPT_ROOT = dirname(dirname(abspath(__file__)))


# Add all necessary filesystem paths to our system path so that we can use
# python import statements.
#sys.path.append(SITE_ROOT)
#sys.path.append(normpath(join(DJANGO_ROOT, 'apps')))
#sys.path.append(normpath(join(DJANGO_ROOT, 'libs')))
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
DEBUG = True


########## END DEBUG CONFIGURATION


########## GENERAL CONFIGURATION
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not all
# choices may be available on all operating systems. On Unix systems, a value
# of None will cause Django to use the same timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html.
LANGUAGE_CODE = 'ru-RU'

########## END GENERAL CONFIGURATION



########## DATABASE CONFIGURATION

########## END DATABASE CONFIGURATION

########## DEFAULT FILE ENCODINGS
DEFAULT_STYLE_LIST_FILE_ENCODING="cp1251"
DEFAULT_INPUT_HTML_FILE_ENCODING="cp1251"
#DEFAULT_OUTPUT_TXT_FILE_ENCODING="cp1251"
DEFAULT_OUTPUT_TXT_FILE_ENCODING="utf8"
DEFAULT_OUTPUT_XML_FILE_ENCODING="cp1251"
DEFAULT_INPUT_REFERENCE_XML_FILE_ENCODING="cp1251"
#DEFAULT_INPUT_COMPARED_XML_FILE_ENCODING="cp1251"
DEFAULT_INPUT_COMPARED_XML_FILE_ENCODING="utf8"
DEFAULT_OUTPUT_COMPARISON_TXT_FILE_ENCODING="utf8"