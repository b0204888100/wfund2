"""`appengine_config` gets loaded when starting a new application instance."""
from google.appengine.ext import vendor
# insert `lib` as a site directory so our `main` module can load
# third-party libraries, and override built-ins with newer
# versions.
vendor.add('lib')
#vendor.add('libx')
import sys
import os.path
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
# appengine_config.py
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
# Add any libraries install in the "lib" folder.
