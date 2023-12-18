from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .forms import MessageForm
from notification.aws_sns import create_topic
def send_message(request):
    pass

class SendMessageView(CreateView):
    template_name = "notification/send_message.html"
    form_class = MessageForm
    success_url = "/"




