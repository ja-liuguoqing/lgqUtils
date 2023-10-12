from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #对属性分类、别名
    fieldsets = [
        (None,               {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
        ]
    #对后台界面的展示列名修改
    list_display = ("question_text", "pub_date", "was_published_recently")

    inlines = [ChoiceInline]

    list_filter = ["pub_date"]

    search_fields = ["question_text"]

    


admin.site.register(Question, QuestionAdmin)