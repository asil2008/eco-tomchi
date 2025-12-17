from django.urls import path
from . import views

# Bu nom shablonlarda 'articles:...' ko'rinishida foydalanish uchun kerak
app_name = 'articles'

urlpatterns = [
    # 1. Bosh sahifa - Barcha maqolalar ro'yxati
    path('', views.article_list, name='article_list'),
    
    # 2. Maqola detali - Har bir maqolani slug orqali ochish
    # Masalan: /article/suvni-tejash-usullari/
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    
    # 3. Kategoriyalar - Maqolalarni turkumlar bo'yicha filtrlash
    # Masalan: /category/1/
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    
    # 4. Statik sahifalar - Biz haqimizda va Aloqa
    path('about/', views.about, name='about'),
]