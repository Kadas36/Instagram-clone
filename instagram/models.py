from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime as dt
from django.forms.widgets import Textarea
from cloudinary.models import  CloudinaryField

# Create your models here.

class Profile(models.Model):
    profile_pic = CloudinaryField('image', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(default="No Bio.. ")
    username = models.CharField(max_length=15, default='User')
    following = models.ManyToManyField(User, related_name='following', blank=True )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-created',) 
    
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
    image = CloudinaryField('image', null=True)
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
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
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





          


