from django.shortcuts import get_object_or_404, render
from django.views import View
from articles.models import Article
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
