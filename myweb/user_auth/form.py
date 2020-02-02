from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class RegisterationFrom(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last Name'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email'}))

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(RegisterationFrom,self).__init__(*args,**kwargs)
        self.fields['username'].widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'})
        self.fields['username'].help_text=''
        self.fields['password1'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password','type':'password'})
        self.fields['password1'].help_text = ''
        self.fields['password2'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password','type':'password'})
        self.fields['password2'].help_text = ''

class EditInfoForm(UserChangeForm):
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'email'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')
    def __init__(self,*args,**kwargs):
        super(EditInfoForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget=forms.TextInput(attrs={'class':'form-control'})
        self.fields['username'].help_text=''