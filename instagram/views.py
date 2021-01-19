from typing import ContextManager
from instagram.models import Image, Profile, Comment
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import postForm, commentForm
from django.urls import reverse
from django.http import HttpResponseRedirect




# Create your views here.

@login_required(login_url='/accounts/login/')
def insta_home(request):
    all_images = Image.objects.all()
    all_profiles = Profile.objects.all()
    current_user = request.user
    user_profile = Profile.objects.filter(user=current_user)
    all_comments = Comment.objects.all()

    context = {
        'images' : all_images,
        'current_user' : current_user,
        'all_profiles': all_profiles,
        'profile': user_profile,
        'all_comments': all_comments
    }    
    return render(request, 'all_insta/home.html', context)

@login_required(login_url='/accounts/login/')
def Commentview(request, image_id):
    form = commentForm()
    image = get_object_or_404(Image, id=image_id)
    current_user = request.user
    image_comments = Comment.objects.filter(image=image_id)

    print(image)

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
        "image": image,
        "form": form,
        'image_comments': image_comments
    }
    return render(request, 'all_insta/comment.html', context)    

@login_required(login_url='/accounts/login/')
def new_post(request):
    form = postForm
    current_user = request.user
    all_profiles = Profile.objects.all()
    all_comments = Comment.objects.all()
    current_user_id = current_user.id
    
    images = Image.objects.filter(user_key_id = current_user_id)
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

    print(images)            

    context = {
        'current_user' : current_user,
        'new_post': form,
        'images': images,
        'all_comments': all_comments
    }  

    return render(request, 'all_insta/new_post.html', context) 


def Likeview(request,pk):
    image = get_object_or_404(Image, id=request.POST.get('image_id'))
    image.likes = image.likes + 1
    image.save()
    return HttpResponseRedirect(reverse('home'))



  

           
    


        
