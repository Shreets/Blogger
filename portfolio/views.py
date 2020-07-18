from django.db import IntegrityError
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
from portfolio.forms import SignUpForm, CreateBlogForm
from blog.models import Blog


def signupuser(request):
    context = {'form': SignUpForm()}
    if request.method == 'GET':
        return render(request, 'portfolio/signup.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('authorhome')
            except IntegrityError:
                context = {'form': SignUpForm(), 'error': ' The username already exists. Please try again!'}
                return render(request, 'portfolio/signup.html', context)
        else:
            context = {'form': SignUpForm(), 'error': ' The passwords do not match. Try again!'}
            return render(request, 'portfolio/signup.html', context)


def loginuser(request):
    context = {'form': AuthenticationForm()}
    if request.method == 'GET':
        return render(request, 'portfolio/login.html', context)
    else:
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        if user is None:
            context = {'form': AuthenticationForm(), 'error': 'The username or password did not match'}
            return render(request, 'portfolio/login.html', context)
        else:
            login(request, user)
            return redirect('authorhome')


def logoutuser(request):
    if request.method == 'POST':
           logout(request)
           return redirect('home')


def authorhome(request):
    blog = Blog.objects.filter(author=request.user).order_by('-date_created')
    context = {'blogs': blog}
    return render(request, 'portfolio/author_home.html', context)


def home(request):
    return render(request,'portfolio/home.html')

def createblog(request):
    context = {'form': CreateBlogForm(initial={'author': request.user})}
    if request.method == 'GET':
        return render(request, 'portfolio/create_blog.html', context)
    else:
        form = CreateBlogForm(request.POST)
        form.save()
        return redirect('authorhome')


def updateblog(request, pk):
    blog = get_object_or_404(Blog, id=pk, author=request.user)
    if request.method == 'GET':
        form = CreateBlogForm(instance=blog)
        return render(request, 'portfolio/create_blog.html', {'form': form})
    if request.method == 'POST':
        blog.date_updated = timezone.now()
        blog.save()
        form = CreateBlogForm(request.POST, instance=blog)
        form.save()
        return redirect('authorhome')



def deleteblog(request,pk):
    blog = Blog.objects.filter(id=pk, author=request.user)
    if request.method == 'GET':
        blog.delete()
        return redirect('authorhome')

