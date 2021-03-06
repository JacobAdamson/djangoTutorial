from django.conf.urls import url

from  . import views

app_name = 'polls' #needed for namespacing
urlpatterns = [
        # ex: /polls"
        url(r'^$', views.index, name = 'index'),
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
        
        # ex: /polls/5/
        url(r'^(?P<question_id>[0-9]+)/result/$', views.results, name = 'results'),
        
        # ex: /polls/5/vote/
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        
    ]
    
    