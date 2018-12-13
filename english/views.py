# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from english.models import group, phoneme, pretestspeaking, pretestscratch, posttestspeaking, posttestscratch, database, exercise, kkdata
from django.contrib.auth.models import User
import random
from django.views.generic.base import View
from django.utils import timezone
import subtest

for i in range(1,12):
            locals()['test%s' % (i)]=phoneme.objects.get(id=i)
            locals()['tes%s' % (i)]=locals()['test%s' % (i)].database_set.all()
            locals()['te%s' % (i)]=random.sample(locals()['tes%s' % (i)],5)
test221 = te1 + te2 + te3 + te4 + te5 + te6 + te7 + te8 + te9 + te10 + te11
test211 = random.sample(test221,55) 

def pretestspeakinglist(request):
    member = User.objects.get(username=request.user)
    tim = member.pretestspeaking_set.all()

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

    ti=tim[54].time-tim[0].time
    posttest = test211
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
       f = posttestscratch(topic1=topic1, topic2=topic2, topic3=topic3, topic4=topic4, topic5=topic5, topic6=topic6, topic7=topic7, topic8=topic8, topic9=topic9, topic10=topic10, topic11=topic11, topic12=topic12, topic13=topic13, topic14=topic14, topic15=topic15, topic16=topic16, topic17=topic17, topic18=topic18, topic19=topic19, topic20=topic20, topic21=topic21, topic22=topic22, topic23=topic23, topic24=topic24, topic25=topic25, topic26=topic26, topic27=topic27, topic28=topic28, topic29=topic29, topic30=topic30, topic31=topic31, topic32=topic32, topic33=topic33, topic34=topic34, topic35=topic35, topic36=topic36, topic37=topic37, topic38=topic38, topic39=topic39, topic40=topic40, topic41=topic41, topic42=topic42, topic43=topic43, topic44=topic44, topic45=topic45, topic46=topic46, topic47=topic47, topic48=topic48, topic49=topic49, topic50=topic50, topic51=topic51, topic52=topic52, topic53=topic53, topic54=topic54, topic55=topic55, user=r) 
       f.save()
       return HttpResponseRedirect('/posttestspeaking1/')    

    d = member.pretestscratch_set.all()
    d.delete()#delete the pretestscratch
    d1 = member.posttestscratch_set.all()
    d1.delete()
    d2 = member.exercisescratch_set.all()
    d2.delete()
    pretest = member.pretestspeaking_set.all()#all of the use answer
    qun = member.pretestspeaking_set.count()#how many question user answer

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
        if pretest[p].vocabulary==pretest[p].answer:
            score+=1#how many right answer user do
	else:
            am.append(pretest[p])#wrong answer user done(array)
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
        locals()["fre%s" % (x)]="Bingo"#final analysis list

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
        for h in range(tm[j]):
            locals()["tre%s" % (wm[j])].append(locals()["e%s" % (wm[j])].kk[h].encode("utf-8"))
	    locals()["tr%s" % (wm[j])].append(locals()["e%s" % (wm[j])].kk[h].encode("utf-8"))
        for s in range(um[j]):
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
    stat=[] #甚麼唸錯成甚麼
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
	 	for kk in range(len(locals()["tr%s" % (ww)])):
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

	

    return render_to_response('pretestspeakinglist.html',RequestContext(request,locals()))

