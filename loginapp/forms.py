from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .models import Post
class RegisterForm(forms.Form):
    username = forms.CharField(label=u"Имя пользователя")
    first_name = forms.CharField(label=u"Имя")
    last_name = forms.CharField(label=u"Фамилия")
    email = forms.EmailField(label=u"Email", required=False)
    password = forms.CharField(label=u"Пароль", widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            self.add_error("password_confirm", u"Пароли не совпадают")
            return False
        return valid


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

