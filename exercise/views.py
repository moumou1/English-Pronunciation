# -*- coding: utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from english.models import group, phoneme, pretestspeaking, exercisescratch, posttestscratch, pretestscratch, posttestspeaking, database, exercise, kkdata
from django.contrib.auth.models import User
import random
from django.utils import timezone

for i in range(1,12):
    locals()['test%s' % (i)]=phoneme.objects.get(id=i)
    locals()['tes%s' % (i)]=locals()['test%s' % (i)].database_set.all()
    locals()['te%s' % (i)]=random.sample(locals()['tes%s' % (i)],5)

exa1=random.sample(tes1,7)
exa2=random.sample(tes2,7)
exa3=random.sample(tes3,6)
exaa=exa1+exa2+exa3
exa=random.sample(exaa,20)

exb1=random.sample(tes4,10)
exb2=random.sample(tes5,10)
exbb=exb1+exb2
exb=random.sample(exbb,20)

exc1=random.sample(tes6,10)
exc2=random.sample(tes7,10)
excc=exc1+exc2
exc=random.sample(excc,20)

exd1=random.sample(tes8,10)
exd2=random.sample(tes9,10)
exdd=exd1+exd2
exd=random.sample(exdd,20)

exe1=random.sample(tes10,10)
exe2=random.sample(tes11,10)
exee=exe1+exe2
exe=random.sample(exee,20)

def exerciseresult(request):
    member = User.objects.get(username=request.user)
    qua = member.exercise_set.all().count()
    ed = member.exercise_set.all()
    if qua>200:# exercise result can't more than 200 records 
        for w in range(0,qua-200):
            locals()['dd%s' % (w)] = exercise.objects.get(id=ed[w].id)
            locals()['dd%s' % (w)].delete()
    
    d = member.pretestscratch_set.all()
    d.delete()#delete the pretestscratch
    d1 = member.posttestscratch_set.all()
    d1.delete()
    d2 = member.exercisescratch_set.all()
    d2.delete()

    if member.posttestspeaking_set.all().count()==0:
        a = "尚未參加後測！！！"
        de = member.posttestspeaking_set.all()
        de.delete()
        ma = "qwe"
    elif member.posttestspeaking_set.all().count()<55:
        a = "後測未做完整,請重新測驗！！！"
        de = member.posttestspeaking_set.all()
        de.delete()
        ma = "qwe"
    else:
        a = "已完成後測！！！"          
        ty = 'type="hidden"'

    pretest = member.pretestspeaking_set.all()#all of the use answer
    q = member.pretestspeaking_set.count()#how many question user answer
    score=0
    am=[]
    pm=[]
    mm1=[]
    mm2=[]
    mm3=[]
    mm4=[]
    mm5=[]
    mm6=[]
    mm7=[]
    mm8=[]
    mm9=[]
    mm10=[]
    mm11=[]
    for p in range(0,q):
        if pretest[p].vocabulary==pretest[p].answer:
            score+=1#how many right answer user do
	else:
            am.append(pretest[p])#wrong answer(number) user do(array)

    i = len(am)#how many wrong answer

    for t in range(1,12):
        locals()['n%s' % (t)]=phoneme.objects.get(id=t) 
        pm.append(locals()['n%s' % (t)])#phoneme (array)

    for w in range(0,i):
        if am[w].vowel==pm[0].vowel:
            mm1.append(am[w])
        elif am[w].vowel==pm[1].vowel:
            mm2.append(am[w])
        elif am[w].vowel==pm[2].vowel:
            mm3.append(am[w])
        elif am[w].vowel==pm[3].vowel: 
            mm4.append(am[w])
        elif am[w].vowel==pm[4].vowel:
            mm5.append(am[w])
        elif am[w].vowel==pm[5].vowel:
            mm6.append(am[w])
        elif am[w].vowel==pm[6].vowel:
            mm7.append(am[w])
        elif am[w].vowel==pm[7].vowel:
            mm8.append(am[w])
        elif am[w].vowel==pm[8].vowel:
            mm9.append(am[w])
        elif am[w].vowel==pm[9].vowel:
            mm10.append(am[w])
        else:
            mm11.append(am[w])
            #how many wrong answer every vowel

    for k in range(1,12):
        locals()['a%s' % (k)]=len(locals()['mm%s' % (k)])
    exetest = member.exercise_set.all() 
    e = member.exercise_set.all().count()
    exetest1=[]
    exetest2=[]
    exetest3=[]
    exetest4=[]
    exetest5=[]
    for b in range(0,e):
        locals()['n%s' % (b)]=exetest[b]        
        if exetest[b].groups_id==1:
            exetest1.append(locals()['n%s' % (b)])
        elif exetest[b].groups_id==2:
            exetest2.append(locals()['n%s' % (b)])
        elif exetest[b].groups_id==3:
            exetest3.append(locals()['n%s' % (b)])
        elif exetest[b].groups_id==4:
            exetest4.append(locals()['n%s' % (b)])
        else:
            exetest5.append(locals()['n%s' % (b)])    
    for z in range(1,6):
        locals()['e%s' % (z)]=len(locals()['exetest%s' % (z)])
    return render_to_response('exerciseresult.html',locals())

