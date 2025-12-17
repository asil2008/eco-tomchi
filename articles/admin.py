from django.contrib import admin
from .models import Article, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display faqat models.py dagi maydonlar bilan mos bo'lishi shart
    list_display = ('title', 'category', 'published_date') 
    list_filter = ('category', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}