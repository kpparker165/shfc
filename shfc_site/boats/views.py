from django.template import Context, loader
from polls.models import Poll
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "boats/index.html")
