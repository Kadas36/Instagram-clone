from django import forms
from .models import Image, Comment,Profile



class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['editor', 'pub_date', 'image']
        widgets = {
            'comment': forms.Textarea(
                attrs={'placeholder': 'add a comment', 'rows': 5}),
                
        }

class postForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date', 'comments', 'likes', 'profile_key', 'user_key']
        widgets = {
            'caption': forms.Textarea(
                attrs={'placeholder': 'add a caption', 'rows': 2}),
                
        }   

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'created', 'updated']
        widgets = {
            'bio': forms.Textarea(
                attrs={'placeholder': 'add bio', 'rows': 2}),
                
        }                  