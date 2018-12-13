from django.contrib import admin
from english.models import group, phoneme, database, pretestscratch, posttestscratch, exercisescratch, pretestspeaking, posttestspeaking, exercise, kkdata

class groupAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')

class phonemeAdmin(admin.ModelAdmin):
    list_display = ('vowel', 'packet')

class databaseAdmin(admin.ModelAdmin):
    list_display = ('vocabulary', 'vowel')

class pretestscratchAdmin(admin.ModelAdmin):
    list_display = ('topic1', 'topic2', 'topic3', 'topic4', 'topic5', 'topic6', 'topic7', 'topic8', 'topic9', 'topic10', 'topic11', 'topic12', 'topic13', 'topic14', 'topic15', 'topic16', 'topic17', 'topic18', 'topic19', 'topic20', 'topic21', 'topic22', 'topic23', 'topic24', 'topic25', 'topic26', 'topic27', 'topic28', 'topic29', 'topic30', 'topic31', 'topic32', 'topic33', 'topic34', 'topic35', 'topic36', 'topic37', 'topic38', 'topic39', 'topic40', 'topic41', 'topic42', 'topic43', 'topic44', 'topic45', 'topic46', 'topic47', 'topic48', 'topic49', 'topic50', 'topic51', 'topic52', 'topic53', 'topic54', 'topic55', 'user')

class posttestscratchAdmin(admin.ModelAdmin):
    list_display = ('topic1', 'topic2', 'topic3', 'topic4', 'topic5', 'topic6', 'topic7', 'topic8', 'topic9', 'topic10', 'topic11', 'topic12', 'topic13', 'topic14', 'topic15', 'topic16', 'topic17', 'topic18', 'topic19', 'topic20', 'topic21', 'topic22', 'topic23', 'topic24', 'topic25', 'topic26', 'topic27', 'topic28', 'topic29', 'topic30', 'topic31', 'topic32', 'topic33', 'topic34', 'topic35', 'topic36', 'topic37', 'topic38', 'topic39', 'topic40', 'topic41', 'topic42', 'topic43', 'topic44', 'topic45', 'topic46', 'topic47', 'topic48', 'topic49', 'topic50', 'topic51', 'topic52', 'topic53', 'topic54', 'topic55', 'user')

class exercisescratchAdmin(admin.ModelAdmin):
    list_display = ('topic1', 'topic2', 'topic3', 'topic4', 'topic5', 'topic6', 'topic7', 'topic8', 'topic9', 'topic10', 'topic11', 'topic12', 'topic13', 'topic14', 'topic15', 'topic16', 'topic17', 'topic18', 'topic19', 'topic20', 'user', 'groups')
class pretestspeakingAdmin(admin.ModelAdmin):
    list_display = ('vocabulary', 'answer', 'vowel', 'time', 'user')

class posttestspeakingAdmin(admin.ModelAdmin):
    list_display = ('vocabulary', 'answer', 'vowel', 'time', 'user')

class exerciseAdmin(admin.ModelAdmin):
    list_display = ('vocabulary', 'answer', 'history', 'user', 'groups')

class kkdataAdmin(admin.ModelAdmin):
    list_display = ('word', 'kk')

admin.site.register(group,groupAdmin)
admin.site.register(phoneme,phonemeAdmin) 
admin.site.register(database,databaseAdmin)
admin.site.register(pretestscratch,pretestscratchAdmin)
admin.site.register(posttestscratch,posttestscratchAdmin)
admin.site.register(exercisescratch,exercisescratchAdmin)
admin.site.register(pretestspeaking,pretestspeakingAdmin) 
admin.site.register(posttestspeaking,posttestspeakingAdmin)
admin.site.register(exercise,exerciseAdmin) 
admin.site.register(kkdata,kkdataAdmin)

# Register your models here.
