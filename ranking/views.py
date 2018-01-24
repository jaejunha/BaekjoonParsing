# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from bs4 import BeautifulSoup
import requests
from models import *

def index(request):
	problem = []
	total = []
	ds = []
	result = User.objects.filter().order_by('-correct')
	for r in result:
		percent = int(float(r.correct)/r.tries*100)
		total.append((r.name,r.correct,r.tries,str(percent)+'%',r.last,r.status))
	
	result = User.objects.filter().order_by('-ds')
	for r in result:
		if r.ds>0:
			percent = int(float(r.ds)/19*100)
			ds.append((r.name,str(r.ds)+' / 19',str(percent)+'%'))
	
	result = Problem.objects.filter()
	for r in result:
		try:
			counter = Solve.objects.get(number=r.number).count()[0]
		except:
			counter = 0
		problem.append((r.number,r.title, counter, int(counter/float(100)*100)))

	return render(request, 'index.html',{'total':total,'ds':ds,'problem':problem})

def update(request):
	members = []
	result = User.objects.filter()
	for r in result:
		members.append(r.name)
	for id in members:
		response = requests.get('https://www.acmicpc.net/user/'+id)
		soup = BeautifulSoup(response.text,'html.parser')
		list = soup.find_all('blockquote')
		status= list[0].string

		problems=[]
		ds = 0
		list = soup.find_all(class_="problem_number")
		for l in list:
			problems.append(int(l.string))

		for p in Problem.objects.filter():
			if p.number in problems:
				Solve(name=id,number=p.number).save()	
				ds=ds+1

		list = soup.find_all('td')
		correct = list[1].string
		tries = list[2].string

		response = requests.get('https://www.acmicpc.net/status/?user_id='+id)
		soup = BeautifulSoup(response.text,'html.parser')
		list = soup.find_all('td')
		last = list[8].string

		User(name=id,correct=correct,tries=tries,last=last,status=status,ds=ds).save()	
	return render(request, 'index.html')
