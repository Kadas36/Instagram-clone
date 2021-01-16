from django.shortcuts import render

# Create your views here.

def insta_home(request):
    return render(request, 'all_insta/home.html')
