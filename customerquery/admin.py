from django.contrib import admin
from .models import CustomerQuery

admin.site.site_header = 'Reply Genie'


@admin.register(CustomerQuery)
class CustomerQueryAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'subject', 'received_at', 'is_processed')
    list_filter = ('is_processed',)
    search_fields = ('sender_name', 'sender_email', 'subject', 'body')
    date_hierarchy = 'received_at'


