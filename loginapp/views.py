from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name *'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email *'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Password *'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password *'}))
    is_active = False

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):

        cleaned_data = super().clean()
        if User.objects.filter(email=cleaned_data.get('email')).exists():
            self.add_error('email', 'такая почта уже зарегистрирована')
        return cleaned_data
# Create your views here.
def home(request):
    return render(request,'index.html')


def mainframe(request):
    return render(request,'mainframe.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request,'registration/register.html',{'form':form})

