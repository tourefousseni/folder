import  os
from django.contrib import admin
from django import forms
from django.utils import timezone
from k.models import Person,  Command
# Command_Content, Produit, Mesure,  Payement,


class KALALISOAdminSite(admin.AdminSite):

    site_header = "KALALISO CREATION"

admin.site = KALALISOAdminSite(name="admin")
admin.site.register(Person, site="admin.site")

class PersonAdmin(admin.ModelAdmin):
    fields = ('nom', 'prenom')

# class PersonAdmin(admin.ModelAdmin):
#         exclude = ('contact')

    # list_display = 'nom', 'prenom', 'contact'
    # def name(self,obj):
    #     return obj.name
# class PersonForm(forms.ModelForm):
#
#     class Meta:
#         model = Person
#         exclude = ['name']

# admin.site.register(Produit, site="admin.site")
# admin.site.register(Mesure, site="admin.site")
# admin.site.register(Payement, site="admin.site")
admin.site.register(Command, site="admin.site")
# admin.site.register(Command_Content, site="admin.site")
