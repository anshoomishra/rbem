from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import GroupForm
from notification.aws_sns import create_topic,subscribe_to_topic
def login(request):
    return HttpResponse("<h1> Trying to login </h1>")

class GroupCreateView(CreateView):
    form_class = GroupForm
    template_name = "account/create_group.html"
    success_url = "/"

    def form_valid(self, form):
        self.object = form.save(False)
        try:
            topic = create_topic(self.object.name)

        except Exception as e:
            print("Could not be created topic",str(e))
            return super().form_invalid(form)
        self.object.topic_arn = topic
        self.object.save()
        for person in form.cleaned_data['persons']:
            try:

                subscribe_to_topic(topic,str(person.phone_number))
            except Exception as e:
                print("Could not be created subscription",str(e))
        return super().form_valid(form)