def exerciseoptions(request):
    member = User.objects.get(username=request.user)
    qua = member.exercise_set.all().count()
    ed = member.exercise_set.all()
    if qua>200:# exercise result can't more than 200 records 
        for w in range(0,qua-200):
            locals()['dd%s' % (w)] = exercise.objects.get(id=ed[w].id)
            locals()['dd%s' % (w)].delete()

    d = member.pretestscratch_set.all()
    d.delete()#delete the pretestscratch
    d1 = member.posttestscratch_set.all()
    d1.delete()
    d2 = member.exercisescratch_set.all()
    d2.delete()

    if member.posttestspeaking_set.all().count()==0:
        a = "尚未參加後測！！！"
        de = member.posttestspeaking_set.all()
        de.delete()
        ma = "qwe"
    elif member.posttestspeaking_set.all().count()<55:
        a = "後測未做完整,請重新測驗！！！"
        de = member.posttestspeaking_set.all()
        de.delete()
        ma = "qwe"
    else:
        a = "已完成後測！！！"          
        hi = 'type="hidden"'
    
    pretest = member.pretestspeaking_set.all()#all of the use answer
    q = member.pretestspeaking_set.count()#how many question user answer
    score=0
    am=[]
    pm=[]
    mm1=[]
    mm2=[]
    mm3=[]
    mm4=[]
    mm5=[]
    mm6=[]
    mm7=[]
    mm8=[]
    mm9=[]
    mm10=[]
    mm11=[]
    for p in range(0,q):
        if pretest[p].vocabulary==pretest[p].answer:
            score+=1#how many right answer user do
	else:
            am.append(pretest[p])#wrong answer(number) user do(array)

    i = len(am)#how many wrong answer

    for t in range(1,12):
        locals()['n%s' % (t)]=phoneme.objects.get(id=t) 
        pm.append(locals()['n%s' % (t)])#phoneme (array)

    for w in range(0,i):
        if am[w].vowel==pm[0].vowel:
            mm1.append(am[w])
        elif am[w].vowel==pm[1].vowel:
            mm2.append(am[w])
        elif am[w].vowel==pm[2].vowel:
            mm3.append(am[w])
        elif am[w].vowel==pm[3].vowel: 
            mm4.append(am[w])
        elif am[w].vowel==pm[4].vowel:
            mm5.append(am[w])
        elif am[w].vowel==pm[5].vowel:
            mm6.append(am[w])
        elif am[w].vowel==pm[6].vowel:
            mm7.append(am[w])
        elif am[w].vowel==pm[7].vowel:
            mm8.append(am[w])
        elif am[w].vowel==pm[8].vowel:
            mm9.append(am[w])
        elif am[w].vowel==pm[9].vowel:
            mm10.append(am[w])
        else:
            mm11.append(am[w])
            #how many wrong answer every vowel

    for k in range(1,12):
        locals()['a%s' % (k)]=len(locals()['mm%s' % (k)])

    if request.user.is_authenticated():
        member = User.objects.get(username=request.user)
        aa = exa
        bb = exb
        cc = exc
        dd = exd
        ee = exe
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
       user=request.POST['user']
       r = User.objects.get(id=user)
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       f = exercisescratch(topic1=topic1, topic2=topic2, topic3=topic3, topic4=topic4, topic5=topic5, topic6=topic6, topic7=topic7, topic8=topic8, topic9=topic9, topic10=topic10, topic11=topic11, topic12=topic12, topic13=topic13, topic14=topic14, topic15=topic15, topic16=topic16, topic17=topic17, topic18=topic18, topic19=topic19, topic20=topic20, user=r, groups=g)
       f.save()
       if 'groups' in request.POST and request.POST['groups']=='1':
           return HttpResponseRedirect('/exercisea1/') 
       elif 'groups' in request.POST and request.POST['groups']=='2':
           return HttpResponseRedirect('/exerciseb1/')
       elif 'groups' in request.POST and request.POST['groups']=='3':
      	   return HttpResponseRedirect('/exercisec1/')
       elif 'groups' in request.POST and request.POST['groups']=='4':
           return HttpResponseRedirect('/exercised1/')          
       else: 
          return HttpResponseRedirect('/exercisee1/')  
  
    return render_to_response('exerciseoptions.html',RequestContext(request,locals()))

