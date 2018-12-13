# -*- coding: utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from english.models import group, phoneme, pretestspeaking, pretestscratch, database, kkdata
from django.contrib.auth.models import User
import random

for i in range(1,12):
            locals()['test%s' % (i)]=phoneme.objects.get(id=i)
            locals()['tes%s' % (i)]=locals()['test%s' % (i)].database_set.all()
            locals()['te%s' % (i)]=random.sample(locals()['tes%s' % (i)],5)
test221 = te1 + te2 + te3 + te4 + te5 + te6 + te7 + te8 + te9 + te10 + te11
test211 = random.sample(test221,55) 

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html', RequestContext(request, locals()))

def index(request): 
    if request.user.is_authenticated():  
        member = User.objects.get(username=request.user)
        d = member.pretestscratch_set.all()
        d.delete()
        d1 = member.posttestscratch_set.all()
        d1.delete()
        pretest = test211
        if member.pretestspeaking_set.all().count()<55:
            de = member.pretestspeaking_set.all()
            de.delete()
            a = "請先做前測!!!"
        else:    
            return HttpResponseRedirect('/pretestspeakinglist/')
    else:
        hi = 'type="hidden"'
    if request.method == "POST":
       topic1=request.POST['topic1']
       topic2=request.POST['topic2']
       topic3=request.POST['topic3']
       topic4=request.POST['topic4']
       topic5=request.POST['topic5']
       topic6=request.POST['topic6']
       topic7=request.POST['topic7']
       topic8=request.POST['topic8']
       topic9=request.POST['topic9']
       topic10=request.POST['topic10']
       topic11=request.POST['topic11']
       topic12=request.POST['topic12']
       topic13=request.POST['topic13']
       topic14=request.POST['topic14']
       topic15=request.POST['topic15']
       topic16=request.POST['topic16']
       topic17=request.POST['topic17']
       topic18=request.POST['topic18']
       topic19=request.POST['topic19']
       topic20=request.POST['topic20']
       topic21=request.POST['topic21']
       topic22=request.POST['topic22']
       topic23=request.POST['topic23']
       topic24=request.POST['topic24']
       topic25=request.POST['topic25']
       topic26=request.POST['topic26']
       topic27=request.POST['topic27']
       topic28=request.POST['topic28']
       topic29=request.POST['topic29']
       topic30=request.POST['topic30']
       topic31=request.POST['topic31']
       topic32=request.POST['topic32']
       topic33=request.POST['topic33']
       topic34=request.POST['topic34']
       topic35=request.POST['topic35']
       topic36=request.POST['topic36']
       topic37=request.POST['topic37']
       topic38=request.POST['topic38']
       topic39=request.POST['topic39']
       topic40=request.POST['topic40']
       topic41=request.POST['topic41']
       topic42=request.POST['topic42']
       topic43=request.POST['topic43']
       topic44=request.POST['topic44']
       topic45=request.POST['topic45']
       topic46=request.POST['topic46']
       topic47=request.POST['topic47']
       topic48=request.POST['topic48']
       topic49=request.POST['topic49']
       topic50=request.POST['topic50']
       topic51=request.POST['topic51']
       topic52=request.POST['topic52']
       topic53=request.POST['topic53']
       topic54=request.POST['topic54']
       topic55=request.POST['topic55']
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = pretestscratch(topic1=topic1, topic2=topic2, topic3=topic3, topic4=topic4, topic5=topic5, topic6=topic6, topic7=topic7, topic8=topic8, topic9=topic9, topic10=topic10, topic11=topic11, topic12=topic12, topic13=topic13, topic14=topic14, topic15=topic15, topic16=topic16, topic17=topic17, topic18=topic18, topic19=topic19, topic20=topic20, topic21=topic21, topic22=topic22, topic23=topic23, topic24=topic24, topic25=topic25, topic26=topic26, topic27=topic27, topic28=topic28, topic29=topic29, topic30=topic30, topic31=topic31, topic32=topic32, topic33=topic33, topic34=topic34, topic35=topic35, topic36=topic36, topic37=topic37, topic38=topic38, topic39=topic39, topic40=topic40, topic41=topic41, topic42=topic42, topic43=topic43, topic44=topic44, topic45=topic45, topic46=topic46, topic47=topic47, topic48=topic48, topic49=topic49, topic50=topic50, topic51=topic51, topic52=topic52, topic53=topic53, topic54=topic54, topic55=topic55, user=r) 
       f.save()
       return HttpResponseRedirect('/pretestspeaking1/')

    return render_to_response('index.html', RequestContext(request, locals()))

def logout(request):
    auth.logout(request)
#    if request.user.is_authenticated():
#        member = User.objects.get(username=request.user)
#    else:
#        return HttpResponseRedirect('/index/')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login')
    else:
        form = UserCreationForm()
    return render_to_response('register.html', RequestContext(request, locals()))

