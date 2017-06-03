from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=150)
    article_text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def set_hidden_data_in_future(self):
        feature = timezone.now() + datetime.timedelta(hours=1)
        if self.pub_date < feature:
            self.hidden = True
        else:
            self.hidden = False