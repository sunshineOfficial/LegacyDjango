from django.shortcuts import render
from django.http import HttpResponse


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, pk):
    return HttpResponse(f'Подробно {pk}')
