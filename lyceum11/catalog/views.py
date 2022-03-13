from django.shortcuts import render
from django.http import HttpResponse


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, id):
    return HttpResponse(f'Подробно {id}')
