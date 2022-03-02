from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify



from django.contrib.auth.models import AbstractBaseUser



# class CustomUser(AbstractBaseUser):
#     is_tech = models.BooleanField(default=False)    


class Home(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    image=models.ImageField(upload_to='photos/%y/%m/%d',null=True, blank=True)
    name=models.CharField(max_length=50,null=True, blank=True)
    desciption=models.TextField(max_length=1000,null=True, blank=True)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(Home,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
class Coding_Skills(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    skl=models.CharField(max_length= 50)
    mea=models.IntegerField()
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(Coding_Skills,self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.skl
    
    
class Professional_Skills(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    skl=models.CharField(max_length= 50)
    mea=models.IntegerField()
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(Professional_Skills,self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.skl
    
    
class Experience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50)
    discription=models.TextField(max_length=200)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(Experience,self).save(*args, **kwargs)
        
    
    def __str__(self):
        return self.title


    
class Education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50)
    discription=models.TextField(max_length=200)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(Education,self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title

class file(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    file=models.FileField(upload_to='media',null=True, blank=True)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(file,self).save(*args, **kwargs)
    
    
    
    
class SERVICES(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    img= models.ImageField(upload_to='service/%y/%m/%d')
    title=models.TextField(max_length=50)
    discription= models.CharField(max_length=200)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(SERVICES,self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title

    
    
class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(Category,self).save(*args, **kwargs)
    
    
    
    def __str__(self):
        return self.name
    
    
    
# class PORTFOLIO(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     title=models.CharField(max_length=80)
#     img=models.ImageField(upload_to='protfolio/%y/%m/%d')
#     category = models.ForeignKey(Category, on_delete=PROTECT)
#     slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
#     def save(self,*args, **kwargs):
#         self.slug = slugify(self.user)
#         super(PORTFOLIO,self).save(*args, **kwargs)
    
    
#     def __str__(self):
#         return self.title
    
    
# class BLOGS(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     img=models.ImageField(upload_to='blogs/%y/%m/%d')
#     create_py=User.objects.first()
#     date=models.DateField(auto_now_add=True)
#     title=models.CharField(max_length=50)
#     description=models.TextField(max_length=300)
#     slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
#     def save(self,*args, **kwargs):
#         self.slug = slugify(self.user)
#         super(BLOGS,self).save(*args, **kwargs)
    
#     def __str__(self):
#         return self.title
    
    
    
class CONTACT_ME(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phone=models.IntegerField()
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=100)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(Message,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.email
    

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=300)
    message=models.TextField(max_length=2000)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(Message,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
    
class Location(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    url=models.TextField(max_length=1000)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user)
        super(Location,self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.user