from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Главная приложения posts.')


def group_posts(request, slug):
    return HttpResponse(f'Новость про {slug}')
