from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


articles = [
    {'id': 1, 'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'id': 2, 'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'id': 3, 'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'id': 4, 'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'id': 5, 'title': '"5 min recepies"', 'author': 'H. Lector'},
]


@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        article = {
            'id': int(request.POST['id']),
            'title': request.POST['title'],
            'author': request.POST['author']
        }
        articles.append(article)
    return render(request, 'articles/index.html', context={'articles': articles})

# BEGIN (write your solution here)
@require_http_methods(['GET'])
def get_article_by_id(article_id):
    pass
# END
