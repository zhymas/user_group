from django.urls import path,include
from .views import users, create_user

urlpatterns = [
    path('', users, name='user'),
    path('create_user/', create_user, name='create_user'),
    path('group/', include('group.urls')),
]
