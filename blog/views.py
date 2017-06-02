from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.template import RequestContext, loader
# from django.http import Http404

from .models import Article


# Create your views here.
def index(request):
    fresh_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {
        'fresh_article_list': fresh_article_list,
    }
    return render(request, 'blog/index.html', context)


def detail_article(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'blog/article.html', { 'article':article })

def post_article(request):
    article = get_object_or_404(Article)
    try:
        article.article_title.get(pk = request.POST['article_title'])
        article.article_text.get(pk = request.POST['article_text'])
    except (KeyError, Article.DoesNotExist):
        return render(request, 'blog/')
    else:
        article.save()
        return HttpResponseRedirect(reverse('blog:index', args=(article.id)))