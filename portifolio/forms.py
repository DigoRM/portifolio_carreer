from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Project, Update, Customer

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['updated_at','added_at','updates',]

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        exclude = ['updated_at','added_at','project',]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists, try another one...")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        field_order = ['profile_pic', 'name', 'company','role','skills','interests']


        widgets = {
        'profile_pic': forms.ClearableFileInput(attrs={'class':'button is-rounded is-centered mb-3','style':'max-width:95%'}),

        'name': forms.TextInput(attrs={ 'class': 'input is-success is-rounded is-flex mb-5', 'placeholder': 'Name','style':'max-width:100%'}),
        'company': forms.TextInput(attrs={ 'class': 'input is-success is-rounded is-flex mb-5', 'placeholder': 'Company','style':'max-width:100%'}),
        'role': forms.TextInput(attrs={ 'class': 'input is-success is-rounded is-flex mb-5', 'placeholder': 'Role','style':'max-width:100%'}),
        'skills': forms.Textarea(attrs={'rows': 6, 'cols': 50, 'placeholder': 'Write your main skills today:', 'class': 'input textarea mb-5 is-flex','style':'max-width:100%'}),
        'interests': forms.Textarea(attrs={'rows': 6, 'cols': 50, 'placeholder': 'Write the skill you want to learn:', 'class': 'input textarea mb-5 is-flex','style':'max-width:100%'}),
    }
        labels={
            'profile_pic':'',
            'name': 'Name',
            'company': 'Company',
            'role': 'Role',


        }
               
class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email address must be unique')
        return email
