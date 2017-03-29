from django.shortcuts import render, get_object_or_404

from events.forms import *
from .models import Event,userinfo,log
from django.shortcuts import render_to_response
from django.template import loader, RequestContext

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse,HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
# Create your views here.
@csrf_exempt
def list(request):

    list=Event.objects.all()
    context={"list":list,
    "title":"list"}
    return render(request, 'events/list.html', context)


@csrf_exempt
def detail(request):
    print 'hello'
    # list=get_object_or_404(Event, id=2)
    list=Event.objects.all()
    context={
    "list":list,
    "title":"events"
    }

    return render(request, 'events/detail.html', context)

@csrf_exempt
def create(request):

    form = EventForm(request.POST or None)

    if form.is_valid():

        instance=form.save(commit=False)
        instance.save()
        return render(request, 'events/detail.html', {})
    else:
        print "Invalid Form"
    context = {
          "form":form,
           }
    #print 'akshay'
    return render(request, 'events/create.html', context)

@csrf_exempt
def userprofile(request):
    form = user(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
    else:
        print ('invalid form')
    context = {
    "form":form,

    }
    return render(request,'events/userprofile.html',context)

@csrf_exempt
def login(request):
    form=login_page(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
    else:
        print ('Invalid login')

    context = {
    "form":form,
    }

    return render(request,'events/login.html',context)





@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect('events/list.html')
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('events/register.html',variables)
