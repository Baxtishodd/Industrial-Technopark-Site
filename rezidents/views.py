from django.shortcuts import render


def rezidents_list(request):
    return render(request, 'rezidents/rezidents_list.html')
