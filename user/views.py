from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return JsonResponse({'success': 'home page'})
