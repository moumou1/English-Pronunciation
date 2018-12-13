from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from voc.models import lesson, vocabulary, record, history, kkdata
from django.contrib.auth.models import User
from django.db import connection
from django.utils import timezone
from django.contrib.sessions.models import Session 



def session_test(request):
    sid = request.COOKIES['sessionid']
    sid2 = request.session.session_key
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid + '<br>SessionID2:' + sid2 + '<br>Expire_date:' + str(s.expire_date) + '<br>Data:' + str(s.get_decoded())
    
    return HttpResponse(s_info)

def test(request):
    var_user=request.user

    cursor = connection.cursor()
    cursor.execute('''
	SELECT voc_kkdata.word,voc_kkdata.kk 
	FROM voc_kkdata 
	INNER JOIN voc_record ON voc_kkdata.word = voc_record.answer1 
	WHERE voc_record.username = %s
    ''', [var_user])
#   cursors = connection.cursor()
#   cursors.execute("""
#         SELECT voc_record.username,voc_kkdata.name,voc_kkdata.kk 
#         FROM voc_kkdata INNER JOIN voc_record 
#         ON voc_kkdata.name = voc_record.answer1
#   """)

    names = [result for result in cursor.fetchall()]


#    namess = [result for result in cursors.fetchall()]
    if request.POST:
	wordss = request.POST['words']
        mer = kkdata.objects.get(word=wordss)

    return render_to_response('test.html',RequestContext(request, locals()))
#{'names':names})    

def list_lesson(request):
    lessons = lesson.objects.all()
    return render_to_response('lesson_list.html',locals())

def lessons(request,id):
    if id:
        vocc = lesson.objects.get(id=id)
        return render_to_response('lessons.html',locals())
    else:
        return HttpResponseRedirect("/lesson_list/")    

def result_lesson(request,id):
    if id: 
        mems = record.objects.get(id=id)
	qq = lesson.objects.get(name=mems.lessons)
        return render_to_response('result_lesson.html',locals())
    else:
        return HttpResponseRedirect("/lesson_list/")        

def result(request):
        member = User.objects.get(username=request.user)
        memm = member.record_set.all()
        his = member.history_set.all()
	return render_to_response('result.html',locals()) 

def result_history(request,id):
    if id:
        mems = history.objects.get(id=id)
	return render_to_response('result_history.html',locals())
    else:
	return HttpResponseRedirect("/lesson_list/")

def historys(request,id):
    if id:
         vocc = lesson.objects.get(id=id)
         member = User.objects.get(username=request.user)
    else:
        return HttpResponseRedirct("/lesson_list/")
    if request.POST:
        username = request.POST['username']
        course = request.POST['course']
        to1 = request.POST['topic1']
        to2 = request.POST['topic2']
        to3 = request.POST['topic3']
        to4 = request.POST['topic4']
        to5 = request.POST['topic5']
        to6 = request.POST['topic6']
        to7 = request.POST['topic7']
        to8 = request.POST['topic8']
        to9 = request.POST['topic9']
        to10 = request.POST['topic10']
        to11 = request.POST['topic11']
        to12 = request.POST['topic12']
        to13 = request.POST['topic13']
        to14 = request.POST['topic14']
        to15 = request.POST['topic15']
        to16 = request.POST['topic16']
        to17 = request.POST['topic17']
        to18 = request.POST['topic18']
        to19 = request.POST['topic19']
        to20 = request.POST['topic20']
        to21 = request.POST['topic21']
        to22 = request.POST['topic22']
        to23 = request.POST['topic23']
        to24 = request.POST['topic24']
        to25 = request.POST['topic25']
        to26 = request.POST['topic26']
        to27 = request.POST['topic27']
        to28 = request.POST['topic28']
        to29 = request.POST['topic29']
        to30 = request.POST['topic30']
        his1 = request.POST['history1']
        his2 = request.POST['history2'] 
        his3 = request.POST['history3'] 
        his4 = request.POST['history4'] 
        his5 = request.POST['history5'] 
        his6 = request.POST['history6'] 
        his7 = request.POST['history7'] 
        his8 = request.POST['history8'] 
        his9 = request.POST['history9'] 
        his10 = request.POST['history10'] 
        his11 = request.POST['history11'] 
        his12 = request.POST['history12'] 
        his13 = request.POST['history13'] 
        his14 = request.POST['history14'] 
        his15 = request.POST['history15'] 
        his16 = request.POST['history16'] 
        his17 = request.POST['history17'] 
        his18 = request.POST['history18'] 
        his19 = request.POST['history19'] 
        his20 = request.POST['history20'] 
        his21 = request.POST['history21'] 
        his22 = request.POST['history22'] 
        his23 = request.POST['history23'] 
        his24 = request.POST['history24'] 
        his25 = request.POST['history25'] 
        his26 = request.POST['history26'] 
        his27 = request.POST['history27'] 
        his28 = request.POST['history28'] 
        his29 = request.POST['history29'] 
        his30 = request.POST['history30']
        mem = request.POST['member']

        history.objects.create(
             username=username,
             course=course,
	     topic1=to1,
             topic2=to2,
             topic3=to3,
             topic4=to4,
             topic5=to5,
             topic6=to6,
             topic7=to7,
             topic8=to8,
             topic9=to9,
             topic10=to10,
             topic11=to11,
             topic12=to12,
             topic13=to13,
             topic14=to14,
             topic15=to15,
             topic16=to16,
             topic17=to17,
             topic18=to18,
             topic19=to19,
             topic20=to20,
             topic21=to21,
             topic22=to22,
             topic23=to23,
             topic24=to24,
             topic25=to25,
             topic26=to26,
             topic27=to27,
             topic28=to28,
             topic29=to29,
             topic30=to30,
	     history1=his1,
             history2=his2,
             history3=his3,
             history4=his4,
             history5=his5,
             history6=his6,
             history7=his7,
             history8=his8,
             history9=his9,
             history10=his10,
             history11=his11,
             history12=his12,
             history13=his13,
             history14=his14,
             history15=his15,
             history16=his16,
             history17=his17,
             history18=his18,
             history19=his19,
             history20=his20,
             history21=his21,
             history22=his22,
             history23=his23,
             history24=his24,
             history25=his25,
             history26=his26,
             history27=his27,
             history28=his28,
             history29=his29,
             history30=his30,
             vocaa_id=mem
       )
    return render_to_response('history.html',RequestContext(request,locals()))
            
