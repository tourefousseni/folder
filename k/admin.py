import  os
from django.contrib import admin
from django.utils import timezone
from k.models import Person



class KALALISOAdminSite(admin.AdminSite):

    site_header = "KALALISO"

admin_site = KALALISOAdminSite(name="admin")
admin_site.register(Person, site="admin_site")


