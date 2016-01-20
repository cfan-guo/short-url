from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import random
import string

# Create your models here.

class Link(models.Model):
  originalURL = models.CharField(max_length=500)
  newURL = models.CharField(max_length=100, unique=True)
  #  somenumber = models.IntegerField()
  #  currenttime = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return self.originalURL

def makeShort():
  # create a random number thing
  choices = string.ascii_lowercase + string.ascii_uppercase + string.digits
  shortURL = ""
  for i in range(0,7): # arbitrarily selected number of chars to have
    shortURL = shortURL+random.choice(choices)
  return shortURL

def checkUnique(shortURL):
  # checks if shortURL already exists
  try:
    Link.objects.get(newURL=shortURL) # if true
  except Link.DoesNotExist:
    return True # get failed, meaning it is unique
  return False # get succeeded, meaning nonunique

def generateURL():
  # takes above two functions to generate unique 
  new = makeShort()
  while(checkUnique(new)==False):
    new = makeShort()
  return new

def newEntry(longURL):
  shortURL = generateURL()
  newLink = Link.objects.create(originalURL = longURL, newURL = shortURL)
  return newLink