def exerciselista(request):
    member = User.objects.get(username=request.user)
    exetest = member.exercise_set.all()
    e = member.exercise_set.all().count()
    exetest1=[]#all the history in group a
    for a in range(0,e):
        locals()['n%s' % (a)]=exetest[a]
        if exetest[a].groups_id==1:
            exetest1.append(locals()['n%s' % (a)])
    q = len(exetest1)#how many record in history(group a)

    for b in range(0,q):
        locals()['t%s' % (b)]=exetest1[b].history.split()
        locals()['q%s' % (b)]=len(exetest1[b].history.split())
        locals()['score%s' % (b)]=0
        for c in range(0,locals()['q%s' % (b)]):
            if exetest1[b].vocabulary==locals()['t%s' % (b)][c]:
                locals()['score%s' % (b)]+=1
    s=[]

    for b in range(0,q):
        s.append(locals()['score%s' % (b)])#how many time your answer is right in each history
    
    return render_to_response('exerciselista.html',locals())     

def exerciselistb(request):
    member = User.objects.get(username=request.user)
    exetest = member.exercise_set.all()
    e = member.exercise_set.all().count()
    exetest2=[]#all the history in group b
    for a in range(0,e):
        locals()['n%s' % (a)]=exetest[a]
        if exetest[a].groups_id==2:
            exetest2.append(locals()['n%s' % (a)])
    q = len(exetest2)#how many record in history(group b)

    for b in range(0,q):
        locals()['t%s' % (b)]=exetest2[b].history.split()
        locals()['q%s' % (b)]=len(exetest2[b].history.split())
        locals()['score%s' % (b)]=0
        for c in range(0,locals()['q%s' % (b)]):
            if exetest2[b].vocabulary==locals()['t%s' % (b)][c]:
                locals()['score%s' % (b)]+=1
    s=[]

    for b in range(0,q):
        s.append(locals()['score%s' % (b)])#how many time your answer is right in each history
    
    return render_to_response('exerciselistb.html',locals())     

