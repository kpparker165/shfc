from django.template import Context, loader
from events.models import Event
from boats.models import Boat
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core import serializers


def index(request):
  latest_event_list = Event.objects.all().order_by('-event_creation_date')[:10]
  
  c = Context({
  'latest_event_list': latest_event_list,
  })
  return render(request, 'boats/index.html', c)

# def index(request):
#     return render(request, "boats/index.html")
def schedule(request):
	qs = Boat.objects.all()
	data = serializers.serialize('json', qs)
	return HttpResponse(qs, content_type="application/json")