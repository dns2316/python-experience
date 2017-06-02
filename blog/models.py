from django.db import models

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=150)
    article_text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.article_title