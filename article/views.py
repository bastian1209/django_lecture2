from django.shortcuts import render, redirect
from article.models import Article
from django.urls import reverse


# Create your views here.


def list_article(request):
    articles = Article.objects.all()
    data = {
        'articles': articles
    }
    return render(request, 'list.html', data)


def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    data = {
        'article': article
    }
    return render(request, 'detail.html', data)


# @csrf_exempt
def create_article(request):
    # 이 조건이 없으면 페이지에 처음 들어갈 때 request의 method가 get이기 때문에 request에 'content'키가 없기 때문에 에러가 뜬다
    if request.method == 'POST':
        title = request.POST.get('title', None)  # key가 없으면 none을 리턴
        content = request.POST['content']  # key가 없으면 바로 에러뜸
        # 바로 article생성을 할 수 있음
        article = Article.objects.create(
            title=title,
            content=content
        )
        return redirect(reverse('list')) #다른 url로 가게 해주는것
    return render(request, 'create.html')
