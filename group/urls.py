from django.urls import path
from .views import groups, create_group

urlpatterns = [
    path('', groups, name='group'),
    path('create/', create_group, name='create_group')
]