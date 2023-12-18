from account.models import AssemblyUserGroup
from django.forms import ModelForm
class GroupForm(ModelForm):
    class Meta:
        model = AssemblyUserGroup
        fields = '__all__'
