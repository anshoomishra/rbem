from django.urls import path
from .views import login,GroupCreateView
urlpatterns = [
    path("",GroupCreateView.as_view(),name="create-group"),
]