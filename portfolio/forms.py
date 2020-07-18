from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.models import Blog

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = User
        fields = ('username','email')


class CreateBlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ('title','author','tag', 'image','body')