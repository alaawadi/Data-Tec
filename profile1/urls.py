from cgitb import handler
from django.urls import path
from . import views
from django.views.static import serve
# from django.conf.urls import re_path
from django.urls import re_path
from django.conf import settings



urlpatterns = [
    path('profile/<slug>',views.massage,name='profile'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('add_cod_skl/',views.add_cod_skl,name='add_cod_skl'),
    path('add_prof_skl/',views.add_prof_skl,name='add_prof_skl'),
    path('add_exp/',views.add_exp,name='add_exp'),
    path('add_edu/',views.add_edu,name='add_edu'),
    path('add_home/',views.add_home,name='add_home'),
    path('home_update/<id>',views.home_update,name='home_update'),
     path('add_file/',views.add_file,name='add_file'),
    path('file_update/<id>',views.file_update,name='file_update'),
    # path('profile/edit/',views.profile_edit , name='profile_edit'),
    
    
    
    # path('',views.about,name='about'),

    # path('<int:message_id>/',views.message,name='message'),
]



handler404 = 'profile1.views.handle404'
handler500 = 'profile1.views.handle500'



urlpatterns += [

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]