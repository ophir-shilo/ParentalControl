from django.contrib import admin
from .models import BlockedUrl

class BlockedUrlAdmin(admin.ModelAdmin):
    list_display= ('url', 'user')
admin.site.register(BlockedUrl, BlockedUrlAdmin)
