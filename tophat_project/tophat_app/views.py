from django.shortcuts import render
from  django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import List # this is ours!

# Create your views here.

def index(request):
  # somehow get the link (user input)
  # paste the new URL
  if request.method == 'POST'
    form = 

  # in the other thing, when given a URL it needs to look into the database
  # from database, match the shortlink with the long URL
  # redirect to long URL

  return HttpResponse("Placeholder for URL thing")

def short(request, short_url):
  try:
    List.objects.get(newURL=short_url)
  except Link.DoesNotExist:
    return HttpResponse("Link does not exist") # get failed, meaning it is unique
  return HttpResponseRedirect(Link.objects.get(newURL=short_url).originalURL) #else redirects
