import imp
from django.urls import path
from . import views

urlpatterns = [
    
    path('home2/',views.home2,name='home2'),

    path('services/',views.services,name='services'),
    
    path('projects/',views.projects,name='projects'),


    
    path('',views.home,name='home'),
    path('courses/',views.courses,name='courses'),
    path('teachers/',views.teachers,name='teachers'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('courses/<str:slug>/',views.course,name='course'),
    # path('courses1/<str:slug>/',views.course1,name='course1'),

    # path('<str:slug>/',views.course_detail,name='course_detail'),
    path('course/<str:slug>/' , views.blog_detail , name="blog_detail"),
    path('blog/<str:slug>/' , views.blog_detail1 , name="blog_detail1"),
    path('services/<str:slug>/' , views.serv_detail , name="serv_detail"),
    path('add-blog/' , views.add_blog, name="add_blog"),
    path('add-project/' , views.add_project, name="add_project"),
    path('add-serv/' , views.add_serv, name="add_serv"),
    path('add-course/' , views.add_course, name="add_course"),
    path('add_lesson/' , views.add_lesson, name="add_lesson"),
    
    
    
    path('pro_add-blog/' , views.pro_add_blog, name="pro_add_blog"),
    path('pro_add-project/' , views.pro_add_project, name="pro_add_project"),
    path('pro_add-serv/' , views.pro_add_serv, name="pro_add_serv"),
    path('pro_add-course/' , views.pro_add_course, name="pro_add_course"),
    path('pro_add-lesson/' , views.pro_add_lesson, name="pro_add_lesson"),
    
    
    
    path('blog-delete/<id>' , views.blog_delete , name="blog_delete"),
    path('<id>' , views.lesson_delete , name="lesson_delete"),
    path('course-delete/<id>' , views.course_delete , name="course_delete"),
    path('project-delete/<id>' , views.project_delete , name="project_delete"),
    path('serv-delete/<id>' , views.serv_delete , name="serv_delete"),
    path('delete_from_myprofile/<id>' , views.delete_from_myprofile , name="delete_from_myprofile"),
    path('delete_course_from_myprofile/<id>' , views.delete_course_from_myprofile , name="delete_course_from_myprofile"),
    # path('blog_update/<id>' , views.blog_update , name="blog_update"),
    # path('serv_update/<id>' , views.serv_update , name="serv_update"),
    path('blog_update/<id>' , views.blog_update , name="blog_update"),
    path('lesson_update/<id>' , views.lesson_update , name="lesson_update"),
    path('course_update/<id>' , views.course_update , name="course_update"),
    path('serv_update/<id>' , views.serv_update , name="serv_update"),
    path('project_update/<id>' , views.project_update , name="project_update"),
    path('video_update/<id>' , views.video_update , name="video_update"),
    path('Pro_blog_update/<id>' , views.pro_blog_update , name="pro_blog_update"),
    path('pro_course_update/<id>' , views.pro_course_update , name="pro_course_update"),
    path('pro_serv_update/<id>' , views.pro_serv_update , name="pro_serv_update"),
    path('pro_project_update/<id>' , views.pro_project_update , name="pro_project_update"),
    path('vid/' , views.vid , name="vid"),
    path('pro_edu_update/<id>' , views.pro_edu_update , name="pro_edu_update"),
    path('pro_exp_update/<id>' , views.pro_exp_update , name="pro_exp_update"),
    path('pro_prof_skil_update/<id>' , views.pro_prof_skl_update , name="pro_prof_skl_update"),
    path('pro_skl_update/<id>' , views.pro_skl_update , name="pro_skl_update"),
    path('pro_edu_delete/<id>' , views.pro_edu_delete , name="pro_edu_delete"),
    path('pro_exp_delete/<id>' , views.pro_exp_delete , name="pro_exp_delete"),
    path('pro_prof_skil_delete/<id>' , views.pro_prof_skl_delete , name="pro_prof_skl_delete"),
    path('pro_skl_delete/<id>' , views.pro_skl_delete , name="pro_skl_delete"),
    # path('vid2/<slug>' , views.vid2 , name="vid2"),
    path("vid2/<slug>" , views.vid2 , name="vid2"),
    path("vid3/<slug>" , views.vid3 , name="vid3"),
    # path('service/', views.autocomplete, name='autocomplete'),
]
