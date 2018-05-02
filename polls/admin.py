from django.contrib import admin
from polls.models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = 'question_text', 'pub_date'
    search_fields = 'question_text', 'pub_date'

class ChoiceAdmin(admin.ModelAdmin):
    list_display = 'question', 'choice_text','votes'
    search_fields = 'question', 'choice_text'
    list_editable = 'choice_text',
    list_filter = 'question',

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)