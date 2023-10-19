from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
from .forms import UserForm


def users(request):
    user = UserProfile.objects.all()
    if user:
        return render(request, 'user/users.html', {'users': user})
    else:
        return JsonResponse({'error': 'users does not exists'})


@csrf_exempt
def create_user(request):
    form = UserForm
    if request.method == 'POST':
        return JsonResponse({'request method': f'{request.method}'})
    return render(request, 'user/create_user.html', {'form': form})

