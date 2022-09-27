from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from .models import Students

def home(request):
	data = Students.objects.all()
	data_json = serializers.serialize('json', data)
	return HttpResponse(data_json, content_type="text/json-comment-filtered")