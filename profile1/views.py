from asyncio.base_events import Server
from turtle import title
from unicodedata import category

from django.urls import reverse
from .models import Home, Message , Coding_Skills , Professional_Skills ,file,Experience , Education ,Category,CONTACT_ME,Location
from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpRequest , HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.



from .forms import HomeForm,Coding_SkillsForm,Professional_SkillsForm,ExperienceForm,EducationForm, fileForm
from pages2.models import BlogModel, Course, Project_Category

# def about(request):
#     x={'about':Coding_Skills.objects.all(),}
#     return render(request,'index.html',x)



# def message(request,message_id):
#     massage= get_object_or_404(Message,pk=message_id)
#     x={'message':message}
    
#     if request.method == 'POST':
#         name= request.POST['name']
#         email= request.POST['email']
#         subject= request.POST['subject']
#         message= request.POST['message']
#         send= Message.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message,
#         )

#         return redirect('#contact' , message_id=message.pk)
        
#     return render(request,'index.html', x)


def massage(request,slug):
    myinfo = Message.objects.first()
    # if Home.objects.filter(slug=slug).exists() and Coding_Skills.objects.filter(slug=slug).exists() and Professional_Skills.objects.filter(slug=slug).exists() and Experience.objects.filter(slug=slug).exists() and Education.objects.filter(slug=slug).exists() and SERVICES.objects.filter(slug=slug).exists() and Category.objects.filter(slug=slug).exists() and PORTFOLIO.objects.filter(slug=slug).exists() and BLOGS.objects.filter(slug=slug).exists() and CONTACT_ME.objects.filter(slug=slug).exists() and Location.objects.filter(slug=slug).exists() and file.objects.filter(slug=slug).exists() :
    homs = Home.objects.get(slug=slug)
    about = Coding_Skills.objects.filter(user=homs.user)
    personal = Professional_Skills.objects.filter(user=homs.user)
    exps = Experience.objects.filter(user=homs.user)
    edus = Education.objects.filter(user=homs.user) 
    servs = BlogModel.objects.filter(user=homs.user,is_serv=True)
    category = Project_Category.objects.filter(user=homs.user)
    ports = BlogModel.objects.filter(user=homs.user,is_project=True)
    blogs = BlogModel.objects.filter(user=homs.user,is_blog=True)
    cont = CONTACT_ME.objects.filter(user=homs.user)
    locs = Location.objects.filter(user=homs.user)
    if file.objects.filter(user=homs.user):
        files = file.objects.get(user=homs.user)
    else :
        files = ''
    course = Course.objects.filter(owner=homs.user)
    
    #  user = User.objects.get(id=request.user.id)
    # homs = Home.objects.filter(user=user)
    # about = Coding_Skills.objects.filter(user=user)
    # personal = Professional_Skills.objects.filter(user=user)
    # exps = Experience.objects.filter(user=user)
    # edus = Education.objects.filter(user=user) 
    # servs = SERVICES.objects.filter(user=user)
    # category = Category.objects.filter(user=user)
    # ports = PORTFOLIO.objects.filter(user=user)
    # blogs = BLOGS.objects.filter(user=user)
    # cont = CONTACT_ME.objects.filter(user=user)
    # locs = Location.objects.filter(user=user)
    # files = file.objects.filter(user=user)
    
    
    # user = User.objects.get(id=request.user.id)
    # homs = Home.objects.filter(user=user)
    # about = Coding_Skills.objects.filter(user=user)
    # personal = Professional_Skills.objects.filter(user=user)
    # exps = Experience.objects.filter(user=user)
    # edus = Education.objects.filter(user=user) 
    # servs = SERVICES.objects.filter(user=user)
    # category = Category.objects.filter(user=user)
    # ports = PORTFOLIO.objects.filter(user=user)
    # blogs = BLOGS.objects.filter(user=user)
    # cont = CONTACT_ME.objects.filter(user=user)
    # locs = Location.objects.filter(user=user)
    # files = file.objects.filter(user=user)
    
    
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            
            
            [settings.EMAIL_HOST_USER],
        )
    x={
    'homs': homs,
    'about': about,
    'personal':personal,
    'exps':exps,
    'edus':edus,
    'servs':servs,
    'category':category,
    'ports':ports,
    'blogs':blogs,
    'cont':cont,
    'locs':locs,
    'file':files,
    'myinfo':myinfo,
    'course':course,
    }
    if request.method == "POST":
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data= Message(email=email,subject=subject,message=message)
        data.save()
    else:
        redirect('/')
        
        
    
    return render(request,'profile.html',x)











