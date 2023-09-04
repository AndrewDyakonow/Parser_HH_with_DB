from django.contrib import admin

from main.models import Vacancies


@admin.register(Vacancies)
class MainAdmin(admin.ModelAdmin):
    fields = ('id_vacancy',)
