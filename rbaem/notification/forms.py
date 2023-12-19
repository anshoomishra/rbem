from django.forms import ModelForm
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title','text','receiver']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["text"].widget.attrs.update({"class": "form-control"})
        self.fields["receiver"].widget.attrs.update({"class": "form-control"})
