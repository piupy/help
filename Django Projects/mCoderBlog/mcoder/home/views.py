from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def home(request):
    # print(request.user.is_authenticated)
    # print(request.user)
    return render(request,"home/home.html")



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        content = request.POST.get('content')
        if len(name) == 0 or len(phone) == 0 or len(email) == 0 or len(content.strip()) == 0:
            messages.error(request,'Please fill the details correctly')
        else:
            contact = Contact(name=name, phone=phone, email=email, content=content)
            contact.save()
            messages.success(request, 'Message submitted successfully')
        return render(request, "home/contact.html")

    else:
        return render(request, "home/contact.html")


def about(request):
    messages.info(request, 'Welcome to About')
    return render(request,"home/about.html")



def search(request):
    if request.method == "POST":
        query = request.POST.get('search','')
        if len(query) > 50:
            allPosts = Post.objects.none()
        else:   
            titlePosts = Post.objects.filter(title__icontains=query)
            contentPosts = Post.objects.filter(content__icontains=query)
            authorPosts = Post.objects.filter(author__icontains=query)
            allPosts = authorPosts.union(titlePosts.union(contentPosts))
            params = {
                'allPosts' : allPosts,
                'query' : query
            }
    else:
        params = {}
    return render(request,'home/search.html',params)




def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        email = request.POST.get('email','')
        username = request.POST.get('username','')
        pass1 = request.POST.get('pass1','')
        pass2 = request.POST.get('pass2','')

        if len(username) < 6:
            messages.error(request, 'Username must have atleast 6 characters')
            return redirect('home')
        elif not username.isalnum():
            messages.error(request, 'Username can only have alphabets and numbers')
            return redirect('home')
        elif pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('home')
        else:
            myuser = User.objects.create_user(username=username,email=email,password=pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request,'Your mcoder account has been created successfully')
            return redirect('home')

    else:    
        return HttpResponse('404 - Not Found')



def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername','')
        loginpassword = request.POST.get('loginpassword', '')

        myuser = authenticate(username=loginusername,password=loginpassword)
        if myuser is not None :
            login(request,myuser)
            messages.success(request,'Logged in')
        else:
            messages.error(request, 'Invalid credentials')
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')



def handleLogout(request):
    logout(request)
    messages.success(request,'Logged out')
    return redirect('home')


