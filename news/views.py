from django.shortcuts import render, get_object_or_404
from .models import News, NewsCategory, Album, Document, DocumentCategory


def news_list(request):
    category = request.GET.get('category', '')
    news_qs = News.objects.all()

    if category and category in NewsCategory.values:
        news_qs = news_qs.filter(category=category)

    return render(request, 'news/news_list.html', {
        'news_list': news_qs,
        'categories': NewsCategory.choices,
        'active_category': category,
    })


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.views += 1
    news.save(update_fields=['views'])

    return render(request, 'news/news_detail.html', {
        'news': news,
    })


def gallery_list(request):
    albums = Album.objects.all()
    return render(request, 'news/gallery_list.html', {
        'albums': albums,
    })


def gallery_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    images = album.images.all()
    return render(request, 'news/gallery_detail.html', {
        'album': album,
        'images': images,
    })


def document_list(request):
    category = request.GET.get('category', '')
    docs = Document.objects.all()

    if category and category in DocumentCategory.values:
        docs = docs.filter(category=category)

    return render(request, 'news/document_list.html', {
        'documents': docs,
        'categories': DocumentCategory.choices,
        'active_category': category,
    })
