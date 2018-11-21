from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from builtins import *

from django.conf.urls import url
from future import standard_library

from .views import workspace

standard_library.install_aliases()
urlpatterns = [
    url('^$', workspace, name="my_workspace"), ]
