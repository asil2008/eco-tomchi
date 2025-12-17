from django.contrib import admin
from .models import Article, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date', 'is_daily_highlight')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')

admin.site.register(Category)