from statistics import mode
from unicodedata import category
from django.contrib import admin
from .models import Article, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'category_to_srt')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']

    def category_to_srt(self, obj):
        return "، ".join([category.title for category in obj.category_publised()])
    category_to_srt.short_description = "دسته بندی‌ها"


admin.site.register(Article, ArticleAdmin)
