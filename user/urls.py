from django.urls import path,include
from .views import users, create_user, UserUpdate, edit_user, delete_user

urlpatterns = [
    path('', users, name='user'),
    path('create_user/', create_user, name='create_user'),
    path('<int:pk>/edit_user', edit_user, name='edit_user'),
    path('<int:pk>/update_user', UserUpdate.as_view(), name='user_update'),
    path('<int:pk>/delete_user', delete_user, name='user_delete'),
    path('group/', include('group.urls')),
]
