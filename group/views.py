from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .models import Group
from .forms import GroupForm
from django.views.decorators.csrf import csrf_exempt


def groups(request):
    group = Group.objects.all()
    context = {
        'groups': group,
    }
    return render(request, 'group/group.html', context)


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


class UpdateGroup(UpdateView):
    model = Group
    template_name = 'group/group_update.html'

    form_class = GroupForm


def edit_group(request, pk):
    group = Group.objects.get(pk=pk)
    context = {
        'group': group
    }
    return render(request, 'group/edit_group.html', context)


def delete_group(request, pk):
    group = Group.objects.get(pk=pk)
    if group.users.count() != 0:
        return JsonResponse({'Error': 'cant delete this group, group has members'})
    else:
        group.delete()
        return redirect('group')

