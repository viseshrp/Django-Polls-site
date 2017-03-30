from django.contrib import admin
from .models import Question, Choice


# Register your models here to make it show up in the admin interface.

# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Info', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)
