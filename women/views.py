from django.http import HttpResponse
from django.shortcuts import render


def index(request: HttpResponse):
    return HttpResponse("Страница приложения women")
