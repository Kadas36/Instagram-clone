from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime as dt
from django.forms.widgets import Textarea

# Create your models here.

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True)
    bio = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    username = models.CharField(max_length=15, default='User')
    
    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
 
    def update_profile(self,new_profile):
        self.profile_pic = new_profile.profile_pic
        self.bio = new_profile.bio
        self.username = new_profile.username
        self.save()      

        
class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=15)
    caption = models.TextField(blank=True)
    profile_key = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    user_key = models.ForeignKey(User,on_delete= models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self,new_caption):
        self.image_caption = new_caption
        self.save()

    def likes_count(self):
        total_likes = self.likes.count()
        return total_likes


class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)  

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


