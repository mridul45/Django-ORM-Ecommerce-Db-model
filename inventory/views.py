from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("age", "nickname")

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect("user:profile")
    else:
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "profile.html", {"u_form":user_form, "p_form": user_profile_form})

# Create your views here.
def index(request):
	objs = Product.objects.all()
	paginator = Paginator(objs,8)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {"page_obj":page_obj}

	return render(request,"index.html")