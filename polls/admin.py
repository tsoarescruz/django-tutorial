from django.contrib import admin
from polls.models import Choice
from polls.models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['question']}),
        ('Date information',    {'fields': ['pub_date']}),

    ]

# admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)

# Register your models here.
