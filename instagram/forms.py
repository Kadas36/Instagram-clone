from django import forms
from .models import Comment, Image



class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['editor', 'pub_date']
        widgets = {
            'comment': forms.Textarea(
                attrs={'placeholder': 'add a comment', 'cols': 1000, 'rows': 1}),
                
        }

class postForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date', 'comments', 'likes', 'profile_key']
        widgets = {
            'caption': forms.Textarea(
                attrs={'placeholder': 'add a caption', 'cols': 100, 'rows': 1}),
                
        }        