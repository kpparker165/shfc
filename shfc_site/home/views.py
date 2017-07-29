from django.template import Context, loader
from events.models import Event
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
  latest_event_list = Event.objects.all().order_by('-event_creation_date')[:10]
  c = Context({
  'latest_event_list': latest_event_list,
  })
  return render(request, 'index.html', c)
