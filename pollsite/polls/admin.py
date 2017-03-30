from django.contrib import admin
from .models import Question

# Register your models here to make it show up in the admin interface.

#admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)