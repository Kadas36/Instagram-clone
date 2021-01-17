from instagram.models import Profile
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import commentForm, postForm




# Create your views here.

@login_required(login_url='/accounts/login/')
def insta_home(request):
    current_user = request.user
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.editor = current_user
            comment.save()
        return redirect('home')

    else:
        form = commentForm()
    return render(request, 'all_insta/home.html', {"form": form})


def new_post(request):
    current_user = request.user
    profile = Profile.objects.filter(user = current_user.id)
    
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile_key = profile.id
            image.user = current_user.id
            image.save()
        return redirect('home') 

    else:
        form = postForm()

    return render(request, 'all_insta/new_post.html', {"new_post": form})
