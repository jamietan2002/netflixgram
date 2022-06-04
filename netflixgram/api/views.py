from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ReviewForm
from django.views import generic
from rest_framework.response import Response

# Create your views here.
def data(request):
    form = ReviewForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            my_review = form.save(commit=False)
            my_review.user = request.user
            my_review.save()
            return redirect("my_watchlist")
    return render(request, "data.html", {"form": form})
    
def my_watchlist(request): 
    form = ReviewForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            my_review = form.save(commit=False)
            my_review.user = request.user
            my_review.save()
            return redirect("my_watchlist")
    return render(request, "my_watchlist.html", {"form": form})

def index(request):
    return render(request, "index.html")

def my_network(request):
    user = request.user.profile
    return render(request, "my_network.html", {"user": user})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "pages/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    
    return render(request, "pages/profile.html", {"profile": profile})
