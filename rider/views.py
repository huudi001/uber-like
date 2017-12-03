from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import CabDriver, CabDriverProfile, Rider, RiderProfile, DriverReview
from .forms import NewDriver, DriverLogin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

def index(request):
    '''
    View function for the landing page of the application
    '''
    title = 'CarPoolers'
    message = 'Landing Page'
    return render(request,'index.html',{"title":title,"message":message})

def new_driver(request):

    title = 'cab signup'

    if request.method == 'POST':

        form = NewDriver(request.POST)

        if form.is_valid:

            first_name = request.POST.get('first_name')

            last_name = request.POST.get('last_name')

            phone_number = request.POST.get('phone_number')

            new_driver = CabDriver(first_name=first_name, last_name=last_name, phone_number=phone_number)