def myprofile(request):
    myinfo = Message.objects.first()
        
    if Home.objects.filter(user=request.user):
        homs = Home.objects.get(user=request.user)
    else:
        homs = ''
        
    if file.objects.filter(user=request.user):
        files = file.objects.get(user=request.user)
    else:
        files=''
    
    
    about = Coding_Skills.objects.filter(user=request.user)
    personal = Professional_Skills.objects.filter(user=request.user)
    exps = Experience.objects.filter(user=request.user)
    edus = Education.objects.filter(user=request.user) 

    category = Project_Category.objects.filter(user=request.user)
    servs = BlogModel.objects.filter(user=request.user,is_serv=True)
    
    ports = BlogModel.objects.filter(user=request.user,is_project=True)
    blogs = BlogModel.objects.filter(user=request.user,is_blog=True)
    cont = CONTACT_ME.objects.filter(user=request.user)
    locs = Location.objects.filter(user=request.user)
    course = Course.objects.filter(owner=request.user)
    
    
    #  user = User.objects.get(id=request.user.id)
    # homs = Home.objects.filter(user=user)
    # about = Coding_Skills.objects.filter(user=user)
    # personal = Professional_Skills.objects.filter(user=user)
    # exps = Experience.objects.filter(user=user)
    # edus = Education.objects.filter(user=user) 
    # servs = SERVICES.objects.filter(user=user)
    # category = Category.objects.filter(user=user)
    # ports = PORTFOLIO.objects.filter(user=user)
    # blogs = BLOGS.objects.filter(user=user)
    # cont = CONTACT_ME.objects.filter(user=user)
    # locs = Location.objects.filter(user=user)
    # files = file.objects.filter(user=user)
    
    
    # user = User.objects.get(id=request.user.id)
    # homs = Home.objects.filter(user=user)
    # about = Coding_Skills.objects.filter(user=user)
    # personal = Professional_Skills.objects.filter(user=user)
    # exps = Experience.objects.filter(user=user)
    # edus = Education.objects.filter(user=user) 
    # servs = SERVICES.objects.filter(user=user)
    # category = Category.objects.filter(user=user)
    # ports = PORTFOLIO.objects.filter(user=user)
    # blogs = BLOGS.objects.filter(user=user)
    # cont = CONTACT_ME.objects.filter(user=user)
    # locs = Location.objects.filter(user=user)
    # files = file.objects.filter(user=user)
    
    
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            
            
            [settings.EMAIL_HOST_USER],
        )
    x={
     
    'homs': homs,
    'about': about,
    'personal':personal,
    'exps':exps,
    'edus':edus,
    'servs':servs,
    'category':category,
    'ports':ports,
    'blogs':blogs,
    'cont':cont,
    'locs':locs,
    'file':files,
    'myinfo':myinfo,
    'course':course,
    }
    if request.method == "POST":
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data= Message(email=email,subject=subject,message=message)
        data.save()
    else:
        redirect('/')
        
        
    
    return render(request,'profile.html',x)















def add_cod_skl(request):
    context = {'form' : Coding_SkillsForm}
    
    try:
        if request.method == 'POST':
            form = Coding_SkillsForm(request.POST)
            user = request.user
                    
            if form.is_valid():
                skl = form.cleaned_data['skl']
                mea = form.cleaned_data['mea']
                
                
            blog_obj = Coding_Skills.objects.create(
                user = user ,
                skl = skl, 
                mea = mea ,
            )
            
            print(blog_obj)
            
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_skls.html' , context)








def add_prof_skl(request):
    context = {'form' : Professional_SkillsForm}
    
    try:
        if request.method == 'POST':
            form = Professional_SkillsForm(request.POST)
            user = request.user
                    
            if form.is_valid():
                skl = form.cleaned_data['skl']
                mea = form.cleaned_data['mea']
                
                
            blog_obj = Professional_Skills.objects.create(
                user = user ,
                skl = skl, 
                mea = mea ,
            )
            
            print(blog_obj)
            
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_prof_skls.html' , context)







