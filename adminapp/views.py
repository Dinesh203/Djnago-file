from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm


# Create your views here.

#New Data

def blogpost(request):
    post = Post.objects.all()
    return render(request, "adminapp/blogpost.html", {'Post': post})


def addblog(request):
    addblog = PostForm()
    if request.method == "POST":
        blogfield = PostForm(request.POST, request.FILES)
        print(request.FILES)
        if blogfield.is_valid():
            blogfield.save()
            messages.success(request, "Blog added successfully!")
            return redirect('blogpost')
    else:
        paddblog = PostForm()
    return render(request, "adminapp/addblog.html", {'addblog': addblog})


def deleteblog(request, id):
    delblog = Post.objects.get(id=id)
    delblog.delete()
    return redirect('blogpost')

# def updateblog(request):
#     if request.method=="POST":  
#         pass
#     else:

#         obj=SignUp.objects.get(email=email)
#         id=obj.id
#         return render(request, 'update.html',{'id':id})
