from django.shortcuts import render


def index(request):
    return render(request, 'document.html', context={'title': 'Document of DRM Starter'})
