from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def article_list(request):
    """Bosh sahifa: Barcha maqolalar ro'yxati"""
    articles = Article.objects.all().order_by('-published_date')
    categories = Category.objects.all()
    
    context = {
        'articles': articles,
        'categories': categories,
        'page_title': 'Barcha maqolalar'
    }
    return render(request, 'articles/index.html', context)

def category_detail(request, category_id):
    """Kategoriyani tanlaganda faqat shu turkumdagi maqolalarni chiqarish"""
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category).order_by('-published_date')
    categories = Category.objects.all() # Menyuda ko'rinishi uchun
    
    context = {
        'category': category,
        'articles': articles,
        'categories': categories,
        'current_category': category
    }
    return render(request, 'articles/index.html', context)

def article_detail(request, slug):
    """Maqola to'liq matni"""
    article = get_object_or_404(Article, slug=slug)
    categories = Category.objects.all()
    return render(request, 'articles/detail.html', {'article': article, 'categories': categories})

def about(request):
    return render(request, 'articles/about.html', {'categories': Category.objects.all()})

def contact(request):
    return render(request, 'articles/contact.html', {'categories': Category.objects.all()})