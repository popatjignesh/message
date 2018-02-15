from django.contrib import admin
from msg_user.models import *


class MessageAdmin(admin.ModelAdmin):
	ordering = ('-created_on',)
	list_display = ('message', 'message_from', 'message_to', 'created_on')


admin.site.register(User)
admin.site.register(Message, MessageAdmin)


