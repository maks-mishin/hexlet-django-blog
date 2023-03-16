from django.shortcuts import get_object_or_404, render
from django.views import View

from .forms import ArticleForm
from .models import Article
from django.db.models import Q


class IndexView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        articles = Article.objects.filter(Q(title__icontains=query))
        return render(
            request,
            'articles/index.html',
            context={
                'articles': articles,
                'query': query,
                }
            )


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
        })


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})