from statistics import mode
from django.contrib import admin
from .models import Articles

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-publish']


admin.site.register(Articles, ArticleAdmin)
