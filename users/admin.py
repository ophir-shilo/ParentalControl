from django.contrib import admin
from send.models import KeyLog, ScreenRecord

class KeyLogAdmin(admin.ModelAdmin):
    list_display= ('content', 'user', 'writeTime')
admin.site.register(KeyLog, KeyLogAdmin)


class ScreenRecordAdmin(admin.ModelAdmin):
    list_display= ('record', 'user', 'writeTime')
admin.site.register(ScreenRecord, ScreenRecordAdmin)
