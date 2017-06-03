from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.template import RequestContext, loader
# from django.http import Http404

from .models import Article


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'fresh_article_list'

    def get_queryset(self):
        """Return the last five published articles"""
        return Article.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailArticle(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'
    def get_queryset(self):
        return Article.objects.filter(pub_date__lte <= timezone.now())

def post_article(request):
    article = Article.objects.create(
        article_title = request.POST['article_title'],
        article_text = request.POST['article_text'],
    )
    return render(request, 'blog/article.html', { 'article':article })
