from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from builtins import *

from django.contrib.auth.decorators import login_required
from cartoview.app_manager.models import AppInstance
from django.shortcuts import render
from future import standard_library
from geonode.documents.models import Document
from geonode.groups.models import GroupProfile
from geonode.layers.models import Layer
from geonode.maps.models import Map
import requests
import json

standard_library.install_aliases()


@login_required
def workspace(request):
    
    created_apps = AppInstance.objects.all()
    maps_count = Map.objects.all().count()
    layers_count = Layer.objects.all().count()
    documents_count = Document.objects.all().count()
    groups_count = GroupProfile.objects.all().count()

    return render(

        request,
        template_name='cartoview_workspace/workspace.html',
        context={
            'maps_count': maps_count,
            'layers_count': layers_count,
            "groups_count": groups_count,
            "documents_count": documents_count,
            "loggeduser": request.user.username
        })

