from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'code': 100, 'url': '/accounts/dashboard'})
        else:
            return JsonResponse({'code': 101, 'error': 'Invalid credential'})
    return render(request, 'accounts/login.html')

@login_required(login_url='accounts:login')
def dashboard(request):
    user_contacts = Contact.objects.filter(user_id=request.user.id)
    context ={'user_contacts':user_contacts}
    if 'message' in request.GET:
        context['message']=request.GET['message']
    return render(request, 'accounts/dashboard.html',context)


def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['password2']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'code': 101, 'error': 'That username is taken.'})
            else:
                if User.objects.filter(email=email).exists():
                    return JsonResponse({'code': 101, 'error': 'That emial  being used.'})
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    return JsonResponse({'code': 100, 'url': '/'})

        else:
            return JsonResponse({'code': 101, 'error': 'Password do not match'})
    else:
        return render(request, 'accounts/register.html')

@login_required(login_url='accounts:login')
def logout(request):
    auth.logout(request)
    return redirect('pages:index')

