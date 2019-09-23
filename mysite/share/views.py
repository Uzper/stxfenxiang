from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Share, ShareType


def share_list(request):
    share_all_list = Share.objects.all()
    paginator = Paginator(share_all_list, 2)
    page_num = request.GET.get('page', 1)
    page_of_shares = paginator.get_page(page_num)
    print(page_of_shares.paginator.page_range)
    context = {}
    context['shares'] = page_of_shares.object_list
    context['page_num_shares'] = page_of_shares
    context['share_type'] = ShareType.objects.all()
    return render(request, 'share/share_list.html', context)


def share_type_list(request, type_pk):
    context = {}
    share_type = get_object_or_404(ShareType, pk=type_pk)
    shares = Share.objects.filter(share_type=share_type)
    context['shares'] = shares
    context['share_type'] = share_type
    return render(request, 'share/type_of_shares.html', context)


def share_detail(request, share_pk):
    context = {}
    share = get_object_or_404(Share, pk=share_pk)
    if not request.COOKIES.get('share_%s_read' % share_pk):
        share.read_num += 1
        share.save()
    context['share'] = share
    context['previous_share'] = Share.objects.filter(id__gt=share.pk).last()
    print(context['previous_share'])
    context['next_share'] = Share.objects.filter(id__lt=share.pk).first()
    # context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    # context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    response = render(request, 'share/share_detail.html', context)
    response.set_cookie('share_%s_read' % share_pk, 'true')
    return response
