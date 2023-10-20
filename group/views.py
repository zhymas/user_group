from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Group
from .forms import GroupForm
from django.views.decorators.csrf import csrf_exempt


def groups(request):
    group = Group.objects.all()

    return render(request, 'group/group.html', {'groups': group})


@csrf_exempt
def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = GroupForm()

    return render(request, 'group/create_group.html', {'form': form})
