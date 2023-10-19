from django.urls import path,include
from .views import users

urlpatterns = [
    path('', users, name='user'),
    path('group/', include('group.urls'))
]