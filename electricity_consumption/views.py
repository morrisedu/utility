from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model

from datetime import date, time, datetime
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


# from django.contrib.auth import login, authenticate, get_user_model, logout
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
# from django.urls import reverse

# Developer created
from .models import *

# Create your views here.

def index(request):
    title = "My Utilities"

    # Constants
    costPU = CostPerUnit.objects.get(id=1)

    try:
        previousUnits = Electricity.objects.latest("id")
    except ObjectDoesNotExist:
        previousUnits = None
    
    previous_readings = Electricity.objects.all()
    labels = []
    datas = []
    
    reversed_prev = previous_readings.reverse()

    for reading in previous_readings:
        labels.append(str(reading.inputDate.strftime("%b")))
        datas.append(float(reading.unitsUsed))

    context = {
            "title": title,
            "previousUnits": previousUnits,
            "costPU": costPU,
            "previous_readings": reversed_prev,
            "labels": json.dumps(labels),
            "datas": json.dumps(datas),
        }
        

    return render(request, "index.html", context)

def readingInput(request):
    try:
        previous_units = Electricity.objects.latest("id")
    except ObjectDoesNotExist:
        previous_units = None
    
    # Constants
    cost_per_unit = CostPerUnit.objects.get(id=1)

    # Form to add unit reading
    if request.method == "POST":
        current_reading = request.POST.get('units_used')
        entry_date = date.today().strftime('%d-%m-%Y')
        entry_time = datetime.now().time().strftime('%H:%M:%S')
        if previous_units is None:
            units_used = 0
            cost_of_units = 0
            messages.error(request, "Add units")
        else:
            units_used = float(current_reading) - int(previous_units.reading)
            cost_of_units = units_used * int(cost_per_unit.unitCost)

        month_reading = Electricity(inputDate = entry_date, inputTime = entry_time, reading = current_reading, unitsUsed = units_used, unitsCost = cost_of_units)

        month_reading.save()
        
        messages.success(request, "Reading Added!")
        
        resp = {
            "status": "created",
            }
        
        return JsonResponse(resp)

def deleteUnit(request, uid):
    reading = Electricity.objects.filter(id = uid)
    reading.delete()
    messages.warning(request, "Deleted")        

    return redirect("/")

def getReadings(request):
    readings = Electricity.objects.all()
    labels = []
    datas = []
    
    reversed_prev = readings.reverse()

    for reading in readings:
        labels.append(str(reading.inputDate.strftime("%b")))
        datas.append(float(reading.unitsUsed))
    
    context = {
        "labels": json.dumps(labels),
        "datas": json.dumps(datas),
    }
    
    return JsonResponse(context)

def getLatestReading(request):
    latest_reading = Electricity.objects.latest("id")
    
    resp = {
        "id":latest_reading.id,
        "date": str(latest_reading.inputDate.strftime("%b" + "." + "%d" + ", " + "%Y")),
        "reading": latest_reading.reading,
        "used_units": latest_reading.unitsUsed,
        "units_cost": latest_reading.unitsCost,
    }
    
    return JsonResponse(resp)

def user_login(request):
    title = "Utility Login"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.warning(request, "The Username or Password is incorrect")
            return redirect(user_login)
    else:
        return render(request, 'user_management/login.html', {"title": title})