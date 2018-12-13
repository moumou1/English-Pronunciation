# -*- coding: utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from english.models import group, phoneme, pretestspeaking, pretestscratch, posttestspeaking, posttestscratch, database, exercise, kkdata
from django.contrib.auth.models import User
import random
from django.views.generic.base import View
from django.utils import timezone

def indextest(request):
    return render_to_response('index12.html',locals(), context_instance = RequestContext(request))

def posttestspeakinglist(request):
    member = User.objects.get(username=request.user)
    tim = member.posttestspeaking_set.all()

    c0 = tim[0].vocabulary
    c1 = tim[1].vocabulary
    c2 = tim[2].vocabulary
    c3 = tim[3].vocabulary
    c4 = tim[4].vocabulary
    c5 = tim[5].vocabulary
    c6 = tim[6].vocabulary
    c7 = tim[7].vocabulary
    c8 = tim[8].vocabulary
    c9 = tim[9].vocabulary
    c10 = tim[10].vocabulary
    c11 = tim[11].vocabulary
    c12 = tim[12].vocabulary
    c13 = tim[13].vocabulary
    c14 = tim[14].vocabulary
    c15 = tim[15].vocabulary
    c16 = tim[16].vocabulary
    c17 = tim[17].vocabulary
    c18 = tim[18].vocabulary
    c19 = tim[19].vocabulary
    c20 = tim[20].vocabulary
    c21 = tim[21].vocabulary
    c22 = tim[22].vocabulary
    c23 = tim[23].vocabulary
    c24 = tim[24].vocabulary
    c25 = tim[25].vocabulary
    c26 = tim[26].vocabulary
    c27 = tim[27].vocabulary
    c28 = tim[28].vocabulary
    c29 = tim[29].vocabulary
    c30 = tim[30].vocabulary
    c31 = tim[31].vocabulary
    c32 = tim[32].vocabulary
    c33 = tim[33].vocabulary
    c34 = tim[34].vocabulary
    c35 = tim[35].vocabulary
    c36 = tim[36].vocabulary
    c37 = tim[37].vocabulary
    c38 = tim[38].vocabulary
    c39 = tim[39].vocabulary
    c40 = tim[40].vocabulary
    c41 = tim[41].vocabulary
    c42 = tim[42].vocabulary
    c43 = tim[43].vocabulary
    c44 = tim[44].vocabulary
    c45 = tim[45].vocabulary
    c46 = tim[46].vocabulary
    c47 = tim[47].vocabulary
    c48 = tim[48].vocabulary
    c49 = tim[49].vocabulary
    c50 = tim[50].vocabulary
    c51 = tim[51].vocabulary
    c52 = tim[52].vocabulary
    c53 = tim[53].vocabulary
    c54 = tim[54].vocabulary

    b0 = tim[0].answer
    b1 = tim[1].answer
    b2 = tim[2].answer
    b3 = tim[3].answer
    b4 = tim[4].answer
    b5 = tim[5].answer
    b6 = tim[6].answer
    b7 = tim[7].answer
    b8 = tim[8].answer
    b9 = tim[9].answer
    b10 = tim[10].answer
    b11 = tim[11].answer
    b12 = tim[12].answer
    b13 = tim[13].answer
    b14 = tim[14].answer
    b15 = tim[15].answer
    b16 = tim[16].answer
    b17 = tim[17].answer
    b18 = tim[18].answer
    b19 = tim[19].answer
    b20 = tim[20].answer
    b21 = tim[21].answer
    b22 = tim[22].answer
    b23 = tim[23].answer
    b24 = tim[24].answer
    b25 = tim[25].answer
    b26 = tim[26].answer
    b27 = tim[27].answer
    b28 = tim[28].answer
    b29 = tim[29].answer
    b30 = tim[30].answer
    b31 = tim[31].answer
    b32 = tim[32].answer
    b33 = tim[33].answer
    b34 = tim[34].answer
    b35 = tim[35].answer
    b36 = tim[36].answer
    b37 = tim[37].answer
    b38 = tim[38].answer
    b39 = tim[39].answer
    b40 = tim[40].answer
    b41 = tim[41].answer
    b42 = tim[42].answer
    b43 = tim[43].answer
    b44 = tim[44].answer
    b45 = tim[45].answer
    b46 = tim[46].answer
    b47 = tim[47].answer
    b48 = tim[48].answer
    b49 = tim[49].answer
    b50 = tim[50].answer
    b51 = tim[51].answer
    b52 = tim[52].answer
    b53 = tim[53].answer
    b54 = tim[54].answer
    a0 = kkdata.objects.get(word=b0)
    a1 = kkdata.objects.get(word=b1)
    a2 = kkdata.objects.get(word=b2)
    a3 = kkdata.objects.get(word=b3)
    a4 = kkdata.objects.get(word=b4)
    a5 = kkdata.objects.get(word=b5)
    a6 = kkdata.objects.get(word=b6)
    a7 = kkdata.objects.get(word=b7)
    a8 = kkdata.objects.get(word=b8)
    a9 = kkdata.objects.get(word=b9)
    a10 = kkdata.objects.get(word=b10)
    a11 = kkdata.objects.get(word=b11)
    a12 = kkdata.objects.get(word=b12)
    a13 = kkdata.objects.get(word=b13)
    a14 = kkdata.objects.get(word=b14)
    a15 = kkdata.objects.get(word=b15)
    a16 = kkdata.objects.get(word=b16)
    a17 = kkdata.objects.get(word=b17)
    a18 = kkdata.objects.get(word=b18)
    a19 = kkdata.objects.get(word=b19)
    a20 = kkdata.objects.get(word=b20)
    a21 = kkdata.objects.get(word=b21)
    a22 = kkdata.objects.get(word=b22)
    a23 = kkdata.objects.get(word=b23)
    a24 = kkdata.objects.get(word=b24)
    a25 = kkdata.objects.get(word=b25)
    a26 = kkdata.objects.get(word=b26)
    a27 = kkdata.objects.get(word=b27)
    a28 = kkdata.objects.get(word=b28)
    a29 = kkdata.objects.get(word=b29)
    a30 = kkdata.objects.get(word=b30)
    a31 = kkdata.objects.get(word=b31)
    a32 = kkdata.objects.get(word=b32)
    a33 = kkdata.objects.get(word=b33)
    a34 = kkdata.objects.get(word=b34)
    a35 = kkdata.objects.get(word=b35)
    a36 = kkdata.objects.get(word=b36)
    a37 = kkdata.objects.get(word=b37)
    a38 = kkdata.objects.get(word=b38)
    a39 = kkdata.objects.get(word=b39)
    a40 = kkdata.objects.get(word=b40)
    a41 = kkdata.objects.get(word=b41)
    a42 = kkdata.objects.get(word=b42)
    a43 = kkdata.objects.get(word=b43)
    a44 = kkdata.objects.get(word=b44)
    a45 = kkdata.objects.get(word=b45)
    a46 = kkdata.objects.get(word=b46)
    a47 = kkdata.objects.get(word=b47)
    a48 = kkdata.objects.get(word=b48)
    a49 = kkdata.objects.get(word=b49)
    a50 = kkdata.objects.get(word=b50)
    a51 = kkdata.objects.get(word=b51)
    a52 = kkdata.objects.get(word=b52)
    a53 = kkdata.objects.get(word=b53)
    a54 = kkdata.objects.get(word=b54)

    e0 = kkdata.objects.get(word=c0)
    e1 = kkdata.objects.get(word=c1)
    e2 = kkdata.objects.get(word=c2)
    e3 = kkdata.objects.get(word=c3)
    e4 = kkdata.objects.get(word=c4)
    e5 = kkdata.objects.get(word=c5)
    e6 = kkdata.objects.get(word=c6)
    e7 = kkdata.objects.get(word=c7)
    e8 = kkdata.objects.get(word=c8)
    e9 = kkdata.objects.get(word=c9)
    e10 = kkdata.objects.get(word=c10)
    e11 = kkdata.objects.get(word=c11)
    e12 = kkdata.objects.get(word=c12)
    e13 = kkdata.objects.get(word=c13)
    e14 = kkdata.objects.get(word=c14)
    e15 = kkdata.objects.get(word=c15)
    e16 = kkdata.objects.get(word=c16)
    e17 = kkdata.objects.get(word=c17)
    e18 = kkdata.objects.get(word=c18)
    e19 = kkdata.objects.get(word=c19)
    e20 = kkdata.objects.get(word=c20)
    e21 = kkdata.objects.get(word=c21)  
    e22 = kkdata.objects.get(word=c22)
    e23 = kkdata.objects.get(word=c23)
    e24 = kkdata.objects.get(word=c24)
    e25 = kkdata.objects.get(word=c25)
    e26 = kkdata.objects.get(word=c26)
    e27 = kkdata.objects.get(word=c27)
    e28 = kkdata.objects.get(word=c28)
    e29 = kkdata.objects.get(word=c29)
    e30 = kkdata.objects.get(word=c30)
    e31 = kkdata.objects.get(word=c31)
    e32 = kkdata.objects.get(word=c32)
    e33 = kkdata.objects.get(word=c33)
    e34 = kkdata.objects.get(word=c34)
    e35 = kkdata.objects.get(word=c35)
    e36 = kkdata.objects.get(word=c36)
    e37 = kkdata.objects.get(word=c37)
    e38 = kkdata.objects.get(word=c38)
    e39 = kkdata.objects.get(word=c39)
    e40 = kkdata.objects.get(word=c40)
    e41 = kkdata.objects.get(word=c41)
    e42 = kkdata.objects.get(word=c42)
    e43 = kkdata.objects.get(word=c43)
    e44 = kkdata.objects.get(word=c44)
    e45 = kkdata.objects.get(word=c45)
    e46 = kkdata.objects.get(word=c46)
    e47 = kkdata.objects.get(word=c47)
    e48 = kkdata.objects.get(word=c48)
    e49 = kkdata.objects.get(word=c49)
    e50 = kkdata.objects.get(word=c50)
    e51 = kkdata.objects.get(word=c51)
    e52 = kkdata.objects.get(word=c52)
    e53 = kkdata.objects.get(word=c53)
    e54 = kkdata.objects.get(word=c54)

    ti = tim[54].time-tim[0].time
    if member.posttestspeaking_set.all().count()==0:
        a = "尚未參加後測！！！"
        de = member.posttestspeaking_set.all()
        de.delete()
    elif member.posttestspeaking_set.all().count<55:
        de = member.posttestspeaking_set.all()
        de.delete()
        a = "後測未做完整,請重新測驗！！！"
    else:
        a = "已完成後測！！！"
        hi = 'type="hidden"'

    d = member.posttestscratch_set.all()
    d.delete()#delete the posttestscratch
    d2 = member.exercisescratch_set.all()
    d2.delete()

    posttest = member.posttestspeaking_set.all()#all of the use answer
    qun = member.posttestspeaking_set.count()#how many question user answer

    score=0
    wm=[]
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
    for p in range(qun):
        if posttest[p].vocabulary==posttest[p].answer:
            score+=1#how many right answer user do
	else:
            am.append(posttest[p])#wrong answer(number) user do(array)
	    wm.append(p)#wrong answer(number-1) user done(array)

    i = len(am)#how many wrong answer

    for t in range(1,12):
        locals()['n%s' % (t)]=phoneme.objects.get(id=t) 
        pm.append(locals()['n%s' % (t)])#phoneme (array)

    for w in range(i):
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
        locals()['aa%s' % (k)]=len(locals()['mm%s' % (k)])

    for x in range(55):
        locals()["fre%s" % (x)]="Bingo"#final vowel list

    for g in wm:
        locals()["tre%s" % (g)]=[]#topic kk scrach
        locals()["ure%s" % (g)]=[]#user's kk scrach
	locals()["tr%s" % (g)]=[]#tre+@
	locals()["ur%s" % (g)]=[]#ure+@
        locals()["tvowel%s" % (g)]=[]#split topic kk scrach
	locals()["uvowel%s" % (g)]=[]#split user's kk scrach
	locals()["tloca%s" % (g)]=[]#topic vowel location
	locals()["uloca%s" % (g)]=[]#user vowel location
	locals()["tnum%s" % (g)]=[]
        locals()["unum%s" % (g)]=[]
	locals()["tcom%s" % (g)]=[]#topic vowel number
	locals()["ucom%s" % (g)]=[]#topic vowel number

    tm=[]
    um=[]
    for q in wm:
	locals()["tcom%s" % (q)].append(len(locals()["e%s" % (q)].kk))
	locals()["ucom%s" % (q)].append(len(locals()["a%s" % (q)].kk))
        tm.append(len(locals()["e%s" % (q)].kk))#topic kk amount list
        um.append(len(locals()["a%s" % (q)].kk))#user's kk amount list

    tmq=len(tm)#user's mistake amount

    for j in range(tmq):
        for h in range(0,tm[j]):
            locals()["tre%s" % (wm[j])].append(locals()["e%s" % (wm[j])].kk[h].encode("utf-8"))
	    locals()["tr%s" % (wm[j])].append(locals()["e%s" % (wm[j])].kk[h].encode("utf-8"))
        for s in range(0,um[j]):
            locals()["ure%s" % (wm[j])].append(locals()["a%s" % (wm[j])].kk[s].encode("utf-8"))
	    locals()["ur%s" % (wm[j])].append(locals()["a%s" % (wm[j])].kk[s].encode("utf-8"))
    phone=['\xc3\xa6', 'e', '\xc9\x9b', 'i', '\xc9\xaa', 'u', '\xca\x8a', '\xca\x8c', '\xc9\x91', 'o', '\xc9\x94']#11 vowels (ascii)

    for m in range(tmq):
	for n in range(tm[m]):
	    for y in phone:
	        if locals()["tre%s" % (wm[m])][n].find(y)!=-1:
		    locals()["tvowel%s" % (wm[m])].append(y)
		    locals()["tloca%s" % (wm[m])].append(n)
		    locals()["tnum%s" % (wm[m])].append(n)

    for zz in range(tmq):
	for yy in range(um[zz]):
	    for xx in phone:
		if locals()["ure%s" % (wm[zz])][yy].find(xx)!=-1:
		    locals()["uvowel%s" % (wm[zz])].append(xx)
		    locals()["uloca%s" % (wm[zz])].append(yy)
		    locals()["unum%s" % (wm[zz])].append(yy)

    ll=["|"]
    wv=["母音不正確"]
    more=["多念了"]
    less=["少念了"]
    into=["念錯成"]
    intt=["@"]
    to=["→"]
    stat=[] #唸錯成甚麼
    lm=[] #多念少念
    
    for ii in wm:
	if locals()["tloca%s" % (ii)]==locals()["uloca%s" % (ii)] and locals()["tvowel%s" % (ii)]==locals()["uvowel%s" % (ii)]:
	    if len(locals()["tre%s" % (ii)])>len(locals()["ure%s" % (ii)]):
		while len(locals()["tr%s" % (ii)])-len(locals()["ur%s" % (ii)])!=0:
		    locals()["ur%s" % (ii)]+=intt
	    elif len(locals()["tre%s" % (ii)])<len(locals()["ure%s" % (ii)]):
		while len(locals()["ur%s" % (ii)])-len(locals()["tr%s" % (ii)])!=0:
		    locals()["tr%s" % (ii)]+=intt
		

    for ww in wm:
	if locals()["e%s" % (ww)].kk==locals()["a%s" % (ww)].kk:
            locals()["fre%s" % (ww)]="Bingo"
	elif locals()["tloca%s" % (ww)]==locals()["uloca%s" % (ww)]:
	    if locals()["tvowel%s" % (ww)]==locals()["uvowel%s" % (ww)]:
		locals()["fre%s" % (ww)]=[]
	 	for kk in range(0,len(locals()["tr%s" % (ww)])):
		    if locals()["tr%s" % (ww)][kk]!=locals()["ur%s" % (ww)][kk]:
		        if locals()["tr%s" % (ww)][kk]=="@":
			    locals()["fre%s" % (ww)]+=more+[locals()["ur%s" % (ww)][kk]]+ll
			    lm+=more+[locals()["ur%s" % (ww)][kk]]
		        elif locals()["ur%s" % (ww)][kk]=="@":
			    locals()["fre%s" % (ww)]+=less+[locals()["tr%s" % (ww)][kk]]+ll
			    lm+=less+[locals()["ur%s" % (ww)][kk]]
			else:
			    locals()["fre%s" % (ww)]+=[locals()["tr%s" % (ww)][kk]]+to+[locals()["ur%s" % (ww)][kk]]+ll
			    stat.append([locals()["tr%s" % (ww)][kk]+"→"+locals()["ur%s" % (ww)][kk]])
	    else:
	        locals()["fre%s" % (ww)]=wv+[x for x in locals()["tvowel%s" % (ww)] if x not in locals()["uvowel%s" % (ww)]]+into+[x for x in locals()["uvowel%s" % (ww)] if x not in locals()["tvowel%s" % (ww)]]
		stat.append([x for x in locals()["tvowel%s" % (ww)] if x not in locals()["uvowel%s" % (ww)]]+to+[x for x in locals()["uvowel%s" % (ww)] if x not in locals()["tvowel%s" % (ww)]])     
	elif locals()["a%s" % (ww)].kk=="can't find kk":
	    locals()["fre%s" % (ww)]="noanswer"
	else:
	    locals()["fre%s" % (ww)]=wv

    statistic=[] #mistake list after filter

    for oo in stat:
	if not oo in statistic:
	    statistic.append(oo)
    #filter the repeat couple

    statnum=len(statistic) #number of mistake after filter
    num=[] #mistake times list 
    num_sort=[] #mistake times list after sort
    loca=[] #mistake location list after sort

    for rr in range(statnum):
	locals()["statisnum%s" % (rr)]=stat.count(statistic[rr])
	num.append(stat.count(statistic[rr]))

    while(num.count(0)!=len(num)):
	max_indx=num.index(max(num))
	loca.append(max_indx)
	num_sort.append(num[max_indx])
	num.pop(max_indx)
	num.insert(max_indx, 0)
	#sort the mistakestatis

    for pp in loca:
	locals()["st%s" % (pp)]=stat[pp]

    for ee in range(statnum):
	locals()["statisnumm%s" % (ee)]=num_sort[ee]

    for tt in range(statnum):
        locals()["statisnu%s" % (tt)]=["次數："]+[locals()["statisnumm%s" % (tt)]]

 
    return render_to_response('posttestspeakinglist.html',locals())

