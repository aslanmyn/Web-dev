
from .models import Vacancy, Company
from django.contrib import admin
from .models import Vacancy, Company

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'salary')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
