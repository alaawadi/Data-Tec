from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    # path('activate/<uidb64>/<token>/',views.activate, name='activate'), 
    # path('ajax/validate_username/', views.validate_username, name='validate_username'),
    # path('login',views.login_view, name = 'login')
    # path('profile/',views.profile , name='profile'),
    # path('profile/edit',views.profile_edit , name='profile_edit'),

]
