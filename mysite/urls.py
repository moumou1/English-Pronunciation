from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
#from test1.views import meta, welcome, session_test  
from voc.views import lessons, list_lesson, stt, result, result_lesson, historys, result_history, test, session_test
#from other.views import comment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^accounts/login/$', 'login'),
    url(r'^accounts/logout/$', 'logout'),
)
urlpatterns += patterns('mysite.views',
    url(r'^index/$', 'index'),
    url(r'^accounts/register/$', 'register'),    
)
urlpatterns += patterns('exercise.views',
    url(r'^exerciselista/$', 'exerciselista'),
    url(r'^exerciselistb/$', 'exerciselistb'),
    url(r'^exerciselistc/$', 'exerciselistc'),
    url(r'^exerciselistd/$', 'exerciselistd'),
    url(r'^exerciseliste/$', 'exerciseliste'),
    url(r'^exerciseoptions/$', 'exerciseoptions'),
    url(r'^exerciseresult/$', 'exerciseresult'),
    url(r'^exercisea1/$', 'exercisea1'),
    url(r'^exercisea2/$', 'exercisea2'),
    url(r'^exercisea3/$', 'exercisea3'),
    url(r'^exercisea4/$', 'exercisea4'),
    url(r'^exercisea5/$', 'exercisea5'),
    url(r'^exercisea6/$', 'exercisea6'),
    url(r'^exercisea7/$', 'exercisea7'),
    url(r'^exercisea8/$', 'exercisea8'),
    url(r'^exercisea9/$', 'exercisea9'),
    url(r'^exercisea10/$', 'exercisea10'),
    url(r'^exercisea11/$', 'exercisea11'),
    url(r'^exercisea12/$', 'exercisea12'),
    url(r'^exercisea13/$', 'exercisea13'),
    url(r'^exercisea14/$', 'exercisea14'),
    url(r'^exercisea15/$', 'exercisea15'),
    url(r'^exercisea16/$', 'exercisea16'),
    url(r'^exercisea17/$', 'exercisea17'),
    url(r'^exercisea18/$', 'exercisea18'),
    url(r'^exercisea19/$', 'exercisea19'),
    url(r'^exercisea20/$', 'exercisea20'),
    url(r'^exerciseb1/$', 'exerciseb1'),
    url(r'^exerciseb2/$', 'exerciseb2'),
    url(r'^exerciseb3/$', 'exerciseb3'),
    url(r'^exerciseb4/$', 'exerciseb4'),
    url(r'^exerciseb5/$', 'exerciseb5'),
    url(r'^exerciseb6/$', 'exerciseb6'),
    url(r'^exerciseb7/$', 'exerciseb7'),
    url(r'^exerciseb8/$', 'exerciseb8'),
    url(r'^exerciseb9/$', 'exerciseb9'),
    url(r'^exerciseb10/$', 'exerciseb10'),
    url(r'^exerciseb11/$', 'exerciseb11'),
    url(r'^exerciseb12/$', 'exerciseb12'),
    url(r'^exerciseb13/$', 'exerciseb13'),
    url(r'^exerciseb14/$', 'exerciseb14'),
    url(r'^exerciseb15/$', 'exerciseb15'),
    url(r'^exerciseb16/$', 'exerciseb16'),
    url(r'^exerciseb17/$', 'exerciseb17'),
    url(r'^exerciseb18/$', 'exerciseb18'),
    url(r'^exerciseb19/$', 'exerciseb19'),
    url(r'^exerciseb20/$', 'exerciseb20'),
    url(r'^exercisec1/$', 'exercisec1'),
    url(r'^exercisec2/$', 'exercisec2'),
    url(r'^exercisec3/$', 'exercisec3'),
    url(r'^exercisec4/$', 'exercisec4'),
    url(r'^exercisec5/$', 'exercisec5'),
    url(r'^exercisec6/$', 'exercisec6'),
    url(r'^exercisec7/$', 'exercisec7'),
    url(r'^exercisec8/$', 'exercisec8'),
    url(r'^exercisec9/$', 'exercisec9'),
    url(r'^exercisec10/$', 'exercisec10'),
    url(r'^exercisec11/$', 'exercisec11'),
    url(r'^exercisec12/$', 'exercisec12'),
    url(r'^exercisec13/$', 'exercisec13'),
    url(r'^exercisec14/$', 'exercisec14'),
    url(r'^exercisec15/$', 'exercisec15'),
    url(r'^exercisec16/$', 'exercisec16'),
    url(r'^exercisec17/$', 'exercisec17'),
    url(r'^exercisec18/$', 'exercisec18'),
    url(r'^exercisec19/$', 'exercisec19'),
    url(r'^exercisec20/$', 'exercisec20'),
    url(r'^exercised1/$', 'exercised1'),
    url(r'^exercised2/$', 'exercised2'),
    url(r'^exercised3/$', 'exercised3'),
    url(r'^exercised4/$', 'exercised4'),
    url(r'^exercised5/$', 'exercised5'),
    url(r'^exercised6/$', 'exercised6'),
    url(r'^exercised7/$', 'exercised7'),
    url(r'^exercised8/$', 'exercised8'),
    url(r'^exercised9/$', 'exercised9'),
    url(r'^exercised10/$', 'exercised10'),
    url(r'^exercised11/$', 'exercised11'),
    url(r'^exercised12/$', 'exercised12'),
    url(r'^exercised13/$', 'exercised13'),
    url(r'^exercised14/$', 'exercised14'),
    url(r'^exercised15/$', 'exercised15'),
    url(r'^exercised16/$', 'exercised16'),
    url(r'^exercised17/$', 'exercised17'),
    url(r'^exercised18/$', 'exercised18'),
    url(r'^exercised19/$', 'exercised19'),
    url(r'^exercised20/$', 'exercised20'),
    url(r'^exercisee1/$', 'exercisee1'),
    url(r'^exercisee2/$', 'exercisee2'),
    url(r'^exercisee3/$', 'exercisee3'),
    url(r'^exercisee4/$', 'exercisee4'),
    url(r'^exercisee5/$', 'exercisee5'),
    url(r'^exercisee6/$', 'exercisee6'),
    url(r'^exercisee7/$', 'exercisee7'),
    url(r'^exercisee8/$', 'exercisee8'),
    url(r'^exercisee9/$', 'exercisee9'),
    url(r'^exercisee10/$', 'exercisee10'),
    url(r'^exercisee11/$', 'exercisee11'),
    url(r'^exercisee12/$', 'exercisee12'),
    url(r'^exercisee13/$', 'exercisee13'),
    url(r'^exercisee14/$', 'exercisee14'),
    url(r'^exercisee15/$', 'exercisee15'),
    url(r'^exercisee16/$', 'exercisee16'),
    url(r'^exercisee17/$', 'exercisee17'),
    url(r'^exercisee18/$', 'exercisee18'),
    url(r'^exercisee19/$', 'exercisee19'),
    url(r'^exercisee20/$', 'exercisee20'),
)
urlpatterns += patterns('english.views',
    url(r'^pretestspeakinglist/$', 'pretestspeakinglist'),
    url(r'^mistakestatis/$', 'mistakestatis'),
    url(r'^pretestspeaking1/$', 'pretestspeaking1'),
    url(r'^pretestspeaking2/$', 'pretestspeaking2'),
    url(r'^pretestspeaking3/$', 'pretestspeaking3'),
    url(r'^pretestspeaking4/$', 'pretestspeaking4'),
    url(r'^pretestspeaking5/$', 'pretestspeaking5'),
    url(r'^pretestspeaking6/$', 'pretestspeaking6'),
    url(r'^pretestspeaking7/$', 'pretestspeaking7'),
    url(r'^pretestspeaking8/$', 'pretestspeaking8'),
    url(r'^pretestspeaking9/$', 'pretestspeaking9'),
    url(r'^pretestspeaking10/$', 'pretestspeaking10'),
    url(r'^pretestspeaking11/$', 'pretestspeaking11'),
    url(r'^pretestspeaking12/$', 'pretestspeaking12'),
    url(r'^pretestspeaking13/$', 'pretestspeaking13'),
    url(r'^pretestspeaking14/$', 'pretestspeaking14'),
    url(r'^pretestspeaking15/$', 'pretestspeaking15'),
    url(r'^pretestspeaking16/$', 'pretestspeaking16'),
    url(r'^pretestspeaking17/$', 'pretestspeaking17'),
    url(r'^pretestspeaking18/$', 'pretestspeaking18'),
    url(r'^pretestspeaking19/$', 'pretestspeaking19'),
    url(r'^pretestspeaking20/$', 'pretestspeaking20'),
    url(r'^pretestspeaking21/$', 'pretestspeaking21'),
    url(r'^pretestspeaking22/$', 'pretestspeaking22'),
    url(r'^pretestspeaking23/$', 'pretestspeaking23'),
    url(r'^pretestspeaking24/$', 'pretestspeaking24'),
    url(r'^pretestspeaking25/$', 'pretestspeaking25'),
    url(r'^pretestspeaking26/$', 'pretestspeaking26'),
    url(r'^pretestspeaking27/$', 'pretestspeaking27'),
    url(r'^pretestspeaking28/$', 'pretestspeaking28'),
    url(r'^pretestspeaking29/$', 'pretestspeaking29'),
    url(r'^pretestspeaking30/$', 'pretestspeaking30'),
    url(r'^pretestspeaking31/$', 'pretestspeaking31'),
    url(r'^pretestspeaking32/$', 'pretestspeaking32'),
    url(r'^pretestspeaking33/$', 'pretestspeaking33'),
    url(r'^pretestspeaking34/$', 'pretestspeaking34'),
    url(r'^pretestspeaking35/$', 'pretestspeaking35'),
    url(r'^pretestspeaking36/$', 'pretestspeaking36'),
    url(r'^pretestspeaking37/$', 'pretestspeaking37'),
    url(r'^pretestspeaking38/$', 'pretestspeaking38'),
    url(r'^pretestspeaking39/$', 'pretestspeaking39'),
    url(r'^pretestspeaking40/$', 'pretestspeaking40'),
    url(r'^pretestspeaking41/$', 'pretestspeaking41'),
    url(r'^pretestspeaking42/$', 'pretestspeaking42'),
    url(r'^pretestspeaking43/$', 'pretestspeaking43'),
    url(r'^pretestspeaking44/$', 'pretestspeaking44'),
    url(r'^pretestspeaking45/$', 'pretestspeaking45'),
    url(r'^pretestspeaking46/$', 'pretestspeaking46'),
    url(r'^pretestspeaking47/$', 'pretestspeaking47'),
    url(r'^pretestspeaking48/$', 'pretestspeaking48'),
    url(r'^pretestspeaking49/$', 'pretestspeaking49'),
    url(r'^pretestspeaking50/$', 'pretestspeaking50'),
    url(r'^pretestspeaking51/$', 'pretestspeaking51'),
    url(r'^pretestspeaking52/$', 'pretestspeaking52'),
    url(r'^pretestspeaking53/$', 'pretestspeaking53'),
    url(r'^pretestspeaking54/$', 'pretestspeaking54'),
    url(r'^pretestspeaking55/$', 'pretestspeaking55'),
)
urlpatterns += patterns('other.views',
    url(r'^indextest/$', 'indextest'),
    url(r'^posttestspeakinglist/$', 'posttestspeakinglist'),
    url(r'^posttestmistake/$', 'posttestmistake'),
    url(r'^posttestspeaking1/$', 'posttestspeaking1'),
    url(r'^posttestspeaking2/$', 'posttestspeaking2'),
    url(r'^posttestspeaking3/$', 'posttestspeaking3'),
    url(r'^posttestspeaking4/$', 'posttestspeaking4'),
    url(r'^posttestspeaking5/$', 'posttestspeaking5'),
    url(r'^posttestspeaking6/$', 'posttestspeaking6'),
    url(r'^posttestspeaking7/$', 'posttestspeaking7'),
    url(r'^posttestspeaking8/$', 'posttestspeaking8'),
    url(r'^posttestspeaking9/$', 'posttestspeaking9'),
    url(r'^posttestspeaking10/$', 'posttestspeaking10'),
    url(r'^posttestspeaking11/$', 'posttestspeaking11'),
    url(r'^posttestspeaking12/$', 'posttestspeaking12'),
    url(r'^posttestspeaking13/$', 'posttestspeaking13'),
    url(r'^posttestspeaking14/$', 'posttestspeaking14'),
    url(r'^posttestspeaking15/$', 'posttestspeaking15'),
    url(r'^posttestspeaking16/$', 'posttestspeaking16'),
    url(r'^posttestspeaking17/$', 'posttestspeaking17'),
    url(r'^posttestspeaking18/$', 'posttestspeaking18'),
    url(r'^posttestspeaking19/$', 'posttestspeaking19'),
    url(r'^posttestspeaking20/$', 'posttestspeaking20'),
    url(r'^posttestspeaking21/$', 'posttestspeaking21'),
    url(r'^posttestspeaking22/$', 'posttestspeaking22'),
    url(r'^posttestspeaking23/$', 'posttestspeaking23'),
    url(r'^posttestspeaking24/$', 'posttestspeaking24'),
    url(r'^posttestspeaking25/$', 'posttestspeaking25'),
    url(r'^posttestspeaking26/$', 'posttestspeaking26'),
    url(r'^posttestspeaking27/$', 'posttestspeaking27'),
    url(r'^posttestspeaking28/$', 'posttestspeaking28'),
    url(r'^posttestspeaking29/$', 'posttestspeaking29'),
    url(r'^posttestspeaking30/$', 'posttestspeaking30'),
    url(r'^posttestspeaking31/$', 'posttestspeaking31'),
    url(r'^posttestspeaking32/$', 'posttestspeaking32'),
    url(r'^posttestspeaking33/$', 'posttestspeaking33'),
    url(r'^posttestspeaking34/$', 'posttestspeaking34'),
    url(r'^posttestspeaking35/$', 'posttestspeaking35'),
    url(r'^posttestspeaking36/$', 'posttestspeaking36'),
    url(r'^posttestspeaking37/$', 'posttestspeaking37'),
    url(r'^posttestspeaking38/$', 'posttestspeaking38'),
    url(r'^posttestspeaking39/$', 'posttestspeaking39'),
    url(r'^posttestspeaking40/$', 'posttestspeaking40'),
    url(r'^posttestspeaking41/$', 'posttestspeaking41'),
    url(r'^posttestspeaking42/$', 'posttestspeaking42'),
    url(r'^posttestspeaking43/$', 'posttestspeaking43'),
    url(r'^posttestspeaking44/$', 'posttestspeaking44'),
    url(r'^posttestspeaking45/$', 'posttestspeaking45'),
    url(r'^posttestspeaking46/$', 'posttestspeaking46'),
    url(r'^posttestspeaking47/$', 'posttestspeaking47'),
    url(r'^posttestspeaking48/$', 'posttestspeaking48'),
    url(r'^posttestspeaking49/$', 'posttestspeaking49'),
    url(r'^posttestspeaking50/$', 'posttestspeaking50'),
    url(r'^posttestspeaking51/$', 'posttestspeaking51'),
    url(r'^posttestspeaking52/$', 'posttestspeaking52'),
    url(r'^posttestspeaking53/$', 'posttestspeaking53'),
    url(r'^posttestspeaking54/$', 'posttestspeaking54'),
    url(r'^posttestspeaking55/$', 'posttestspeaking55'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lessons/(\d{1,5})/$', lessons),
#    url(r'^meta/$', meta),
#    url(r'^welcome/$', welcome),
    url(r'^lesson_list/$', list_lesson),
    url(r'^session', session_test),
#    url(r'^index/$', index),
#    url(r'^accounts/register/$', register),
    url(r'^stt/(\d{1,5})/$', stt),
#    url(r'^comment/$', comment),
    url(r'^result/$', result),
    url(r'^result_lesson/(\d{1,5})/$', result_lesson),
    url(r'^historys/(\d{1,5})/$', historys),
    url(r'^result_history/(\d{1,5})/$', result_history),
    url(r'^test/$', test),
)