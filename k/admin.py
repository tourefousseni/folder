import  os
from django.contrib import admin
from k.models import Person, Modeles,\
    Payement, Mesure, Typeperson


class KALALISOAdminSite(admin.AdminSite):

    site_header = "KALALISO"

admin_site = KALALISOAdminSite(name="admin")

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     pass
# @admin.register(Modeles)
# class ModelesAdmin(admin.ModelAdmin):
#     pass
# @admin.register(Payement)
# class PayementAdmin(admin.ModelAdmin):
#     pass
# @admin.register(Mesure)
# class MesureAdmin(admin.ModelAdmin):
#     pass
# @admin.register(Typeperson)
# class TypepersonAdmin(admin.ModelAdmin):
#     pass

admin_site.register(Person, site="admin_site")
admin_site.register(Modeles, site="admin_site")
admin_site.register(Payement, site="admin_site")
admin_site.register(Mesure, site="admin_site")
admin_site.register(Typeperson, site="admin_site")
