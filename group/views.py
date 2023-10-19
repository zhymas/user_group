from django.http import JsonResponse
from django.shortcuts import render
from .models import Group


def groups(request):
    group = Group.objects.all()
    if group:
        return render(request, 'group/group.html')
    else:
        return JsonResponse({'error': 'groups does not exist'})
