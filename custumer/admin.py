from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(NewUser)
admin.site.register(Affectation)
admin.site.register(CritereChef)
admin.site.register(CritereConj)
admin.site.register(CritereEnfant)
admin.site.register(CritereCharge   )
admin.site.register(CritereCommodite)
admin.site.register(CritereEquipement)
admin.site.register(CritereDeces)
admin.site.register(CritereHabitat)
admin.site.register(CritereGeneral)

admin.site.register(Quartier)