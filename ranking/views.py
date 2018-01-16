# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from bs4 import BeautifulSoup
import requests
from models import *

def index(request):
	total = []
	result = User.objects.filter().order_by('-correct')
	for r in result:
		percent = int(float(r.correct)/r.tries*100)
		total.append((r.name,r.correct,r.tries,str(percent)+'%',r.last,r.status))
	
	return render(request, 'index.html',{'total':total})

def update(request):
	print 'called'
	members = []
	result = User.objects.filter()
	for r in result:
		members.append(r.name)
	for id in members:
		response = requests.get('https://www.acmicpc.net/user/'+id)
		soup = BeautifulSoup(response.text,'html.parser')
		list = soup.find_all('blockquote')
		status= list[0].string

		list = soup.find_all('td')
		correct = list[1].string
		tries = list[2].string

		response = requests.get('https://www.acmicpc.net/status/?user_id='+id)
		soup = BeautifulSoup(response.text,'html.parser')
		list = soup.find_all('td')
		last = list[8].string

		User(name=id,correct=correct,tries=tries,last=last,status=status).save()	
	return render(request, 'index.html')