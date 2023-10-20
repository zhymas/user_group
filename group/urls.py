from django.urls import path
from .views import groups, create_group, UpdateGroup, edit_group, delete_group

urlpatterns = [
    path('', groups, name='group'),
    path('create/', create_group, name='create_group'),
    path('<int:pk>/edit_group', edit_group, name='edit_group'),
    path('<int:pk>/update', UpdateGroup.as_view(), name='update_group'),
    path('<int:pk>/delete', delete_group, name='delete_group')
]