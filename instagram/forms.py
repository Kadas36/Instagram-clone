from django import forms
from .models import Comment, Image



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