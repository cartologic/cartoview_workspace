from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def workspace(request):
    return render(
        request,
        template_name='cartoview_workspace/workspace.html',
        context={}
        )