def exerciselistc(request):
    member = User.objects.get(username=request.user)
    exetest = member.exercise_set.all()
    e = member.exercise_set.all().count()
    exetest3=[]#all the history in group c
    for a in range(0,e):
        locals()['n%s' % (a)]=exetest[a]
        if exetest[a].groups_id==3:
            exetest3.append(locals()['n%s' % (a)])
    q = len(exetest3)#how many record in history(group c)

    for b in range(0,q):
        locals()['t%s' % (b)]=exetest3[b].history.split()
        locals()['q%s' % (b)]=len(exetest3[b].history.split())
        locals()['score%s' % (b)]=0
        for c in range(0,locals()['q%s' % (b)]):
            if exetest3[b].vocabulary==locals()['t%s' % (b)][c]:
                locals()['score%s' % (b)]+=1
    s=[]

    for b in range(0,q):
        s.append(locals()['score%s' % (b)])#how many time your answer is right in each history
    
    return render_to_response('exerciselistc.html',locals())     

def exerciselistd(request):
    member = User.objects.get(username=request.user)
    exetest = member.exercise_set.all()
    e = member.exercise_set.all().count()
    exetest4=[]#all the history in group d
    for a in range(0,e):
        locals()['n%s' % (a)]=exetest[a]
        if exetest[a].groups_id==4:
            exetest4.append(locals()['n%s' % (a)])
    q = len(exetest4)#how many record in history(group d)

    for b in range(0,q):
        locals()['t%s' % (b)]=exetest4[b].history.split()
        locals()['q%s' % (b)]=len(exetest4[b].history.split())
        locals()['score%s' % (b)]=0
        for c in range(0,locals()['q%s' % (b)]):
            if exetest4[b].vocabulary==locals()['t%s' % (b)][c]:
                locals()['score%s' % (b)]+=1
    s=[]

    for b in range(0,q):
        s.append(locals()['score%s' % (b)])#how many time your answer is right in each history
    
    return render_to_response('exerciselistd.html',locals())     

def exerciseliste(request):
    member = User.objects.get(username=request.user)
    exetest = member.exercise_set.all()
    e = member.exercise_set.all().count()
    exetest5=[]#all the history in group e
    for a in range(0,e):
        locals()['n%s' % (a)]=exetest[a]
        if exetest[a].groups_id==5:
            exetest5.append(locals()['n%s' % (a)])
    q = len(exetest5)#how many record in history(group e)

    for b in range(0,q):
        locals()['t%s' % (b)]=exetest5[b].history.split()
        locals()['q%s' % (b)]=len(exetest5[b].history.split())
        locals()['score%s' % (b)]=0
        for c in range(0,locals()['q%s' % (b)]):
            if exetest5[b].vocabulary==locals()['t%s' % (b)][c]:
                locals()['score%s' % (b)]+=1
    s=[]

    for b in range(0,q):
        s.append(locals()['score%s' % (b)])#how many time your answer is right in each history
    
    return render_to_response('exerciseliste.html',locals())     

