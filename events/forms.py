from .models import Event,userinfo, log
from django.forms import ModelForm
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields=('event_name', 'date_time', 'duration', 'address')





class RegistrationForm(forms.Form):#for Registration of new user
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password',
                          widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)',
                        widget=forms.PasswordInput())

    def clean_password2(self):#to check password and again password is same or not
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')



class user(ModelForm):
    class Meta:
        model = userinfo
        fields = ('firstname','lastname','dob','gender','country','state','city')

class login_page(ModelForm):
    class Meta:
        model = log
        fields = ('email','password')      
