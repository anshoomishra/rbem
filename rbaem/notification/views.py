from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .forms import MessageForm
from account.models import AssemblyUserGroup
from notification.aws_sns import send_message_to_topic
def send_message(request):
    pass

class SendMessageView(CreateView):
    template_name = "notification/send_message.html"
    form_class = MessageForm
    success_url = "/"

    def form_valid(self, form):
        object = form.save()
        for group in form.cleaned_data['receiver']:
            try:
                grp = AssemblyUserGroup.objects.get(name=group.name)
                topic = grp.topic_arn
                if topic:
                    message_id = send_message_to_topic(topic, object.text)
            except Exception as e:
                print("Could not be created subscription", str(e))
                return super().form_invalid(form)
        print(message_id)

        return super().form_valid(form)





