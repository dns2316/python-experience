from django.test import TestCase

import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Article

# Create your tests here.

def create_article(title, text, days, hidden=False):
    time = timezone.now() + datetime.timedelta(days=days)
    return Article.objects.create(
        article_title = title,
        article_text = text,
        pub_date = time,
        hidden = hidden,
    )

class ArticleMethodTests(TestCase):
    def test_detail_article_with_a_future_date(self):
        article_future = create_article(
            title='Hello from test FUTURE',
            text='this text did writed for test',
            days=5,
        )
        response = self.client.get(reverse('blog:detail', args=(article_future.id)))
        self.assertEqual(response.status_code, 404)

    def test_detail_article_with_a_past_date(self):
        article_past = create_article(
            title='Hello from test PAST',
            text='this text did writed for test',
            days=-5,
        )
        response = self.client.get(reverse('blog:detail', args=(article_past.id)))
        self.assertContains(response, article_past.text, status_code=200)

    def test_send_empty_article(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['fresh_article_list'], [])

    def test_send_article_with_past_time_date(self):
        create_article(
            title = 'Hello from test',
            text = 'this text did writed for test',
            days=-30,
        )
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['fresh_article_list'],
            ['<Article: Hello from test>']
        )

    def test_was_published_in_future(self):
        time = timezone.now() + datetime.timedelta(hours=1)
        article_future = Article(pub_date=time)
        self.assertEqual(article_future.was_published_recently(), False)

    def test_was_published_old(self):
        time = timezone.now() - datetime.timedelta(days=30)
        article_old = Article(pub_date=time)
        self.assertEqual(article_old.was_published_recently(), False)

    def test_was_published_recent(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        article_recent = Article(pub_date=time)
        self.assertEqual(article_recent.was_published_recently(), True)