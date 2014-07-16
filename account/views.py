from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect

# Create your views here.


@login_required(login_url='/account/login/')
def account(request):
    if request.user.is_authenticated():
        # Do something for authenticated users.
        return render(request, 'account/account.html', {'user': request.user})
    else:
        return HttpResponseRedirect('/account/login/')


def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    if request.method == 'POST':
        u = request.POST['username']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        e = request.POST['email']
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        if p1 != p2:
            return render(request, 'account/error.html', {'error': 'Password were not the same'})
        request.session.flush()
        user = User.objects.create_user(u, e, p1)
        user.first_name = fn
        user.last_name = ln
        user.is_active = True
        user.save()
        user = authenticate(username=u, password=p1)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/account/')

def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def do_login(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        request.session.flush()
        user = authenticate(username=u, password=p)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/account/')



def order(request):
    pass


def order_detail(request):
    pass
