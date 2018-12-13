from django.contrib import admin
from voc.models import lesson, vocabulary, history, record, kkdata

class kkdataAdmin(admin.ModelAdmin):
    list_display = ('word', 'kk')

class lessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')

class vocabularyAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'kk', 'pos', 'tran', 'sen', 'voca')

class historyAdmin(admin.ModelAdmin):
    list_display = ('username', 'course', 'topic1', 'topic2', 'topic3', 'topic4', 'topic5', 'topic6', 'topic7', 'topic8', 'topic9', 'topic10', 'topic11', 'topic12', 'topic13', 'topic14', 'topic15', 'topic16', 'topic17', 'topic18', 'topic19', 'topic20', 'topic21', 'topic22', 'topic23', 'topic24', 'topic25', 'topic26', 'topic27', 'topic28', 'topic29', 'topic30', 'history1', 'history2', 'history3', 'history4', 'history5', 'history6', 'history7', 'history8', 'history9', 'history10', 'history11', 'history12', 'history13', 'history14', 'history15', 'history16', 'history17', 'history18', 'history19', 'history20', 'history21', 'history22', 'history23', 'history24', 'history25', 'history26', 'history27', 'history28', 'history29', 'history30')
class recordAdmin(admin.ModelAdmin):
    list_display = ('username', 'result1', 'result2', 'result3', 'result4', 'result5', 'result6', 'result7', 'result8', 'result9', 'result10', 'result11', 'result12', 'result13', 'result14', 'result15', 'result16', 'result17', 'result18', 'result19', 'result20', 'result21', 'result22', 'result23', 'result24', 'result25', 'result26', 'result27', 'result28', 'result29', 'result30', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8', 'answer9', 'answer10', 'answer11', 'answer12', 'answer13', 'answer14', 'answer15', 'answer16', 'answer17', 'answer18', 'answer19', 'answer20', 'answer21', 'answer22', 'answer23', 'answer24', 'answer25', 'answer26', 'answer27', 'answer28', 'answer29', 'answer30',  'score', 'users', 'lessons')

#    search_fields = ('name')
    
admin.site.register(lesson,lessonAdmin) 
admin.site.register(vocabulary,vocabularyAdmin)
admin.site.register(history,historyAdmin)
admin.site.register(record,recordAdmin)
admin.site.register(kkdata,kkdataAdmin)    
# Register your models here.

