from django import forms
from .models import *

  
class UserForm(forms.ModelForm):
  
    class Meta:
        model = Name
        fields = ['Username']

        widgets = {
            'Username': forms.TextInput(attrs={'class':'form-control'})
        }

class addQuestionform(forms.ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"