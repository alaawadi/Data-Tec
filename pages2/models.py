from cgitb import small
from distutils.command.upload import upload
from tokenize import blank_re
from turtle import title
from typing import OrderedDict
from unicodedata import category
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from profile1.models import Category
# Create your models here.


from froala_editor.fields import FroalaField
from .helpers import *


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/blog',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    course = models.ForeignKey('Course',on_delete=models.CASCADE,null=True,blank=True)
    blog_Category = models.ForeignKey('blog_Category',on_delete=models.CASCADE,null=True,blank=True)
    vid_num = models.IntegerField(null=True,blank=True)
    is_blog = models.BooleanField(default=False)
    is_serv = models.BooleanField(default=False)
    small_desc = models.CharField(max_length=200,null=True,blank=True)
    is_project = models.BooleanField(default=False)
    user_slug = models.SlugField(max_length=1000 , null=True , blank=True)
    course_category = models.ForeignKey('Category',on_delete=models.PROTECT,blank=True,null=True)
    project_Category = models.ForeignKey('Project_Category',on_delete=models.CASCADE,null=True,blank=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
        
    
    # def save(self,*args, **kwargs):
    #     self.user_slug = slugify(self.user)
    #     super(BlogModel,self).save(*args, **kwargs)






class Project_Category(models.Model):
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE) 
    title = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='images/procat')
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.user)
        super(Project_Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


def home_img(instance,filename):
    imagename , extension = filename.split(".")
    return "home/%s.%s"%(instance.id,extension)

class Home(models.Model):
    img = models.ImageField(upload_to=home_img)
    title = models.CharField(max_length=100)
    disc = models.TextField(max_length=400)
    
    def __str__(self):
        return self.title
    
    
    
    
    
    
def course_img(instance,filename):
    imagename , extension = filename.split(".")
    return "course/%s.%s"%(instance.id,extension)

class Course(models.Model):
    img = models.ImageField(upload_to=course_img)
    title = models.CharField(max_length=100)
    disc = models.TextField(max_length=200)
    owner = models.ForeignKey(User, related_name='course_owner', on_delete=models.CASCADE)
    category= models.ForeignKey('Category',on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Course,self).save(*args, **kwargs)
    
    
    
    
    
    
def video(instance,filename):
    imagename , extension = filename.split(".")
    return "course/video/%s.%s"%(instance.id,extension)

def video_img(instance,filename):
    imagename , extension = filename.split(".")
    return "course/image/%s.%s"%(instance.id,extension)

def code(instance,filename):
    imagename , extension = filename.split(".")
    return "course/code/%s.%s"%(instance.id,extension)

class Video(models.Model):
    video=models.FileField(upload_to=video)
    image = models.ImageField(upload_to=video_img)
    title = models.CharField(max_length=100)
    disc= models.TextField(blank=True,null=True)
    code = models.FileField(upload_to=code,blank=True,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.course)  + self.title





    




    
    
    
def category_img(instance,filename):
    imagename , extension = filename.split(".")
    return "category/%s.%s"%(instance.id,extension)

class Category(models.Model):
    img = models.ImageField(upload_to=category_img)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    
    


def blog_category_img(instance,filename):
    imagename , extension = filename.split(".")
    return "category/%s.%s"%(instance.id,extension)

class blog_Category(models.Model):
    img = models.ImageField(upload_to=category_img)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    



    
    
def teacher_img(instance,filename):
    imagename , extension = filename.split(".")
    return "teacher/%s.%s"%(instance.id,extension)

class Teacher(models.Model):
    img = models.ImageField(upload_to=teacher_img)
    name = models.CharField(max_length=50)
    work = models.CharField(max_length=50)
    facebook = models.URLField()
    instagram = models.URLField()
    twiter = models.URLField()
    github = models.URLField()
    
    def __str__(self):
        return self.name
    
    
    
    
    
def blog_img(instance,filename):
    imagename , extension = filename.split(".")
    return "blog/%s.%s"%(instance.id,extension)

class Blog(models.Model):
    img = models.ImageField(upload_to=blog_img)
    date = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, related_name='blog_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    smol_disc = models.TextField(max_length=200)
    big_disc = models.TextField(max_length=100000)
    
    def __str__(self):
        return self.title
    
    
    
    
    
class Contact(models.Model):
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=150)
    map = models.URLField()
    
    def __str__(self):
        return self.email
    
    
    
    
class Message(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.name