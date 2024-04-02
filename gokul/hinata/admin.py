from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone' ,'organization','option')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')

admin.site.register(Contact, ContactAdmin)