from django.contrib import admin
from .models import Conversation

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

admin.site.register(Conversation, ConversationAdmin)