def stt(request,id):
    if id:
         vocc = lesson.objects.get(id=id)
         member = User.objects.get(username=request.user)
    else:
        return HttpResponseRedirct("/lesson_list/")
    if request.method=='POST' and 'button1' in request.POST:
	  an1 = request.POST['answer1']
          an2 = request.POST['answer2']
          an3 = request.POST['answer3']
          an4 = request.POST['answer4']
          an5 = request.POST['answer5']
          an6 = request.POST['answer6']
          an7 = request.POST['answer7']
          an8 = request.POST['answer8']
          an9 = request.POST['answer9']
          an10 = request.POST['answer10']
          an11 = request.POST['answer11']
          an12 = request.POST['answer12']
          an13 = request.POST['answer13']
          an14 = request.POST['answer14']
          an15 = request.POST['answer15']
          an16 = request.POST['answer16']
          an17 = request.POST['answer17']
          an18 = request.POST['answer18']
          an19 = request.POST['answer19']
          an20 = request.POST['answer20']
          an21 = request.POST['answer21']
          an22 = request.POST['answer22']
          an23 = request.POST['answer23']
          an24 = request.POST['answer24']
          an25 = request.POST['answer25']
          an26 = request.POST['answer26']
          an27 = request.POST['answer27']
          an28 = request.POST['answer28']
          an29 = request.POST['answer29']
          an30 = request.POST['answer30']

	  transform1 = kkdata.objects.get(word=an1)
	  transform2 = kkdata.objects.get(word=an2)
	  transform3 = kkdata.objects.get(word=an3)
	  transform4 = kkdata.objects.get(word=an4)
	  transform5 = kkdata.objects.get(word=an5)
	  transform6 = kkdata.objects.get(word=an6)
	  transform7 = kkdata.objects.get(word=an7)
	  transform8 = kkdata.objects.get(word=an8)
	  transform9 = kkdata.objects.get(word=an9)
	  transform10 = kkdata.objects.get(word=an10)
	  transform11 = kkdata.objects.get(word=an11)
	  transform12 = kkdata.objects.get(word=an12)
	  transform13 = kkdata.objects.get(word=an13)
	  transform14 = kkdata.objects.get(word=an14)
	  transform15 = kkdata.objects.get(word=an15)
	  transform16 = kkdata.objects.get(word=an16)
	  transform17 = kkdata.objects.get(word=an17)
 	  transform18 = kkdata.objects.get(word=an18)
	  transform19 = kkdata.objects.get(word=an19)
	  transform20 = kkdata.objects.get(word=an20)
	  transform21 = kkdata.objects.get(word=an21)
	  transform22 = kkdata.objects.get(word=an22)
	  transform23 = kkdata.objects.get(word=an23)	
	  transform24 = kkdata.objects.get(word=an24)
	  transform25 = kkdata.objects.get(word=an25)
	  transform26 = kkdata.objects.get(word=an26)
	  transform27 = kkdata.objects.get(word=an27)
 	  transform28 = kkdata.objects.get(word=an28)
	  transform29 = kkdata.objects.get(word=an29)
	  transform30 = kkdata.objects.get(word=an30)
    if request.method=='POST' and 'button2' in request.POST:
        user = request.POST['username']
        re1 = request.POST['result1']
        re2 = request.POST['result2'] 
        re3 = request.POST['result3'] 
        re4 = request.POST['result4'] 
        re5 = request.POST['result5'] 
        re6 = request.POST['result6'] 
        re7 = request.POST['result7'] 
        re8 = request.POST['result8'] 
        re9 = request.POST['result9'] 
        re10 = request.POST['result10'] 
        re11 = request.POST['result11'] 
        re12 = request.POST['result12'] 
        re13 = request.POST['result13'] 
        re14 = request.POST['result14']          
        re15 = request.POST['result15'] 
        re16 = request.POST['result16'] 
        re17 = request.POST['result17'] 
        re18 = request.POST['result18'] 
        re19 = request.POST['result19'] 
        re20 = request.POST['result20'] 
        re21 = request.POST['result21'] 
        re22 = request.POST['result22'] 
        re23 = request.POST['result23'] 
        re24 = request.POST['result24'] 
        re25 = request.POST['result25'] 
        re26 = request.POST['result26'] 
        re27 = request.POST['result27'] 
        re28 = request.POST['result28'] 
        re29 = request.POST['result29'] 
        re30 = request.POST['result30']
        an1 = request.POST['answer1']
        an2 = request.POST['answer2']
        an3 = request.POST['answer3']
        an4 = request.POST['answer4']
        an5 = request.POST['answer5']
        an6 = request.POST['answer6']  
        an7 = request.POST['answer7']
        an8 = request.POST['answer8']
        an9 = request.POST['answer9']
        an10 = request.POST['answer10']
        an11 = request.POST['answer11']
        an12 = request.POST['answer12']
        an13 = request.POST['answer13']
        an14 = request.POST['answer14']
        an15 = request.POST['answer15']
        an16 = request.POST['answer16']
        an17 = request.POST['answer17']
        an18 = request.POST['answer18']
        an19 = request.POST['answer19']
        an20 = request.POST['answer20']
        an21 = request.POST['answer21']
        an22 = request.POST['answer22']	
        an23 = request.POST['answer23']
        an24 = request.POST['answer24']
        an25 = request.POST['answer25']
        an26 = request.POST['answer26']
        an27 = request.POST['answer27']
        an28 = request.POST['answer28']
        an29 = request.POST['answer29']
        an30 = request.POST['answer30']
	so = request.POST['score']
        mem = request.POST['member']
	use = request.POST['vocaa']
        
	#transform1 = kkdata.objects.get(word=an1)
        #transform2 = kkdata.objects.get(word=an2)
        #transform3 = kkdata.objects.get(word=an3)
        #transform4 = kkdata.objects.get(word=an4)
        #transform5 = kkdata.objects.get(word=an5)
        #transform6 = kkdata.objects.get(word=an6)
        #transform7 = kkdata.objects.get(word=an7)
        #transform8 = kkdata.objects.get(word=an8)
        #transform9 = kkdata.objects.get(word=an9)
        #transform10 = kkdata.objects.get(word=an10)
        #transform11 = kkdata.objects.get(word=an11)
        #transform12 = kkdata.objects.get(word=an12)
        #transform13 = kkdata.objects.get(word=an13)
        #transform14 = kkdata.objects.get(word=an14)
        #transform15 = kkdata.objects.get(word=an15)
        #transform16 = kkdata.objects.get(word=an16)
        #transform17 = kkdata.objects.get(word=an17)
        #transform18 = kkdata.objects.get(word=an18)
        #transform19 = kkdata.objects.get(word=an19)
        #transform20 = kkdata.objects.get(word=an20)
        #transform21 = kkdata.objects.get(word=an21)
        #transform22 = kkdata.objects.get(word=an22)
        #transform23 = kkdata.objects.get(word=an23)
        #transform24 = kkdata.objects.get(word=an24)
        #transform25 = kkdata.objects.get(word=an25)
        #transform26 = kkdata.objects.get(word=an26)
        #transform27 = kkdata.objects.get(word=an27)
        #transform28 = kkdata.objects.get(word=an28)
        #transform29 = kkdata.objects.get(word=an29)
        #transform30 = kkdata.objects.get(word=an30)
        record.objects.create(
	     username=user,
             result1=re1,       
             result2=re2,
             result3=re3,
             result4=re4,
             result5=re5,
             result6=re6,
             result7=re7,
             result8=re8,
             result9=re9,
             result10=re10,
             result11=re11,
             result12=re12,
             result13=re13,
             result14=re14,
             result15=re15,
             result16=re16,
             result17=re17,
             result18=re18,
             result19=re19,
             result20=re20,
             result21=re21,
             result22=re22,
             result23=re23,
             result24=re24,
             result25=re25,
             result26=re26,
             result27=re27,
             result28=re28,
             result29=re29,
             result30=re30,
	     answer1=an1,
             answer2=an2,
             answer3=an3,
             answer4=an4,
             answer5=an5,
             answer6=an6,
             answer7=an7,
             answer8=an8,
             answer9=an9,
             answer10=an10,
             answer11=an11,
             answer12=an12,
             answer13=an13,
             answer14=an14,
             answer15=an15,
             answer16=an16,
             answer17=an17,
             answer18=an18,
             answer19=an19,
             answer20=an20,
             answer21=an21,
             answer22=an22,
             answer23=an23,
             answer24=an24,
             answer25=an25,
             answer26=an26,
             answer27=an27,
             answer28=an28,
             answer29=an29,
             answer30=an30,
	     score=so,
             users_id=mem,
	     lessons_id=use
       )
    return render_to_response('stt.html',RequestContext(request,locals()))
# Create your views here.
