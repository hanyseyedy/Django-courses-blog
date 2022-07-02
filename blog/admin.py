from statistics import mode
from unicodedata import category
from django.contrib import messages
from django.utils.translation import ngettext
from django.contrib import admin
from .models import Article, Category

# Register your models here.


# admin header title change
admin.site.site_header = "وبلاگ جنگویی من"


@admin.action(description='انتشار مقالات انتخاب شده')
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='p')
    modeladmin.message_user(request, ngettext(
        '%d مقاله منتشر شد.',
        '%d مقاله منتشر شدند.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.action(description='پیش‌نویس شدن مقالات انتخاب شده')
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
        '%d مقاله پیش‌نویس شد.',
        '%d مقاله پیش‌نویس شدند.',
        updated,
    ) % updated, messages.SUCCESS)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'author',
                    'jpublish', 'status', 'category_to_srt')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = [make_published, make_draft]

    def category_to_srt(self, obj):
        return "، ".join([category.title for category in obj.category.active()])
    category_to_srt.short_description = "دسته بندی‌ها"


admin.site.register(Article, ArticleAdmin)
