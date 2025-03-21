from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=10, required=True, help_text='Required. 10 characters or fewer.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')