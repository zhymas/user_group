from django.urls import path
from .views import groups

urlpatterns = [
    path('', groups, name='group')
]