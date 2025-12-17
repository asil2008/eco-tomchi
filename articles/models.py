from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    # Fayl yuklash uchun (ixtiyoriy)
    featured_image = models.ImageField(upload_to='articles/', blank=True, null=True)
    # INTERNETDAN LINK QO'YISH UCHUN (ASOSIY):
    image_url = models.URLField(max_length=500, blank=True, null=True)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title