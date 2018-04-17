# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import NewAnnouncement, UpdateRSOCalendar
import json
import hashlib
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import django.contrib.auth.context_processors

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  return render(request, 'home.html', {'announcements': announcements})

def range(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  rso_calendar_data = UpdateRSOCalendar.objects.all()
  rso_users_list = User.objects.filter(groups__name__in=['RSO Members']).order_by('last_name')
  return render(request, 'range.html', {'announcements': announcements, 'rso_calendar_data':rso_calendar_data,\
    'rso_users_list':rso_users_list})

def marine(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  data = {}#SensorData.objects.all() 
  return render(request, 'marine.html', {'announcements': announcements})

def membership(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  data = {}#SensorData.objects.all() 
  return render(request, 'membership.html', {'announcements': announcements})

    # return HttpResponse("Hello, world. You're at the Water index.")

def about(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  question = {}
  return render(request, 'about.html', {'announcements': announcements})

@login_required
def purchase(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  question = {} 
  return render(request, 'purchase.html', {'announcements': announcements})

def events(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  question = {} 
  return render(request, 'events.html', {'announcements': announcements})
  
def documents(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  question = {} 
  return render(request, 'documents.html', {'announcements': announcements})

@login_required
def calendarManagement(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  if request.user.has_perm('applications.admin_access'):
    rso_users_list = User.objects.filter(groups__name__in=['RSO Members']).order_by('last_name')
    personal_rso_calendar_data = UpdateRSOCalendar.objects.all().order_by('-start_date')
    return render(request, 'calendarManagement.html', {'announcements': announcements,'personal_rso_calendar_data':personal_rso_calendar_data,
    'rso_users_list':rso_users_list})
  else:
    personal_rso_calendar_data = UpdateRSOCalendar.objects.filter(rso_user=User.objects.get(username=request.user)).order_by('-start_date')
    return render(request, 'calendarManagement.html', {'announcements': announcements,'personal_rso_calendar_data':personal_rso_calendar_data})

@login_required
def workBond(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  question = {} 
  return render(request, 'workbond.html', {'announcements': announcements})


#################
# RSO UPDATE PAGE
#################

# Webpage
@login_required
def calendarManagementRSO(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  if request.user.has_perm('applications.admin_access'):
    rso_users_list = User.objects.filter(groups__name__in=['RSO Members']).order_by('last_name')
    personal_rso_calendar_data = UpdateRSOCalendar.objects.all().order_by('-start_date')
    return render(request, 'management_rso.html', {'announcements': announcements,'personal_rso_calendar_data':personal_rso_calendar_data,
    'rso_users_list':rso_users_list})
  else:
    personal_rso_calendar_data = UpdateRSOCalendar.objects.filter(rso_user=User.objects.get(username=request.user)).order_by('-start_date')
    return render(request, 'management_rso.html', {'announcements': announcements,'personal_rso_calendar_data':personal_rso_calendar_data})

# Save / Update / Delete
@login_required
def updateRSOCalendar(request):
  if request.method == "POST":
    start_date = str(request.POST['rso_startDate'])
    start_time = str(request.POST['rso_startTime'])
    end_date = str(request.POST['rso_startDate'])
    end_time = str(request.POST['rso_endTime'])
    id = str(request.POST['reservation_id'])
    start_date_time = start_date + "-" + start_time
    end_date_time = start_date + "-" + end_time

    if request.POST.get('delete') and id:
      URC = UpdateRSOCalendar.objects.get(pk=id)
      URC.delete()
    elif request.POST.get('create'):
      URC = UpdateRSOCalendar(rso_user=User.objects.get(pk=request.POST['rso_user']),\
      start_date=datetime.strptime(start_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M"),\
      end_date=datetime.strptime(end_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M"))
      URC.save()
    else:
      URC = UpdateRSOCalendar.objects.get(pk=id)
      URC.rso_user=User.objects.get(pk=request.POST['rso_user'])
      URC.start_date=datetime.strptime(start_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M")
      URC.end_date=datetime.strptime(end_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M")
      URC.save()
    
    return HttpResponseRedirect('/management/rso/')

###########################
# ANNOUNCEMENT UPDATE PAGE
########################### 
@login_required
def updateAnnouncement(request):
  if request.method == "POST":
    if request.POST['announcement_type'] and request.POST['announcement_title'] \
    and request.POST['announcement_description']:

      if request.POST['announcement_id'] and request.POST.get('delete'):
        NA = NewAnnouncement.objects.get(pk=request.POST['announcement_id'])
        NA.delete()

      if request.POST['announcement_id'] and request.POST.get('update'):
        NA = NewAnnouncement.objects.get(pk=request.POST['announcement_id'])
        NA.user = User.objects.get(pk=request.user.pk)
        NA.announcement_type = request.POST['announcement_type']
        NA.announcement_title = request.POST['announcement_title']
        NA.announcement_description = request.POST['announcement_description']
        NA.save()

      if request.POST.get('create'):
        NA = NewAnnouncement(announcement_title=request.POST['announcement_title'],\
          announcement_type=request.POST['announcement_type'],\
          announcement_description=request.POST['announcement_description'],\
          announcement_user=User.objects.get(pk=request.POST['announcement_user']))
        NA.save()

      return HttpResponseRedirect('/management/announcement/')         
  else:
    print "Unable to process request"





@login_required
def updateEventCalendar(request):
  if request.method == "POST":
    start_date = str(request.POST['rso_startDate'])
    start_time = str(request.POST['rso_startTime'])
    end_date = str(request.POST['rso_startDate'])
    end_time = str(request.POST['rso_endTime'])
    id = str(request.POST['reservation_id'])
    start_date_time = start_date + "-" + start_time
    end_date_time = start_date + "-" + end_time

    if request.POST.get('delete') and id:
      URC = UpdateRSOCalendar.objects.get(pk=id)
      URC.delete()
    elif request.POST.get('create'):
      URC = UpdateRSOCalendar(rso_user=User.objects.get(pk=request.POST['rso_user']),\
      start_date=datetime.strptime(start_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M"),\
      end_date=datetime.strptime(end_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M"))
      URC.save()
    else:
      URC = UpdateRSOCalendar.objects.get(pk=id)
      URC.rso_user=User.objects.get(pk=request.POST['rso_user'])
      URC.start_date=datetime.strptime(start_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M")
      URC.end_date=datetime.strptime(end_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M")
      URC.save()
    
    return HttpResponseRedirect('/calendarManagement/rso/')

# @login_required
# def deleteRSOCalendar(request):
#   if request.method == "POST":
#     start_date = str(request.POST['rso_startDate'])
#     start_time = str(request.POST['rso_startTime'])
#     end_date = str(request.POST['rso_startDate'])
#     end_time = str(request.POST['rso_endTime'])
#     id = str(request.POST['reservation_id'])
#     start_date_time = start_date + "-" + start_time
#     end_date_time = start_date + "-" + end_time

#     URC = UpdateRSOCalendar.objects.get(pk=id)
#     URC.rso_user=User.objects.get(pk=request.POST['rso_user'])
#     URC.start_date=datetime.strptime(start_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M")
#     URC.end_date=datetime.strptime(end_date_time, '%Y-%m-%d-%H:%M').strftime("%Y-%m-%d %H:%M")
#     URC.save()
    
#     return HttpResponseRedirect('/calendarManagement/')

@login_required
def createRSOCalendarEvent(request):
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










@login_required
def calendarManagementEVENTS(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  return render(request, 'management_events.html', {'announcements': announcements})

@login_required
def calendarManagementMARINE(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  return render(request, 'management_marine.html', {'announcements': announcements})

@login_required
def calendarManagementANNOUNCEMENTS(request):
  announcements = NewAnnouncement.objects.all().order_by('-announcement_date')[:20]
  return render(request, 'management_announcement.html', {'announcements': announcements})

   
    
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


@login_required
def updateRangesPage(request):
  if request.method == "POST":
    UpdateRangesPage.objects.select_for_update().filter(id=1).update(
      range_top_notification = request.POST['range_top_notification'],
      range_200_300_section = request.POST['range_200_300_section'],
      range_100_section = request.POST['range_100_section'],
      range_25_50_section = request.POST['range_25_50_section'],
      range_trap_section = request.POST['range_trap_section'],
      range_archery_standing_section = request.POST['range_archery_standing_section'],
      range_archery_walking_section = request.POST['range_archery_walking_section'])
    return HttpResponseRedirect('/range/') 
  else:
    print "CRAP"
    return HttpResponseRedirect('/') 
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