def posttestmistake(request):
    pos = User.objects.get(username=request.user)
    posttest = pos.pretestspeaking_set.all()#all of the use answer
    q = pos.pretestspeaking_set.count()#how many question user answer

    mis=[]
    am=[]
    mim=[]

    for p in range(0,q):
        locals()['n%s' % (p)] = posttest[p]
        if locals()['n%s' % (p)].vocabulary!=locals()['n%s' % (p)].answer:
            mis.append(posttest[p])#wrong answer(number) user do(array)
    i = len(mis)
    qua = kkdata.objects.all()
    qu = kkdata.objects.all().count()

#    for m in range(0,i):
#        for w in range(0,qu):
#            if mis[m].answer==qua[w].word:
#                mim.append(qua[w])

    return render_to_response('prosttmistake.html',locals())

def posttestspeaking1(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic1#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer1=request.POST['textbox']
       answer=answer1.lower()
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking2/')

    return render_to_response('post-testspeaking1.html',RequestContext(request,locals()))

def posttestspeaking2(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic2#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking3/')
    
    return render_to_response('post-testspeaking2.html',RequestContext(request,locals()))

def posttestspeaking3(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic3#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking4/')

    return render_to_response('post-testspeaking3.html',RequestContext(request,locals()))

def posttestspeaking4(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic4#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking5/')

    return render_to_response('post-testspeaking4.html',RequestContext(request,locals()))

def posttestspeaking5(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic5#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking6/')

    return render_to_response('post-testspeaking5.html',RequestContext(request,locals()))

def posttestspeaking6(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic6#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking7/')

    return render_to_response('post-testspeaking6.html',RequestContext(request,locals()))

def posttestspeaking7(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic7#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking8/')

    return render_to_response('post-testspeaking7.html',RequestContext(request,locals()))

def posttestspeaking8(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic8#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking9/')

    return render_to_response('post-testspeaking8.html',RequestContext(request,locals()))

def posttestspeaking9(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic9#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking10/')

    return render_to_response('post-testspeaking9.html',RequestContext(request,locals()))

def posttestspeaking10(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic10#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking11/')

    return render_to_response('post-testspeaking10.html',RequestContext(request,locals()))

def posttestspeaking11(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic11#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking12/')

    return render_to_response('post-testspeaking11.html',RequestContext(request,locals()))

def posttestspeaking12(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic12#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking13/')

    return render_to_response('post-testspeaking12.html',RequestContext(request,locals()))

def posttestspeaking13(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic13#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking14/')

    return render_to_response('post-testspeaking13.html',RequestContext(request,locals()))

def posttestspeaking14(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic14#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking15/')

    return render_to_response('post-testspeaking14.html',RequestContext(request,locals()))

def posttestspeaking15(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic15#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking16/')

    return render_to_response('post-testspeaking15.html',RequestContext(request,locals()))

def posttestspeaking16(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic16#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking17/')

    return render_to_response('post-testspeaking16.html',RequestContext(request,locals()))

def posttestspeaking17(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic17#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking18/')

    return render_to_response('post-testspeaking17.html',RequestContext(request,locals()))

def posttestspeaking18(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic18#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking19/')

    return render_to_response('post-testspeaking18.html',RequestContext(request,locals()))

def posttestspeaking19(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic19#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking20/')

    return render_to_response('post-testspeaking19.html',RequestContext(request,locals()))

def posttestspeaking20(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic20#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking21/')

    return render_to_response('post-testspeaking20.html',RequestContext(request,locals()))

def posttestspeaking21(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic21#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking22/')

    return render_to_response('post-testspeaking21.html',RequestContext(request,locals()))

def posttestspeaking22(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic22#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking23/')

    return render_to_response('post-testspeaking22.html',RequestContext(request,locals()))

def posttestspeaking23(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic23#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking24/')

    return render_to_response('post-testspeaking23.html',RequestContext(request,locals()))

def posttestspeaking24(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic24#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking25/')

    return render_to_response('post-testspeaking24.html',RequestContext(request,locals()))

def posttestspeaking25(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic25#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking26/')

    return render_to_response('post-testspeaking25.html',RequestContext(request,locals()))

def posttestspeaking26(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic26#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking27/')

    return render_to_response('post-testspeaking26.html',RequestContext(request,locals()))

def posttestspeaking27(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic27#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking28/')

    return render_to_response('post-testspeaking27.html',RequestContext(request,locals()))

def posttestspeaking28(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic28#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking29/')

    return render_to_response('post-testspeaking28.html',RequestContext(request,locals()))

def posttestspeaking29(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic29#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking30/')

    return render_to_response('post-testspeaking29.html',RequestContext(request,locals()))

def posttestspeaking30(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic30#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking31/')

    return render_to_response('post-testspeaking30.html',RequestContext(request,locals()))

def posttestspeaking31(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic31#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking32/')

    return render_to_response('post-testspeaking31.html',RequestContext(request,locals()))

def posttestspeaking32(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic32#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking33/')

    return render_to_response('post-testspeaking32.html',RequestContext(request,locals()))

def posttestspeaking33(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic33#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking34/')

    return render_to_response('post-testspeaking33.html',RequestContext(request,locals()))

def posttestspeaking34(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic34#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking35/')

    return render_to_response('post-testspeaking34.html',RequestContext(request,locals()))

def posttestspeaking35(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic35#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking36/')

    return render_to_response('post-testspeaking35.html',RequestContext(request,locals()))

def posttestspeaking36(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic36#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking37/')

    return render_to_response('post-testspeaking36.html',RequestContext(request,locals()))

def posttestspeaking37(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic37#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking38/')

    return render_to_response('post-testspeaking37.html',RequestContext(request,locals()))

def posttestspeaking38(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic38#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking39/')

    return render_to_response('post-testspeaking38.html',RequestContext(request,locals()))

def posttestspeaking39(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic39#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking40/')

    return render_to_response('post-testspeaking39.html',RequestContext(request,locals()))

def posttestspeaking40(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic40#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking41/')

    return render_to_response('post-testspeaking40.html',RequestContext(request,locals()))

def posttestspeaking41(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic41#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking42/')

    return render_to_response('post-testspeaking41.html',RequestContext(request,locals()))

def posttestspeaking42(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic42#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking43/')

    return render_to_response('post-testspeaking42.html',RequestContext(request,locals()))

def posttestspeaking43(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic43#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking44/')

    return render_to_response('post-testspeaking43.html',RequestContext(request,locals()))

def posttestspeaking44(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic44#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking45/')

    return render_to_response('post-testspeaking44.html',RequestContext(request,locals()))

def posttestspeaking45(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic45#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking46/')

    return render_to_response('post-testspeaking45.html',RequestContext(request,locals()))

def posttestspeaking46(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic46#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking47/')

    return render_to_response('post-testspeaking46.html',RequestContext(request,locals()))

def posttestspeaking47(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic47#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking48/')

    return render_to_response('post-testspeaking47.html',RequestContext(request,locals()))

def posttestspeaking48(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic48#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking49/')

    return render_to_response('post-testspeaking48.html',RequestContext(request,locals()))

def posttestspeaking49(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic49#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking50/')

    return render_to_response('post-testspeaking49.html',RequestContext(request,locals()))

def posttestspeaking50(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic50#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking51/')

    return render_to_response('post-testspeaking50.html',RequestContext(request,locals()))

def posttestspeaking51(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic51#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking52/')

    return render_to_response('post-testspeaking51.html',RequestContext(request,locals()))

def posttestspeaking52(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic52#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking53/')

    return render_to_response('post-testspeaking52.html',RequestContext(request,locals()))

def posttestspeaking53(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic53#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking54/')

    return render_to_response('post-testspeaking53.html',RequestContext(request,locals()))

def posttestspeaking54(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic54#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeaking55/')

    return render_to_response('post-testspeaking54.html',RequestContext(request,locals()))

def posttestspeaking55(request):
    member = User.objects.get(username=request.user)
    test21 = posttestscratch.objects.get(user_id=member.id)
    ee = test21.topic55#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = posttestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/posttestspeakinglist/')

    return render_to_response('post-testspeaking55.html',RequestContext(request,locals()))

# Create your views here
