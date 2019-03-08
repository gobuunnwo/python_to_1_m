from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
# Create your views here.


# Post
def home(request):
    # context変数を使うと、postsリストを活用できる
    context={
        "posts":Post.objects.all()
    }
    return render(request,'newapp/home.html',context)

def about(request):
    return render(request,'newapp/about.html')

def contact(request):
    return render(request,'newapp/contact.html')