from typing import ContextManager
from instagram.models import Comment, Image, Profile
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import commentForm, postForm




# Create your views here.

@login_required(login_url='/accounts/login/')
def insta_home(request):
    current_user = request.user
    all_images = Image.objects.all()
    all_comments = Comment.objects.all()
    all_profiles = Profile.objects.all()
    user_profile = Profile.objects.filter(user=current_user)
    form = commentForm

    # comments = []
    # for image in all_images:
    #     for comment in all_comments:
    #         if comment.image_id == image.id:
    #             comment
               
    #         comments += comment

    context = {
        'images' : all_images,
        'current_user' : current_user,
        'all_profiles': all_profiles,
        'all_comments': all_comments,
        'profile': user_profile,
        'form': form,
    }    
    return render(request, 'all_insta/home.html', context)


def new_post(request):

    form = postForm
    current_user = request.user
    all_profiles = Profile.objects.all()
    for profile in all_profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = postForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.user_key = current_user.id
                    post.profile_key = profile.id
                    post.save()
                    return redirect('home')
            else:
                form = postForm()

        context = {
            'current_user' : current_user,
            'new_post': form,
        }  

    return render(request, 'all_insta/new_post.html', {'current_user' : current_user, 'new_post': form})

        
