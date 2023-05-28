from django.contrib import admin
from quizmania.models import *
# Register your models here.
@admin.register(QuizCreation) 
class TMasterModuleOther(admin.ModelAdmin): 
    list_display = [field.name for field in QuizCreation._meta.fields]
