from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from datetime import datetime
from iBlog.models import CreateBlogPost

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/')
    return render(request,'index.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username= username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'index.html')
            # A backend authenticated the 
        else:
            return render(request,'login.html')
       
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('regusername')
        password = request.POST.get('regpassword')
        institute = request.POST.get('institute')
        user = User.objects.create_user(username = username, password = password, first_name = institute )
        user.save()
    return render(request,'signup.html')

# def blogpost(request):
#     return render(request,'blog.html')

def createpost(request):
    if request.method == 'POST':
        Author = request.POST.get('author')
        blogtitle = request.POST.get('blogtitle')
        desc = request.POST.get('desc')
        createblogpost = CreateBlogPost(Author=Author , blogtitle = blogtitle,desc = desc, date = datetime.today())
        createblogpost.save()
        return redirect('/index')
    return render(request,'createpost.html')

def profile(request):
    data = CreateBlogPost.objects.all()
    content = {
        'post_number' : data
    }
    return render(request,'profile.html',content)