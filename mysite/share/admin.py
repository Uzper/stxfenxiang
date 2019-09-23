from django.contrib import admin
from .models import Share, ShareType


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ('photo', 'title', 'video', 'read_num', 'author', 'content', )


@admin.register(ShareType)
class ShareTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)