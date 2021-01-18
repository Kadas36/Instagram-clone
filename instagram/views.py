from typing import ContextManager
from instagram.models import Comment, Image, Profile
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    for image in all_images:
        if request.method == 'POST':
            form = commentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.image = image
                comment.editor = current_user
                comment.save()
                return redirect('home')
            else:
                form = commentForm()

    context = {
        'images' : all_images,
        'current_user' : current_user,
        'all_profiles': all_profiles,
        'all_comments': all_comments,
        'profile': user_profile,
        'form': form,
    }    
    return render(request, 'all_insta/home.html', context)


@login_required(login_url='/accounts/login/')
def new_post(request):
    form = postForm
    current_user = request.user
    all_profiles = Profile.objects.all()
    current_user_id = current_user.id
    current_user_profile = Profile.objects.filter(user_id = current_user_id)
    print(current_user_id)
    for profile in all_profiles:
        if current_user_id:
            if request.method == 'POST':
                form = postForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.user_key = current_user
                    post.profile_key = profile
                    post.save()
                    return redirect('home')
            else:
                form = postForm()

    context = {
        'current_user' : current_user,
        'new_post': form,
    }  

    return render(request, 'all_insta/new_post.html', context)  

        
