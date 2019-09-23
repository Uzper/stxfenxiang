from django.urls import path
from . import views


urlpatterns = [
    path('', views.share_list, name="share_list"),
    path('type/<int:type_pk>', views.share_type_list, name='share_type'),
    path('<int:share_pk>', views.share_detail, name='share_detail'),
]