def mistakestatis(request):
    member = User.objects.get(username=request.user)
    tim = member.pretestspeaking_set.all()

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

    pretest=member.pretestspeaking_set.all()
    qun=member.pretestspeaking_set.count()
    score=0
    wm=[]

    for p in range(qun):
        if pretest[p].vocabulary!=pretest[p].answer:
            score+=1#how many wrong answer user do
            wm.append(p)#wrong answer(number-1) user done(array)

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
        for h in range(tm[j]):
            locals()["tre%s" % (wm[j])].append(locals()["e%s" % (wm[j])].kk[h].encode("utf-8"))
	    locals()["tr%s" % (wm[j])].append(locals()["e%s" % (wm[j])].kk[h].encode("utf-8"))
        for s in range(um[j]):
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
    stat=[] #甚麼唸錯成甚麼
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
	if locals()["tloca%s" % (ww)]==locals()["uloca%s" % (ww)]:
	    if locals()["tvowel%s" % (ww)]==locals()["uvowel%s" % (ww)]:
	 	for kk in range(len(locals()["tr%s" % (ww)])):
		    if locals()["tr%s" % (ww)][kk]!=locals()["ur%s" % (ww)][kk]:
		        if locals()["tr%s" % (ww)][kk]=="@":
			    lm+=more+[locals()["ur%s" % (ww)][kk]]+ll
		        elif locals()["ur%s" % (ww)][kk]=="@":
			    lm+=less+[locals()["ur%s" % (ww)][kk]]+ll
			else:
			    stat.append([locals()["tr%s" % (ww)][kk]+"→"+locals()["ur%s" % (ww)][kk]])
	    else:
	        stat.append([x for x in locals()["tvowel%s" % (ww)] if x not in locals()["uvowel%s" % (ww)]]+to+[x for x in locals()["uvowel%s" % (ww)] if x not in locals()["tvowel%s" % (ww)]])     
	
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

    """posttestspeaking"""
    
    timp = member.posttestspeaking_set.all()

    cp0 = timp[0].vocabulary
    cp1 = timp[1].vocabulary
    cp2 = timp[2].vocabulary
    cp3 = timp[3].vocabulary
    cp4 = timp[4].vocabulary
    cp5 = timp[5].vocabulary
    cp6 = timp[6].vocabulary
    cp7 = timp[7].vocabulary
    cp8 = timp[8].vocabulary
    cp9 = timp[9].vocabulary
    cp10 = timp[10].vocabulary
    cp11 = timp[11].vocabulary
    cp12 = timp[12].vocabulary
    cp13 = timp[13].vocabulary
    cp14 = timp[14].vocabulary
    cp15 = timp[15].vocabulary
    cp16 = timp[16].vocabulary
    cp17 = timp[17].vocabulary
    cp18 = timp[18].vocabulary
    cp19 = timp[19].vocabulary
    cp20 = timp[20].vocabulary
    cp21 = timp[21].vocabulary
    cp22 = timp[22].vocabulary
    cp23 = timp[23].vocabulary
    cp24 = timp[24].vocabulary
    cp25 = timp[25].vocabulary
    cp26 = timp[26].vocabulary
    cp27 = timp[27].vocabulary
    cp28 = timp[28].vocabulary
    cp29 = timp[29].vocabulary
    cp30 = timp[30].vocabulary
    cp31 = timp[31].vocabulary
    cp32 = timp[32].vocabulary
    cp33 = timp[33].vocabulary
    cp34 = timp[34].vocabulary
    cp35 = timp[35].vocabulary
    cp36 = timp[36].vocabulary
    cp37 = timp[37].vocabulary
    cp38 = timp[38].vocabulary
    cp39 = timp[39].vocabulary
    cp40 = timp[40].vocabulary
    cp41 = timp[41].vocabulary
    cp42 = timp[42].vocabulary
    cp43 = timp[43].vocabulary
    cp44 = timp[44].vocabulary
    cp45 = timp[45].vocabulary
    cp46 = timp[46].vocabulary
    cp47 = timp[47].vocabulary
    cp48 = timp[48].vocabulary
    cp49 = timp[49].vocabulary
    cp50 = timp[50].vocabulary
    cp51 = timp[51].vocabulary
    cp52 = timp[52].vocabulary
    cp53 = timp[53].vocabulary
    cp54 = timp[54].vocabulary

    bp0 = timp[0].answer
    bp1 = timp[1].answer
    bp2 = timp[2].answer
    bp3 = timp[3].answer
    bp4 = timp[4].answer
    bp5 = timp[5].answer
    bp6 = timp[6].answer
    bp7 = timp[7].answer
    bp8 = timp[8].answer
    bp9 = timp[9].answer
    bp10 = timp[10].answer
    bp11 = timp[11].answer
    bp12 = timp[12].answer
    bp13 = timp[13].answer
    bp14 = timp[14].answer
    bp15 = timp[15].answer
    bp16 = timp[16].answer
    bp17 = timp[17].answer
    bp18 = timp[18].answer
    bp19 = timp[19].answer
    bp20 = timp[20].answer
    bp21 = timp[21].answer
    bp22 = timp[22].answer
    bp23 = timp[23].answer
    bp24 = timp[24].answer
    bp25 = timp[25].answer
    bp26 = timp[26].answer
    bp27 = timp[27].answer
    bp28 = timp[28].answer
    bp29 = timp[29].answer
    bp30 = timp[30].answer
    bp31 = timp[31].answer
    bp32 = timp[32].answer
    bp33 = timp[33].answer
    bp34 = timp[34].answer
    bp35 = timp[35].answer
    bp36 = timp[36].answer
    bp37 = timp[37].answer
    bp38 = timp[38].answer
    bp39 = timp[39].answer
    bp40 = timp[40].answer
    bp41 = timp[41].answer
    bp42 = timp[42].answer
    bp43 = timp[43].answer
    bp44 = timp[44].answer
    bp45 = timp[45].answer
    bp46 = timp[46].answer
    bp47 = timp[47].answer
    bp48 = timp[48].answer
    bp49 = timp[49].answer
    bp50 = timp[50].answer
    bp51 = timp[51].answer
    bp52 = timp[52].answer
    bp53 = timp[53].answer
    bp54 = timp[54].answer
    ap0 = kkdata.objects.get(word=bp0)
    ap1 = kkdata.objects.get(word=bp1)
    ap2 = kkdata.objects.get(word=bp2)
    ap3 = kkdata.objects.get(word=bp3)
    ap4 = kkdata.objects.get(word=bp4)
    ap5 = kkdata.objects.get(word=bp5)
    ap6 = kkdata.objects.get(word=bp6)
    ap7 = kkdata.objects.get(word=bp7)
    ap8 = kkdata.objects.get(word=bp8)
    ap9 = kkdata.objects.get(word=bp9)
    ap10 = kkdata.objects.get(word=bp10)
    ap11 = kkdata.objects.get(word=bp11)
    ap12 = kkdata.objects.get(word=bp12)
    ap13 = kkdata.objects.get(word=bp13)
    ap14 = kkdata.objects.get(word=bp14)
    ap15 = kkdata.objects.get(word=bp15)
    ap16 = kkdata.objects.get(word=bp16)
    ap17 = kkdata.objects.get(word=bp17)
    ap18 = kkdata.objects.get(word=bp18)
    ap19 = kkdata.objects.get(word=bp19)
    ap20 = kkdata.objects.get(word=bp20)
    ap21 = kkdata.objects.get(word=bp21)
    ap22 = kkdata.objects.get(word=bp22)
    ap23 = kkdata.objects.get(word=bp23)
    ap24 = kkdata.objects.get(word=bp24)
    ap25 = kkdata.objects.get(word=bp25)
    ap26 = kkdata.objects.get(word=bp26)
    ap27 = kkdata.objects.get(word=bp27)
    ap28 = kkdata.objects.get(word=bp28)
    ap29 = kkdata.objects.get(word=bp29)
    ap30 = kkdata.objects.get(word=bp30)
    ap31 = kkdata.objects.get(word=bp31)
    ap32 = kkdata.objects.get(word=bp32)
    ap33 = kkdata.objects.get(word=bp33)
    ap34 = kkdata.objects.get(word=bp34)
    ap35 = kkdata.objects.get(word=bp35)
    ap36 = kkdata.objects.get(word=bp36)
    ap37 = kkdata.objects.get(word=bp37)
    ap38 = kkdata.objects.get(word=bp38)
    ap39 = kkdata.objects.get(word=bp39)
    ap40 = kkdata.objects.get(word=bp40)
    ap41 = kkdata.objects.get(word=bp41)
    ap42 = kkdata.objects.get(word=bp42)
    ap43 = kkdata.objects.get(word=bp43)
    ap44 = kkdata.objects.get(word=bp44)
    ap45 = kkdata.objects.get(word=bp45)
    ap46 = kkdata.objects.get(word=bp46)
    ap47 = kkdata.objects.get(word=bp47)
    ap48 = kkdata.objects.get(word=bp48)
    ap49 = kkdata.objects.get(word=bp49)
    ap50 = kkdata.objects.get(word=bp50)
    ap51 = kkdata.objects.get(word=bp51)
    ap52 = kkdata.objects.get(word=bp52)
    ap53 = kkdata.objects.get(word=bp53)
    ap54 = kkdata.objects.get(word=bp54)

    ep0 = kkdata.objects.get(word=cp0)
    ep1 = kkdata.objects.get(word=cp1)
    ep2 = kkdata.objects.get(word=cp2)
    ep3 = kkdata.objects.get(word=cp3)
    ep4 = kkdata.objects.get(word=cp4)
    ep5 = kkdata.objects.get(word=cp5)
    ep6 = kkdata.objects.get(word=cp6)
    ep7 = kkdata.objects.get(word=cp7)
    ep8 = kkdata.objects.get(word=cp8)
    ep9 = kkdata.objects.get(word=cp9)
    ep10 = kkdata.objects.get(word=cp10)
    ep11 = kkdata.objects.get(word=cp11)
    ep12 = kkdata.objects.get(word=cp12)
    ep13 = kkdata.objects.get(word=cp13)
    ep14 = kkdata.objects.get(word=cp14)
    ep15 = kkdata.objects.get(word=cp15)
    ep16 = kkdata.objects.get(word=cp16)
    ep17 = kkdata.objects.get(word=cp17)
    ep18 = kkdata.objects.get(word=cp18)
    ep19 = kkdata.objects.get(word=cp19)
    ep20 = kkdata.objects.get(word=cp20)
    ep21 = kkdata.objects.get(word=cp21)  
    ep22 = kkdata.objects.get(word=cp22)
    ep23 = kkdata.objects.get(word=cp23)
    ep24 = kkdata.objects.get(word=cp24)
    ep25 = kkdata.objects.get(word=cp25)
    ep26 = kkdata.objects.get(word=cp26)
    ep27 = kkdata.objects.get(word=cp27)
    ep28 = kkdata.objects.get(word=cp28)
    ep29 = kkdata.objects.get(word=cp29)
    ep30 = kkdata.objects.get(word=cp30)
    ep31 = kkdata.objects.get(word=cp31)
    ep32 = kkdata.objects.get(word=cp32)
    ep33 = kkdata.objects.get(word=cp33)
    ep34 = kkdata.objects.get(word=cp34)
    ep35 = kkdata.objects.get(word=cp35)
    ep36 = kkdata.objects.get(word=cp36)
    ep37 = kkdata.objects.get(word=cp37)
    ep38 = kkdata.objects.get(word=cp38)
    ep39 = kkdata.objects.get(word=cp39)
    ep40 = kkdata.objects.get(word=cp40)
    ep41 = kkdata.objects.get(word=cp41)
    ep42 = kkdata.objects.get(word=cp42)
    ep43 = kkdata.objects.get(word=cp43)
    ep44 = kkdata.objects.get(word=cp44)
    ep45 = kkdata.objects.get(word=cp45)
    ep46 = kkdata.objects.get(word=cp46)
    ep47 = kkdata.objects.get(word=cp47)
    ep48 = kkdata.objects.get(word=cp48)
    ep49 = kkdata.objects.get(word=cp49)
    ep50 = kkdata.objects.get(word=cp50)
    ep51 = kkdata.objects.get(word=cp51)
    ep52 = kkdata.objects.get(word=cp52)
    ep53 = kkdata.objects.get(word=cp53)
    ep54 = kkdata.objects.get(word=cp54)
    
    posttest = member.posttestspeaking_set.all()#all of the use answer
    qunp=member.posttestspeaking_set.count()
    scorep=0
    wmp=[]
    
    for p in range(qunp):
        if posttest[p].vocabulary!=posttest[p].answer:
            scorep+=1#how many wrong answer user do
	    wmp.append(p)#wrong answer(number-1) user done(array)

    for g in wmp:
        locals()["trep%s" % (g)]=[]#topic kk scrach
        locals()["urep%s" % (g)]=[]#user's kk scrach
	locals()["trp%s" % (g)]=[]#tre+@
	locals()["urp%s" % (g)]=[]#ure+@
        locals()["tvowelp%s" % (g)]=[]#split topic kk scrach
	locals()["uvowelp%s" % (g)]=[]#split user's kk scrach
	locals()["tlocap%s" % (g)]=[]#topic vowel location
	locals()["ulocap%s" % (g)]=[]#user vowel location
	locals()["tnump%s" % (g)]=[]
        locals()["unump%s" % (g)]=[]
	locals()["tcomp%s" % (g)]=[]#topic vowel number
	locals()["ucomp%s" % (g)]=[]#topic vowel number

    tmp=[]
    ump=[]
    for q in wmp:
	locals()["tcomp%s" % (q)].append(len(locals()["ep%s" % (q)].kk))
	locals()["ucomp%s" % (q)].append(len(locals()["ap%s" % (q)].kk))
        tmp.append(len(locals()["ep%s" % (q)].kk))#topic kk amount list
        ump.append(len(locals()["ap%s" % (q)].kk))#user's kk amount list

    tmqp=len(tmp)#user's mistake amount

    for j in range(tmqp):
        for h in range(tmp[j]):
            locals()["trep%s" % (wmp[j])].append(locals()["ep%s" % (wmp[j])].kk[h].encode("utf-8"))
	    locals()["trp%s" % (wmp[j])].append(locals()["ep%s" % (wmp[j])].kk[h].encode("utf-8"))
        for s in range(ump[j]):
            locals()["urep%s" % (wmp[j])].append(locals()["ap%s" % (wmp[j])].kk[s].encode("utf-8"))
	    locals()["urp%s" % (wmp[j])].append(locals()["ap%s" % (wmp[j])].kk[s].encode("utf-8"))

    for m in range(tmqp):
	for n in range(tmp[m]):
	    for y in phone:
	        if locals()["trep%s" % (wmp[m])][n].find(y)!=-1:
		    locals()["tvowelp%s" % (wmp[m])].append(y)
		    locals()["tlocap%s" % (wmp[m])].append(n)
		    locals()["tnump%s" % (wmp[m])].append(n)

    for zz in range(tmqp):
	for yy in range(ump[zz]):
	    for xx in phone:
		if locals()["urep%s" % (wmp[zz])][yy].find(xx)!=-1:
		    locals()["uvowelp%s" % (wmp[zz])].append(xx)
		    locals()["ulocap%s" % (wmp[zz])].append(yy)
		    locals()["unump%s" % (wmp[zz])].append(yy)

    """ll=["|"]
    wv=["母音不正確"]
    more=["多念了"]
    less=["少念了"]
    into=["念錯成"]
    intt=["@"]
    to=["→"]"""
    statp=[] #唸錯成甚麼
    lmp=[] #多念少念
    
    for ii in wmp:
	if locals()["tlocap%s" % (ii)]==locals()["ulocap%s" % (ii)] and locals()["tvowelp%s" % (ii)]==locals()["uvowelp%s" % (ii)]:
	    if len(locals()["trep%s" % (ii)])>len(locals()["urep%s" % (ii)]):
		while len(locals()["trp%s" % (ii)])-len(locals()["urp%s" % (ii)])!=0:
		    locals()["urp%s" % (ii)]+=intt
	    elif len(locals()["trep%s" % (ii)])<len(locals()["urep%s" % (ii)]):
		while len(locals()["urp%s" % (ii)])-len(locals()["trp%s" % (ii)])!=0:
		    locals()["trp%s" % (ii)]+=intt
		

    for ww in wmp:
	if locals()["tlocap%s" % (ww)]==locals()["ulocap%s" % (ww)]:
	    if locals()["tvowelp%s" % (ww)]==locals()["uvowelp%s" % (ww)]:
	 	for kk in range(len(locals()["trp%s" % (ww)])):
		    if locals()["trp%s" % (ww)][kk]!=locals()["urp%s" % (ww)][kk]:
		        if locals()["trp%s" % (ww)][kk]=="@":
		    	    lmp+=more+[locals()["urp%s" % (ww)][kk]]+ll
		        elif locals()["urp%s" % (ww)][kk]=="@":
			    lmp+=less+[locals()["urp%s" % (ww)][kk]]+ll
			else:
			    statp.append([locals()["trp%s" % (ww)][kk]+"→"+locals()["urp%s" % (ww)][kk]])
	    else:
	        statp.append([x for x in locals()["tvowelp%s" % (ww)] if x not in locals()["uvowelp%s" % (ww)]]+to+[x for x in locals()["uvowelp%s" % (ww)] if x not in locals()["tvowelp%s" % (ww)]])     

    statisticp=[] #mistake list after filter

    for oo in statp:
	if not oo in statisticp:
	    statisticp.append(oo)
    #filter the repeat couple

    statnump=len(statisticp) #number of mistake after filter
    nump=[] #mistake times list 
    num_sortp=[] #mistake times list after sort
    locap=[] #mistake location list after sort

    for rr in range(statnump):
	locals()["statisnump%s" % (rr)]=statp.count(statisticp[rr])
	nump.append(statp.count(statisticp[rr]))

    while(nump.count(0)!=len(nump)):
	max_indxp=nump.index(max(nump))
	locap.append(max_indxp)
	num_sortp.append(nump[max_indxp])
	nump.pop(max_indxp)
	nump.insert(max_indxp, 0)
	#sort the mistakestatis

    for pp in locap:
	locals()["stp%s" % (pp)]=statp[pp]

    for ee in range(statnump):
	locals()["statisnummp%s" % (ee)]=num_sortp[ee]

    for tt in range(statnump):
        locals()["statisnup%s" % (tt)]=["次數："]+[locals()["statisnummp%s" % (tt)]]
    

    return render_to_response('mistakestatis.html',locals())

