from django.contrib import admin

from .models import *

# Register your models here.


class Chemistry(admin.ModelAdmin):
    list_display = ('Question','Option1','Option2','Option3','Option4','Answer')

admin.site.register(ChemistryQuestions,Chemistry)

