from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from builtins import *

from account.decorators import login_required
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
    owner = request.user
    created_apps = AppInstance.objects.all()
    maps_count = Map.objects.all().count()
    layers_count = Layer.objects.all().count()
    documents_count = Document.objects.all().count()
    groups_count = GroupProfile.objects.all().count()
    layers_req = requests.get('http://'+request.get_host()+'/api/layers?owner__username='+owner.username)
    layer = layers_req.json()
    maps_req = requests.get('http://'+request.get_host()+'/api/maps?owner__username='+owner.username)
    maps = maps_req.json()
    appinstances_req = requests.get('http://'+request.get_host()+'/api/appinstances/?owner__username='+owner.username)
    apps =  appinstances_req.json()
    groups_req = requests.get('http://'+request.get_host()+'/api/groups?owner__username='+owner.username)
    groups = groups_req.json()
    docs_req = requests.get('http://'+request.get_host()+'/api/documents?owner__username='+owner.username)
    docs = docs_req.json()
  
  
    return render(
        request,
        template_name='cartoview_workspace/workspace.html',
        context={
            'my_apps': apps,
            'my_layers': layer,
            'created_apps': created_apps,
            'my_maps': maps,
            'maps_count': maps_count,
            'layers_count': layers_count,
            "groups": groups,
            "groups_count": groups_count,
            "documents": docs,
            "documents_count": documents_count
        })
