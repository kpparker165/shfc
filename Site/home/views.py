# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import UpdateHomePage, NewAnnouncement, UpdateRSOCalendar
import json
import hashlib
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:10]
  information =  UpdateHomePage.objects.all().first()
  return render(request, 'home.html', {'information': information, 'announcements': announcements})

def range(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:10]
  rso_calendar_data = UpdateRSOCalendar.objects.all()
  return render(request, 'range.html', {'announcements': announcements, 'rso_calendar_data':rso_calendar_data})

def marine(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:10]
  data = {}#SensorData.objects.all() 
  return render(request, 'marine.html', {'announcements': announcements})

def membership(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:10]
  data = {}#SensorData.objects.all() 
  return render(request, 'membership.html', {'announcements': announcements})

    # return HttpResponse("Hello, world. You're at the Water index.")

def about(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:10]
  question = {}
  return render(request, 'about.html', {'announcements': announcements})

def purchase(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:10]
  question = {} 
  return render(request, 'purchase.html', {'announcements': announcements})

def calendar(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:10]
  question = {} 
  return render(request, 'calendar.html', {'announcements': announcements})

@login_required
def newAnnouncement(request):
  if request.method == "POST":
    if request.POST['announcement_type'] and request.POST['announcement_title'] \
    and request.POST['announcement_description']:
      NA = NewAnnouncement(announcement_title=request.POST['announcement_title'],\
        announcement_type=request.POST['announcement_type'],\
        announcement_description=request.POST['announcement_description'],\
        announcement_user=User.objects.get(pk=request.POST['announcement_user']))
      NA.save()

      return HttpResponseRedirect('/') 
  else:
    print "CRAP"

@login_required
def updateHomePage(request):
  if request.method == "POST":
    UpdateHomePage.objects.select_for_update().filter(id=1).update(about_section=request.POST['about_description'],\
      facilities_section=request.POST['facilities_description'], general_section=request.POST['general_description'])
    
    return HttpResponseRedirect('/') 
  else:
    print "CRAP"
    return HttpResponseRedirect('/') 

@login_required
def updateRSOCalendar(request):
  if request.method == "POST":
    start_date = str(request.POST['rso_startDate'])
    start_time = str(request.POST['rso_startTime'])
    end_date = str(request.POST['rso_startDate'])
    end_time = str(request.POST['rso_endTime'])
    start_date_time = start_date + "-" + start_time
    end_date_time = start_date + "-" + end_time

    URC = UpdateRSOCalendar(rso_user=User.objects.get(pk=request.POST['rso_user']),\
      start_date=datetime.strptime(start_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M"),\
      end_date=datetime.strptime(end_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M"))
    URC.save()
    
    return HttpResponseRedirect('/range/') 
   
    



@csrf_exempt
def save(request):
  if request.method == "POST":
    received_json_data=json.loads(request.body)
    # This is what the data should look like
    # Trasnmit time = epoch time 1520316652
    #data = {'device_data':{'device_id':'8944501805175413977','device_key':'SECRET_KEY','location':'655 arbutus street','signal_strength':'5','transmit_time':'1520316652','distance_cm':80,'confidence_level':2}}

    request_obj = {}
    request_obj = received_json_data['device_data']
    device_id = received_json_data['device_data']['device_id']
    device_key = received_json_data['device_data']['device_key']
    location = received_json_data['device_data']['location']
    signal_strength = received_json_data['device_data']['signal_strength']
    transmit_time = received_json_data['device_data']['transmit_time']
    distance_cm = received_json_data['device_data']['distance_cm']
    confidence_level = received_json_data['device_data']['confidence_level']

    rd = RegisteredDevice.objects.filter(device_ID=str(device_id))
    if len(rd) > 1:
      return HttpResponse("WE HAVE MORE THAN ONE RETURNED ITEM!!!")

    # use -n when creating a new has in your shell
    # echo -n "STRING" | md5
    if hashlib.md5(device_key).hexdigest() == rd[0].device_key:
      try:
        sd = SensorData(
          device_id=rd[0],
          location=location,
          signal_strength=signal_strength,
          transmit_time=transmit_time,
          distance_cm=distance_cm, 
          confidence_level=confidence_level,
        ) 
        sd.save()
        return HttpResponseRedirect("/products")
      except Exception, e:
        raise e
    else:
      return HttpResponse("YOU HAVE FAILED TO PROVIDE THE CORRECT KEY")
  else:
    return HttpResponse("DID NOT USE A POST COMMAND")

## FOR TESTING URLS
# def tetingSend():
# import requests  
# import json
# url = "http://127.0.0.1:8000/save/"
# data = {'data':[{'key1':'val1'}, {'key2':'val2'}]}
#data = {'device_data':{'device_id':'8944501805175413977','location':'655 arbutus street','signal_strength':'5','transmit_time':'40 min','distance_cm':80,'confidence_level':2}}
# headers = {'content-type': 'application/json'}
# r=requests.post(url, data=json.dumps(data), headers=headers)
# r.text
