from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
from .forms import UserForm


def users(request):
    user = UserProfile.objects.all()
    return render(request, 'user/users.html', {'users': user})


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = UserForm()
    return render(request, 'user/create_user.html', {'form': form})


