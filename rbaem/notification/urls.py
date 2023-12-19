from django.urls import path
from .views import send_message,SendMessageView
app_name="notification"
urlpatterns = [
    path("",SendMessageView.as_view(),name="create-message"),
]