from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
	objs = Product.objects.all()
	context = {"objs":objs}

	return render(request,"index.html")