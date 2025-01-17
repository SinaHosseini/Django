from django.contrib import admin
from .models import Question, Choice
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import TabularInlineJalaliMixin


class ChoiceInline(TabularInlineJalaliMixin, admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "get_jalali_pub_date", "was_published_recently"]
    ordering = ["-pub_date"]  # مرتب‌سازی بر اساس تاریخ انتشار

    def get_jalali_pub_date(self, obj):
        return obj.get_jalali_pub_date()

    get_jalali_pub_date.short_description = "تاریخ انتشار (جلالی)"


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
