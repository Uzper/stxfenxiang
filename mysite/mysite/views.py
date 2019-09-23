from django.shortcuts import render
from share.models import Share, ShareType


def home(request):
    context = {}
    shares = Share.objects.all()
    share_type_list = ShareType.objects.all()
    context['shares'] = shares
    context['share_type_list'] = share_type_list
    return render(request, 'home.html', context)
