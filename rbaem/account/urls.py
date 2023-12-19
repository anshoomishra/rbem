from django.urls import path
from .views import login,GroupCreateView,test
app_name='account'
urlpatterns = [
    path("",GroupCreateView.as_view(),name="create-group"),
    path("test/",test)
]