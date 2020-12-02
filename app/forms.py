from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']