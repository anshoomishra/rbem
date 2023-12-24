from account.models import AssemblyUserGroup,AssemblyUser
from django import forms
class GroupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["persons"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = AssemblyUserGroup
        fields = ['name','persons']


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["first_name"].widget.attrs.update({"class": "form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
        self.fields["password"].widget.attrs.update({"class": "form-control"})
        self.fields["booth_name"].widget.attrs.update({"class": "form-control"})
        self.fields["phone_number"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = AssemblyUser
        fields = ['username','first_name','last_name','password','booth_name','phone_number']

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)