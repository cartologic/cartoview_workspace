from django.urls import path
from future import standard_library

from .views import workspace

standard_library.install_aliases()
urlpatterns = [
    path('', workspace, name="my_workspace")
]
