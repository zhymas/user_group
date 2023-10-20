from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
from .forms import UserForm
from django.views.generic import UpdateView

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


def edit_user(request, pk):
    user = UserProfile.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'user/edit_client.html', context)


class UserUpdate(UpdateView):
    model = UserProfile
    template_name = 'user/update_client.html'

    form_class = UserForm


def delete_user(request, pk):
    user = UserProfile.objects.get(pk=pk)
    user.delete()
    return redirect('user')

