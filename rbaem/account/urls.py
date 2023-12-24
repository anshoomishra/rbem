from django.urls import path
from .views import login,GroupCreateView,test,UserCreateView,UserListView
app_name='account'
urlpatterns = [
    path("",GroupCreateView.as_view(),name="create-group"),
    path("user/",UserCreateView.as_view(),name="create-user"),
    path("users/",UserListView.as_view(),name="all-users"),
    path("test/",test)
]