def exercisea1(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic1 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea2/')

    return render_to_response('exercisea1.html',RequestContext(request,locals())) 

def exercisea2(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic2 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea3/')

    return render_to_response('exercisea2.html',RequestContext(request,locals())) 

def exercisea3(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic3 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea4/')

    return render_to_response('exercisea3.html',RequestContext(request,locals())) 

def exercisea4(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic4 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea5/')

    return render_to_response('exercisea4.html',RequestContext(request,locals())) 

def exercisea5(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic5 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea6/')

    return render_to_response('exercisea5.html',RequestContext(request,locals())) 

def exercisea6(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic6 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea7/')

    return render_to_response('exercisea6.html',RequestContext(request,locals())) 

def exercisea7(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic7 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea8/')

    return render_to_response('exercisea7.html',RequestContext(request,locals())) 

def exercisea8(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic8 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea9/')

    return render_to_response('exercisea8.html',RequestContext(request,locals())) 

def exercisea9(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic9 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea10/')

    return render_to_response('exercisea9.html',RequestContext(request,locals())) 

def exercisea10(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic10 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea11/')

    return render_to_response('exercisea10.html',RequestContext(request,locals())) 

def exercisea11(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic11 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea12/')

    return render_to_response('exercisea11.html',RequestContext(request,locals())) 

def exercisea12(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic12 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea13/')

    return render_to_response('exercisea12.html',RequestContext(request,locals())) 

def exercisea13(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic13 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea14/')

    return render_to_response('exercisea13.html',RequestContext(request,locals())) 

def exercisea14(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic14 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea15/')

    return render_to_response('exercisea14.html',RequestContext(request,locals())) 

def exercisea15(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic15 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea16/')

    return render_to_response('exercisea15.html',RequestContext(request,locals())) 

def exercisea16(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic16 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea17/')

    return render_to_response('exercisea16.html',RequestContext(request,locals())) 

def exercisea17(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic17 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea18/')

    return render_to_response('exercisea17.html',RequestContext(request,locals())) 

def exercisea18(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic18 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea19/')

    return render_to_response('exercisea18.html',RequestContext(request,locals())) 

def exercisea19(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic19 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisea20/')

    return render_to_response('exercisea19.html',RequestContext(request,locals())) 

def exercisea20(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=1, user=member.id)
    ee = ex.topic20 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseresult/')

    return render_to_response('exercisea20.html',RequestContext(request,locals())) 

def exerciseb1(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic1 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb2/')

    return render_to_response('exerciseb1.html',RequestContext(request,locals())) 

def exerciseb2(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic2 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb3/')

    return render_to_response('exerciseb2.html',RequestContext(request,locals())) 

def exerciseb3(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic3 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb4/')

    return render_to_response('exerciseb3.html',RequestContext(request,locals())) 

def exerciseb4(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic4 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb5/')

    return render_to_response('exerciseb4.html',RequestContext(request,locals())) 

def exerciseb5(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic5 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb6/')

    return render_to_response('exerciseb5.html',RequestContext(request,locals())) 

def exerciseb6(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic6 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb7/')

    return render_to_response('exerciseb6.html',RequestContext(request,locals())) 

def exerciseb7(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic7 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb8/')

    return render_to_response('exerciseb7.html',RequestContext(request,locals())) 

def exerciseb8(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic8 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb9/')

    return render_to_response('exerciseb8.html',RequestContext(request,locals())) 

def exerciseb9(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic9 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb10/')

    return render_to_response('exerciseb9.html',RequestContext(request,locals())) 

def exerciseb10(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic10 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb11/')

    return render_to_response('exerciseb10.html',RequestContext(request,locals())) 

def exerciseb11(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic11 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb12/')

    return render_to_response('exerciseb11.html',RequestContext(request,locals())) 

def exerciseb12(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic12 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb13/')

    return render_to_response('exerciseb12.html',RequestContext(request,locals())) 

def exerciseb13(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic13 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb14/')

    return render_to_response('exerciseb13.html',RequestContext(request,locals())) 

def exerciseb14(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic14 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb15/')

    return render_to_response('exerciseb14.html',RequestContext(request,locals())) 

def exerciseb15(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic15 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb16/')

    return render_to_response('exerciseb15.html',RequestContext(request,locals())) 

def exerciseb16(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic16 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb17/')

    return render_to_response('exerciseb16.html',RequestContext(request,locals())) 

def exerciseb17(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic17 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb18/')

    return render_to_response('exerciseb17.html',RequestContext(request,locals())) 

def exerciseb18(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic18 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb19/')

    return render_to_response('exerciseb18.html',RequestContext(request,locals())) 

def exerciseb19(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic19 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseb20/')

    return render_to_response('exerciseb19.html',RequestContext(request,locals())) 

def exerciseb20(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=2, user=member.id)
    ee = ex.topic20 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseresult/')

    return render_to_response('exerciseb20.html',RequestContext(request,locals())) 

def exercisec1(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic1 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec2/')

    return render_to_response('exercisec1.html',RequestContext(request,locals())) 

def exercisec2(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic2 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec3/')

    return render_to_response('exercisec2.html',RequestContext(request,locals())) 

def exercisec3(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic3 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec4/')

    return render_to_response('exercisec3.html',RequestContext(request,locals())) 

def exercisec4(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic4 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec5/')

    return render_to_response('exercisec4.html',RequestContext(request,locals())) 

def exercisec5(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic5 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec6/')

    return render_to_response('exercisec5.html',RequestContext(request,locals())) 

def exercisec6(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic6 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec7/')

    return render_to_response('exercisec6.html',RequestContext(request,locals())) 

def exercisec7(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic7 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec8/')

    return render_to_response('exercisec7.html',RequestContext(request,locals())) 

def exercisec8(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic8 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec9/')

    return render_to_response('exercisec8.html',RequestContext(request,locals())) 

def exercisec9(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic9 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec10/')

    return render_to_response('exercisec9.html',RequestContext(request,locals())) 

def exercisec10(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic10 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec11/')

    return render_to_response('exercisec10.html',RequestContext(request,locals())) 

def exercisec11(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic11 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec12/')

    return render_to_response('exercisec11.html',RequestContext(request,locals())) 

def exercisec12(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic12 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec13/')

    return render_to_response('exercisec12.html',RequestContext(request,locals())) 

def exercisec13(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic13 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec14/')

    return render_to_response('exercisec13.html',RequestContext(request,locals())) 

def exercisec14(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic14 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec15/')

    return render_to_response('exercisec14.html',RequestContext(request,locals())) 

def exercisec15(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic15 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec16/')

    return render_to_response('exercisec15.html',RequestContext(request,locals())) 

def exercisec16(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic16 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec17/')

    return render_to_response('exercisec16.html',RequestContext(request,locals())) 

def exercisec17(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic17 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec18/')

    return render_to_response('exercisec17.html',RequestContext(request,locals())) 

def exercisec18(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic18 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec19/')

    return render_to_response('exercisec18.html',RequestContext(request,locals())) 

def exercisec19(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic19 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisec20/')

    return render_to_response('exercisec19.html',RequestContext(request,locals())) 

def exercisec20(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=3, user=member.id)
    ee = ex.topic20 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseresult/')

    return render_to_response('exercisec20.html',RequestContext(request,locals())) 

def exercised1(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic1 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised2/')

    return render_to_response('exercised1.html',RequestContext(request,locals())) 

def exercised2(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic2 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised3/')

    return render_to_response('exercised2.html',RequestContext(request,locals())) 

def exercised3(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic3 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised4/')

    return render_to_response('exercised3.html',RequestContext(request,locals())) 

def exercised4(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic4 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised5/')

    return render_to_response('exercised4.html',RequestContext(request,locals())) 

def exercised5(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic5 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised6/')

    return render_to_response('exercised5.html',RequestContext(request,locals())) 

def exercised6(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic6 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised7/')

    return render_to_response('exercised6.html',RequestContext(request,locals())) 

def exercised7(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic7 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised8/')

    return render_to_response('exercised7.html',RequestContext(request,locals())) 

def exercised8(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic8 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised9/')

    return render_to_response('exercised8.html',RequestContext(request,locals())) 

def exercised9(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic9 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised10/')

    return render_to_response('exercised9.html',RequestContext(request,locals())) 

def exercised10(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic10 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised11/')

    return render_to_response('exercised10.html',RequestContext(request,locals())) 

def exercised11(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic11 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised12/')

    return render_to_response('exercised11.html',RequestContext(request,locals())) 

def exercised12(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic12 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised13/')

    return render_to_response('exercised12.html',RequestContext(request,locals())) 

def exercised13(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic13 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised14/')

    return render_to_response('exercised13.html',RequestContext(request,locals())) 

def exercised14(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic14 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised15/')

    return render_to_response('exercised14.html',RequestContext(request,locals())) 

def exercised15(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic15 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised16/')

    return render_to_response('exercised15.html',RequestContext(request,locals())) 

def exercised16(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic16 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised17/')

    return render_to_response('exercised16.html',RequestContext(request,locals())) 

def exercised17(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic17 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised18/')

    return render_to_response('exercised17.html',RequestContext(request,locals())) 

def exercised18(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic18 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised19/')

    return render_to_response('exercised18.html',RequestContext(request,locals())) 

def exercised19(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic19 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercised20/')

    return render_to_response('exercised19.html',RequestContext(request,locals())) 

def exercised20(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=4, user=member.id)
    ee = ex.topic20 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseresult/')

    return render_to_response('exercised20.html',RequestContext(request,locals())) 

def exercisee1(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic1 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee2/')

    return render_to_response('exercisee1.html',RequestContext(request,locals())) 

def exercisee2(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic2 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee3/')

    return render_to_response('exercisee2.html',RequestContext(request,locals())) 

def exercisee3(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic3 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee4/')

    return render_to_response('exercisee3.html',RequestContext(request,locals())) 

def exercisee4(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic4 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee5/')

    return render_to_response('exercisee4.html',RequestContext(request,locals())) 

def exercisee5(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic5 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee6/')

    return render_to_response('exercisee5.html',RequestContext(request,locals())) 

def exercisee6(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic6 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee7/')

    return render_to_response('exercisee6.html',RequestContext(request,locals())) 

def exercisee7(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic7 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee8/')

    return render_to_response('exercisee7.html',RequestContext(request,locals())) 

def exercisee8(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic8 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee9/')

    return render_to_response('exercisee8.html',RequestContext(request,locals())) 

def exercisee9(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic9 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee10/')

    return render_to_response('exercisee9.html',RequestContext(request,locals())) 

def exercisee10(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic10 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee11/')

    return render_to_response('exercisee10.html',RequestContext(request,locals())) 

def exercisee11(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic11 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee12/')

    return render_to_response('exercisee11.html',RequestContext(request,locals())) 

def exercisee12(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic12 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee13/')

    return render_to_response('exercisee12.html',RequestContext(request,locals())) 

def exercisee13(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic13 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee14/')

    return render_to_response('exercisee13.html',RequestContext(request,locals())) 

def exercisee14(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic14 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee15/')

    return render_to_response('exercisee14.html',RequestContext(request,locals())) 

def exercisee15(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic15 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee16/')

    return render_to_response('exercisee15.html',RequestContext(request,locals())) 

def exercisee16(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic16 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee17/')

    return render_to_response('exercisee16.html',RequestContext(request,locals())) 

def exercisee17(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic17 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee18/')

    return render_to_response('exercisee17.html',RequestContext(request,locals())) 

def exercisee18(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic18 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee19/')

    return render_to_response('exercisee18.html',RequestContext(request,locals())) 

def exercisee19(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic19 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exercisee20/')

    return render_to_response('exercisee19.html',RequestContext(request,locals())) 

def exercisee20(request):
    member = User.objects.get(username=request.user)
    ex = exercisescratch.objects.get(groups=5, user=member.id)
    ee = ex.topic20 
    a = kkdata.objects.get(word=ee)
    v = database.objects.get(vocabulary=ee)
    if request.method == "POST":
       vocabulary=request.POST['vocabulary']
       answer=request.POST['answer']
       vowel=request.POST['vowel']
       history=request.POST['history']
       groups=request.POST['groups']
       g = group.objects.get(id=groups)
       user=request.POST['user']
       r = User.objects.get(id=user)
       f = exercise(vocabulary=vocabulary, answer=answer, vowel=vowel, history=history, groups=g, user=r)
       f.save()
       return HttpResponseRedirect('/exerciseresult/')

    return render_to_response('exercisee20.html',RequestContext(request,locals())) 

# Create your views here.
