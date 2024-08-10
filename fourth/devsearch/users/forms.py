from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message
from django.forms import ModelForm
from django import forms


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'bio', 'short_intro',
                  'profile_image', 'social_github', 'social_youtube',
                  'social_website']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})


class MessageForm(ModelForm):
    sender_ = forms.CharField(max_length=100)
    recipient_ = forms.CharField(max_length=100)

    class Meta:
        model = Message
        fields = ['sender_', 'recipient_', 'name', 'email', 'subject', 'body']
        labels = {
            'sender': 'Sender',
            'recipient': 'Recipient',
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'body': 'Body'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})


