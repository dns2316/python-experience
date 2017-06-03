from django.contrib import admin

from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields':['article_title']}),
        ('Body article info', {'fields':['pub_date','article_text']}),
    ]

admin.site.register(Article, ArticleAdmin)