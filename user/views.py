from django.http import JsonResponse
from django.shortcuts import render
from .models import User


def users(request):
    user = User.objects.all()
    if user:
        return render(request, 'user/base.html', {'users': user})
    else:
        return JsonResponse({'error': 'users does not exists'})

