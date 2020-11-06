from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'message', 'date')
    list_filter = ('date',)
    search_fields = ('nom', 'message' )

admin.site.register(Contact, ContactAdmin)