import  os
from django.contrib import admin
from django.utils import timezone
from k.models import Person, Article,\
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
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('release_date')
    list_display = ('first_name',
                    'last_name',
                    'contact',
                    'domicile',
                    'release_date')
    autocomplete_fields = ('Modeles',)

admin_site.register(Article, site="admin_site")
admin_site.register(Payement, site="admin_site")
admin_site.register(Mesure, site="admin_site")
admin_site.register(Typeperson, site="admin_site")
