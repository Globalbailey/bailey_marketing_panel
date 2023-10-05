from django.contrib import admin

from django.contrib.admin import AdminSite

from gmcapp.models import MessageTemplate


class CustomAdminSite(AdminSite):
    site_header = 'Bailey Admin Panel'
    admin.site.site_header = "Bailey Admin Panel"
    admin.site.site_title = "Bailey Admin"
    admin.site.index_title = "Welcome to Bailey Admin Panel"


admin_site = CustomAdminSite(name='admin')  # Create an instance of your custom admin site

# Register your models with the custom admin site

# Register more models as needed
