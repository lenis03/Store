from django.shortcuts import render
from django.http import HttpResponse


def store(request):
    return HttpResponse('Wellcome To Store...')


def hello_world(request):
    return HttpResponse('HelloWorld!')


def get_num(request, num):
    return HttpResponse(f'Your num: {num}')
