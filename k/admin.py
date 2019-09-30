import  os
from django.contrib import admin
from django.utils import timezone
from k.models import Person, Article, Mesure, Payement



class KALALISOAdminSite(admin.AdminSite):

    site_header = "KALALISO"

admin.site = KALALISOAdminSite(name="admin")
admin.site.register(Person, site="admin.site")
admin.site.register(Article, site="admin.site")
admin.site.register(Mesure, site="admin.site")
admin.site.register(Payement, site="admin.site")