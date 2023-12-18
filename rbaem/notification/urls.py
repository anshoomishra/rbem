from django.urls import path
from .views import send_message,SendMessageView
urlpatterns = [
    path("",SendMessageView.as_view(),name="create-message"),
]