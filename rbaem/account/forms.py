from account.models import AssemblyUserGroup
from django.forms import ModelForm
class GroupForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["persons"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = AssemblyUserGroup
        fields = ['name','persons']

