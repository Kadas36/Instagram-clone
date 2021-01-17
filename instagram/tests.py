from django.contrib.auth.forms import UsernameField
from django.test import TestCase
from .models import Image,Comment,Friend,Profile,User

# Create your tests here.

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        User.james= Profile(user = 'james')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Profile))  

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)       
