from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SignUp
from adminapp.models import Post
from .forms import SignUpForm


# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, "adminapp/blogpost.html", {'Post': post})
    # return render(request, "userapp/home.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            message = messages.success(request, 'Created User successfully')
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "userapp/signup_login.html", {'form': form})


def login(request):
    if request.method == 'POST':
        email1 = request.POST['email']
        password1 = request.POST['password']

        if SignUp.objects.filter(email=email1, password=password1).exists():
            em = SignUp.objects.get(email=email1)
            request.session['email'] = email1
            return redirect('getuser')
        else:
            msg = "invalid input please try again"
            print(msg)
            return render(request, 'userapp/signup_login.html', {'mssg': msg})
    else:
        return render(request, 'userapp/login.html')


def getuser(request):
    email_id = request.session['email']
    obj = SignUp.objects.filter(email=email_id)
    for data in obj:
        name = data.name
        if name:
            userblog = Post.objects.filter(user_id=data)
            content = {'user_id': userblog,
                       'name': data.name}
            return render(request, 'userapp/userprofile.html', content)
        # return None
        else:
            messages.WARNING("user id not match")
            return render(request, "userapp/userprofile.html")

    # email1 = SignUp.objects.get(pk=object_id)
    # return redirect("home", {'email':email})

# def update(request):
#     if request.method=="POST":
#         pass
#     else:

#         email=request.session['email']
#         obj=SignUp.objects.get(email=email)
#         id=obj.id
#         return render(request, 'update.html',{'id':id})
