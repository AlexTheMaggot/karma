from django.shortcuts import render


def index(request):
    if '/ru/' in request.path:
        template = 'mainapp/index_ru.html'
    else:
        template = 'mainapp/index.html'
    return render(request, template)