def add_home(request):
    context = {'form' : HomeForm}
    
    try:
        if request.method == 'POST':
            form = HomeForm(request.POST,request.FILES)
            user = request.user
                    
            if form.is_valid():
                name = form.cleaned_data['name']
                image = form.cleaned_data['image']
                desciption = form.cleaned_data['desciption']
                
            blog_obj = Home.objects.create(
                user = user ,
                name = name, 
                image = image ,
                desciption = desciption,
            )
            
            print(blog_obj)
            
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_blog.html' , context)




def home_update(request,id):
    blog_id = Home.objects.get(id=id)
    if request.method == 'POST':
        blog_save = HomeForm(request.POST , request.FILES , instance= blog_id)
        if blog_save.is_valid():
            blog_save.save()
            return redirect('/myprofile/')
    else:
        blog_save =HomeForm(instance=blog_id)
        context = {
        'form' : blog_save,
        }
        return render(request , 'update_blog.html' ,context )
    

















def add_file(request):
    context = {'form' : fileForm}
    
    try:
        if request.method == 'POST':
            form = fileForm(request.POST,request.FILES)
            user = request.user
                    
            if form.is_valid():
                filee = form.cleaned_data['file']

            blog_obj = file.objects.create(
                user = user ,
                file = filee, 
            )
            
            print(blog_obj)
            
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_blog.html' , context)




def file_update(request,id):
    blog_id = file.objects.get(id=id)
    if request.method == 'POST':
        blog_save = fileForm(request.POST , request.FILES , instance= blog_id)
        if blog_save.is_valid():
            blog_save.save()
            return redirect('/myprofile/')
    else:
        blog_save =fileForm(instance=blog_id)
        context = {
        'form' : blog_save,
        }
        return render(request , 'update_blog.html' ,context )


















def add_exp(request):
    context = {'form' : ExperienceForm}
    
    try:
        if request.method == 'POST':
            form = ExperienceForm(request.POST)
            user = request.user
                    
            if form.is_valid():
                title = form.cleaned_data['title']
                discription = form.cleaned_data['discription']
                
                
            blog_obj = Experience.objects.create(
                user = user ,
                title = title ,
                discription = discription, 
                
            )
            
            print(blog_obj)
            
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_prof_skls.html' , context)







def add_edu(request):
    context = {'form' : EducationForm}
    
    try:
        if request.method == 'POST':
            form = EducationForm(request.POST)
            user = request.user
                    
            if form.is_valid():
                title = form.cleaned_data['title']
                discription = form.cleaned_data['discription']
                
                
            blog_obj = Education.objects.create(
                user = user ,
                title = title ,
                discription = discription, 
                
            )
            
            print(blog_obj)
            
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_prof_skls.html' , context)




def handle404(request,exception):
    return render(request,'404.html',status=404)



def handle500(request):
    return render(request,'404.html',status=404)






# def profile_edit(request):
#     home={}
#     if Home.objects.filter(user=request.user):
#         home = Home.objects.get(user=request.user)
#     about = Coding_Skills.objects.filter(user=request.user)
#     personal = Professional_Skills.objects.filter(user=request.user)
#     exps = Experience.objects.filter(user=request.user)
#     edus = Education.objects.filter(user=request.user) 

#     category = Project_Category.objects.filter(user=request.user)
#     servs = BlogModel.objects.filter(user=request.user,is_serv=True)
    
#     ports = BlogModel.objects.filter(user=request.user,is_project=True)
#     blogs = BlogModel.objects.filter(user=request.user,is_blog=True)
#     cont = CONTACT_ME.objects.filter(user=request.user)
#     locs = Location.objects.filter(user=request.user)
#     course = Course.objects.filter(owner=request.user)
    
# #     home = Home.objects.get(user=request.user)
# #     coding_skills = Coding_Skills.objects.filter(user=request.user)
# #     professional_skills = Professional_Skills.objects.filter(user=request.user)
# #     experience = Experience.objects.filter(user=request.user)
# #     education = Education.objects.filter(user=request.user)
# #     filee = file.objects.get(user=request.user)
# #     services = SERVICES.objects.filter(user=request.user)
# #     category = Category.objects.filter(user=request.user)
# #     project = BlogModel.objects.filter(user=request.user,is_project=True)
# #     blog = BlogModel.objects.filter(user=request.user,is_blog=True)
    
