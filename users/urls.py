from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('user/list', view=views.UserList.as_view(), name='user-list'),
    path('user/rud/<int:pk>', view=views.UserRetrieveUpdateDestroy.as_view(), name='user-rud')
]