def pretestspeaking1(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic1#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking2/')

    return render_to_response('pre-testspeaking1.html',RequestContext(request,locals()))

def pretestspeaking2(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic2#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking3/')
    
    return render_to_response('pre-testspeaking2.html',RequestContext(request,locals()))

def pretestspeaking3(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic3#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking4/')

    return render_to_response('pre-testspeaking3.html',RequestContext(request,locals()))

def pretestspeaking4(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic4#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking5/')

    return render_to_response('pre-testspeaking4.html',RequestContext(request,locals()))

def pretestspeaking5(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic5#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking6/')

    return render_to_response('pre-testspeaking5.html',RequestContext(request,locals()))

def pretestspeaking6(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic6#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking7/')

    return render_to_response('pre-testspeaking6.html',RequestContext(request,locals()))

def pretestspeaking7(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic7#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking8/')

    return render_to_response('pre-testspeaking7.html',RequestContext(request,locals()))

def pretestspeaking8(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic8#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking9/')

    return render_to_response('pre-testspeaking8.html',RequestContext(request,locals()))

def pretestspeaking9(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic9#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking10/')

    return render_to_response('pre-testspeaking9.html',RequestContext(request,locals()))

def pretestspeaking10(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic10#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking11/')

    return render_to_response('pre-testspeaking10.html',RequestContext(request,locals()))

def pretestspeaking11(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic11#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking12/')

    return render_to_response('pre-testspeaking11.html',RequestContext(request,locals()))

def pretestspeaking12(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic12#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking13/')

    return render_to_response('pre-testspeaking12.html',RequestContext(request,locals()))

def pretestspeaking13(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic13#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking14/')

    return render_to_response('pre-testspeaking13.html',RequestContext(request,locals()))

def pretestspeaking14(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic14#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking15/')

    return render_to_response('pre-testspeaking14.html',RequestContext(request,locals()))

def pretestspeaking15(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic15#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking16/')

    return render_to_response('pre-testspeaking15.html',RequestContext(request,locals()))

def pretestspeaking16(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic16#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking17/')

    return render_to_response('pre-testspeaking16.html',RequestContext(request,locals()))

def pretestspeaking17(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic17#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking18/')

    return render_to_response('pre-testspeaking17.html',RequestContext(request,locals()))

def pretestspeaking18(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic18#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking19/')

    return render_to_response('pre-testspeaking18.html',RequestContext(request,locals()))

def pretestspeaking19(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic19#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking20/')

    return render_to_response('pre-testspeaking19.html',RequestContext(request,locals()))

def pretestspeaking20(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic20#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking21/')

    return render_to_response('pre-testspeaking20.html',RequestContext(request,locals()))

def pretestspeaking21(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic21#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking22/')

    return render_to_response('pre-testspeaking21.html',RequestContext(request,locals()))

def pretestspeaking22(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic22#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking23/')

    return render_to_response('pre-testspeaking22.html',RequestContext(request,locals()))

def pretestspeaking23(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic23#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking24/')

    return render_to_response('pre-testspeaking23.html',RequestContext(request,locals()))

def pretestspeaking24(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic24#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking25/')

    return render_to_response('pre-testspeaking24.html',RequestContext(request,locals()))

def pretestspeaking25(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic25#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking26/')

    return render_to_response('pre-testspeaking25.html',RequestContext(request,locals()))

def pretestspeaking26(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic26#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking27/')

    return render_to_response('pre-testspeaking26.html',RequestContext(request,locals()))

def pretestspeaking27(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic27#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking28/')

    return render_to_response('pre-testspeaking27.html',RequestContext(request,locals()))

def pretestspeaking28(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic28#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking29/')

    return render_to_response('pre-testspeaking28.html',RequestContext(request,locals()))

def pretestspeaking29(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic29#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking30/')

    return render_to_response('pre-testspeaking29.html',RequestContext(request,locals()))

def pretestspeaking30(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic30#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking31/')

    return render_to_response('pre-testspeaking30.html',RequestContext(request,locals()))

def pretestspeaking31(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic31#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking32/')

    return render_to_response('pre-testspeaking31.html',RequestContext(request,locals()))

def pretestspeaking32(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic32#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking33/')

    return render_to_response('pre-testspeaking32.html',RequestContext(request,locals()))

def pretestspeaking33(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic33#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking34/')

    return render_to_response('pre-testspeaking33.html',RequestContext(request,locals()))

def pretestspeaking34(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic34#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking35/')

    return render_to_response('pre-testspeaking34.html',RequestContext(request,locals()))

def pretestspeaking35(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic35#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking36/')

    return render_to_response('pre-testspeaking35.html',RequestContext(request,locals()))

def pretestspeaking36(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic36#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking37/')

    return render_to_response('pre-testspeaking36.html',RequestContext(request,locals()))

def pretestspeaking37(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic37#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking38/')

    return render_to_response('pre-testspeaking37.html',RequestContext(request,locals()))

def pretestspeaking38(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic38#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking39/')

    return render_to_response('pre-testspeaking38.html',RequestContext(request,locals()))

def pretestspeaking39(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic39#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel
    
    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking40/')

    return render_to_response('pre-testspeaking39.html',RequestContext(request,locals()))

def pretestspeaking40(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic40#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking41/')

    return render_to_response('pre-testspeaking40.html',RequestContext(request,locals()))

def pretestspeaking41(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic41#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking42/')

    return render_to_response('pre-testspeaking41.html',RequestContext(request,locals()))

def pretestspeaking42(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic42#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking43/')

    return render_to_response('pre-testspeaking42.html',RequestContext(request,locals()))

def pretestspeaking43(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic43#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking44/')

    return render_to_response('pre-testspeaking43.html',RequestContext(request,locals()))

def pretestspeaking44(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic44#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking45/')

    return render_to_response('pre-testspeaking44.html',RequestContext(request,locals()))

def pretestspeaking45(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic45#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking46/')

    return render_to_response('pre-testspeaking45.html',RequestContext(request,locals()))

def pretestspeaking46(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic46#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking47/')

    return render_to_response('pre-testspeaking46.html',RequestContext(request,locals()))

def pretestspeaking47(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic47#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking48/')

    return render_to_response('pre-testspeaking47.html',RequestContext(request,locals()))

def pretestspeaking48(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic48#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking49/')

    return render_to_response('pre-testspeaking48.html',RequestContext(request,locals()))

def pretestspeaking49(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic49#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking50/')

    return render_to_response('pre-testspeaking49.html',RequestContext(request,locals()))

def pretestspeaking50(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic50#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking51/')

    return render_to_response('pre-testspeaking50.html',RequestContext(request,locals()))

def pretestspeaking51(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic51#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking52/')

    return render_to_response('pre-testspeaking51.html',RequestContext(request,locals()))

def pretestspeaking52(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic52#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking53/')

    return render_to_response('pre-testspeaking52.html',RequestContext(request,locals()))

def pretestspeaking53(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic53#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking54/')

    return render_to_response('pre-testspeaking53.html',RequestContext(request,locals()))

def pretestspeaking54(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic54#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeaking55/')

    return render_to_response('pre-testspeaking54.html',RequestContext(request,locals()))

def pretestspeaking55(request):
    member = User.objects.get(username=request.user)
    test21 = pretestscratch.objects.get(user_id=member.id)
    ee = test21.topic55#print topic
    v = database.objects.get(vocabulary=ee)#print topic vowel

    if request.method == "POST":
       topic=request.POST['topic']
       answer=request.POST['textbox']
       vowel=request.POST['kk']
       user=request.POST['user']
       time = timezone.localtime(timezone.now())
       r = User.objects.get(id=user)
       f = pretestspeaking(vocabulary=topic, answer=answer, vowel=vowel, time=time, user=r)
       f.save()
       return HttpResponseRedirect('/pretestspeakinglist/')

    return render_to_response('pre-testspeaking55.html',RequestContext(request,locals()))


# Create your views here.