# #     if request.method=='POST':

# #         homeform = HomeForm(request.POST,request.FILES,instance= home )
# #         coding_skillsform = Coding_SkillsForm(request.POST,request.FILES,instance=coding_skills )
# #         professional_skillsform = Professional_SkillsForm(request.POST,request.FILES,instance=professional_skills )
# #         experienceform = ExperienceForm(request.POST,request.FILES,instance= experience )
# #         educationform = EducationForm(request.POST,request.FILES,instance=education )
# #         fileform = fileForm(request.POST,request.FILES,instance=filee )
# #         servicesform = SERVICESForm(request.POST,request.FILES,instance= services )
# #         categoryform = CategoryForm(request.POST,request.FILES,instance= category )
# #         projectform = BlogModelForm(request.POST,request.FILES,instance= project )
# #         blogmodelform = BlogModelForm(request.POST,request.FILES,instance= blog )
        
        
        
# #         if homeform.is_valid() and coding_skillsform.is_valid() and professional_skillsform.is_valid() and experienceform.is_valid() and educationform.is_valid() and fileform.is_valid() and servicesform.is_valid() and categoryform.is_valid() and projectform.is_valid() and blogmodelform.is_valid():
            
# #             home = homeform.save(commit=False)
# #             home.user = request.user
# #             home.save()
            
# #             coding_skills = coding_skillsform.save(commit=False)
# #             coding_skills.user = request.user
# #             coding_skills.save()
            
# #             professional_skills = professional_skillsform.save(commit=False)
# #             professional_skills.user = request.user
# #             professional_skills.save()
            
# #             experience = experienceform.save(commit=False)
# #             experience.user = request.user
# #             experience.save()
            
# #             education = educationform.save(commit=False)
# #             education.user = request.user
# #             education.save()
            
# #             filee = fileform.save(commit=False)
# #             filee.user = request.user
# #             filee.save()
            
# #             services = servicesform.save(commit=False)
# #             services.user = request.user
# #             services.save()
            
# #             category = categoryform.save(commit=False)
# #             category.user = request.user
# #             category.save()
            
# #             project = projectform.save(commit=False)
# #             project.user = request.user
# #             project.save()
            
# #             blog = blogmodelform.save(commit=False)
# #             blog.user = request.user
# #             blog.save()
            
# #             return redirect('/profile/')

# #     else :
# #         homeform = homeform(instance=home)
# #         coding_skillsform = coding_skillsform(instance=coding_skills)
# #         professional_skillsform = professional_skillsform(instance=professional_skills)
# #         experienceform = experienceform(instance=experience)
# #         educationform = educationform(instance=education)
# #         fileform = fileform(instance=filee)
# #         servicesform = servicesform(instance=services)
# #         categoryform = categoryform(instance=category)
# #         projectform = projectform(instance=project)
# #         blogmodelform = blogmodelform(instance=blog)


# #     x = {
# #         'homeform':homeform,
# #          'coding_skillsform':coding_skillsform,
# #          'professional_skillsform':professional_skillsform,
# #          'experienceform':experienceform,
# #          'educationform':educationform,
# #          'fileform':fileform,
# #          'servicesform':servicesform,
# #          'categoryform':categoryform,
# #          'projectform':projectform,
# #          'blogmodelform':blogmodelform
# #          }

#     x = {
#         'home':home,
#         'about': about,
#         'personal':personal,
#         'exps':exps,
#         'edus':edus,
#         'servs':servs,
#         'category':category,
#         'ports':ports,
#         'blogs':blogs,
#         'cont':cont,
#         'locs':locs,
#         'course':course,
#          }
#     return render(request,'profile_edit.html',x)




# # def profile_edit(request):
# #     profile = Profile.objects.get(user=request.user)

# #     if request.method=='POST':
# #         userform = UserForm(request.POST,instance=request.user)
# #         profileform = ProfileForm(request.POST,request.FILES,instance=profile )
# #         if userform.is_valid() and profileform.is_valid():
# #             userform.save()
# #             myprofile = profileform.save(commit=False)
# #             myprofile.user = request.user
# #             myprofile.save()
# #             return redirect(reverse('profile'))

# #     else :
# #         userform = UserForm(instance=request.user)
# #         profileform = ProfileForm(instance=profile)

# #     return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})