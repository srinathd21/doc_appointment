from django import forms
from .models import UserProfile


class MyForm(forms.Form):
    def __init__(self, *args, my_variable=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_variable = my_variable
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['pid','doctor','name','fh', 'age', 'contact', 'gender', 'description']
