# from asyncio.windows_events import NULL
# from cgitb import small
# from email.mime import image
# from pyexpat import model
# from turtle import title
from django.shortcuts import redirect, render

# from profile1.models import file
from .models import BlogModel, Home,Course,Category,Contact,Message, Video, blog_Category,Project_Category
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from profile1.models import file,Home,Coding_Skills,Professional_Skills,Experience,Education
# Create your views here.
from profile1.forms import Coding_SkillsForm,Professional_SkillsForm,ExperienceForm,EducationForm


from .forms import BlogForm,ProjectForm, courseForm, lessonForm,servForm, videoForm


# import json

# from django.http import JsonResponse



# def validate_username(request): 
#     username = request.GET.get('username')
#     is_taken = User.objects.filter(username__iexact=username).exists()
#     data = {'is_taken':is_taken}
#     if data['is_taken']: 
#         data['error_message'] = "The username already taken"
#     return JsonResponse(data)




# def autocomplete(request):
#     if 'term' in request.GET:
#         qs = BlogModel.objects.filter(is_serv=True,title__icontains=request.GET.get('term'))
#         titles = list()
#         for x in qs:
#             titles.append(x.title)
#         # titles = [product.title for product in qs]
#         return JsonResponse(titles, safe=False)
#     return render(request, 'services.html')


def vid(request):
    if request.user.is_tech == True and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''

    vid = Video.objects.all()
    disc = BlogModel.objects.all()
    # vide = Video.objects.all().first()
    return render(request,'video.html',{'vid':vid,'disc':disc,'home':home,})



def vid2(request,slug):
    if request.user.is_tech == True and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''

    coursee = Course.objects.get(slug=slug)
    disc = BlogModel.objects.filter(course=coursee)
    dic = BlogModel.objects.filter(course=coursee).first()
    # vide = Video.objects.all().first()
    return render(request,'video2.html',{'disc':disc,'dic':dic,'home':home,})

def vid3(request,slug):
    if request.user.is_tech == True and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''

    dic = BlogModel.objects.get(slug=slug)
    disc = BlogModel.objects.filter(course=dic.course)
    # vide = Video.objects.all().first()
    return render(request,'video2.html',{'dic':dic,'disc':disc,'home':home,})



# def course1(request, slug):
#     coursee = Course.objects.get(slug=slug)
#     lesons=BlogModel.objects.filter(course=coursee.id)
#     x={'course': coursee,
#        'lesons':lesons.order_by('title'),
#        }
    
#     return render(request,'course-3.html',x)

# def alllesons(request):
#     context = {'lesons' : BlogModel.objects.all()}
#     return render(request , 'course-3.html' , context)





def add_blog(request):
    if request.user.is_tech == True and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'form' : BlogForm,'home':home}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST,request.FILES)
            user = request.user
            
            if form.is_valid():
                title = form.cleaned_data['title']
                image = form.cleaned_data['image']
                content = form.cleaned_data['content']
                # project_Category = form.cleaned_data['project_Category']
                blog_Category = form.cleaned_data['blog_Category']
                # course = form.cleaned_data['course']
                # is_serv = form.cleaned_data['is_serv']
                # is_project = form.cleaned_data['is_project']
                small_desc = form.cleaned_data['small_desc']
                # is_blog = form.cleaned_data['is_blog']    
                
                
                
                
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                image = image ,
                is_blog = True , content = content,
                blog_Category = blog_Category,
                small_desc = small_desc
            )
            print(blog_obj)
            return redirect('/blog/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_blog.html' , context)










def pro_add_blog(request):
    if request.user.is_tech == True and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'form' : BlogForm,'home':home}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST,request.FILES)
            user = request.user
            
            if form.is_valid():
                title = form.cleaned_data['title']
                image = form.cleaned_data['image']
                content = form.cleaned_data['content']
                # project_Category = form.cleaned_data['project_Category']
                blog_Category = form.cleaned_data['blog_Category']
                # course = form.cleaned_data['course']
                # is_serv = form.cleaned_data['is_serv']
                # is_project = form.cleaned_data['is_project']
                small_desc = form.cleaned_data['small_desc']
                # is_blog = form.cleaned_data['is_blog']    
                
                
                
                
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                image = image ,
                is_blog = True , content = content,
                blog_Category = blog_Category,
                small_desc = small_desc
            )
            print(blog_obj)
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_blog.html' , context)










def add_serv(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'form' : servForm,'home':home}
    try:
        if request.method == 'POST':
            form = servForm(request.POST,request.FILES)
            user = request.user
            
            if form.is_valid():
                title = form.cleaned_data['title']
                image = form.cleaned_data['image']
                content = form.cleaned_data['content']
                small_desc = form.cleaned_data['small_desc']
                # project_Category = form.cleaned_data['project_Category']
                # blog_Category = form.cleaned_data['blog_Category']
                # course = form.cleaned_data['course']
                # is_serv = form.cleaned_data['is_serv']
                # is_project = form.cleaned_data['is_project']
                # is_blog = form.cleaned_data['is_blog']    
                
                
                
                
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                image = image , is_serv = True , content = content,
                small_desc = small_desc
            )
            print(blog_obj)
            return redirect('/services/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_serv.html' , context)








def pro_add_serv(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'form' : servForm,'home':home}
    try:
        if request.method == 'POST':
            form = servForm(request.POST,request.FILES)
            user = request.user
            
            if form.is_valid():
                title = form.cleaned_data['title']
                image = form.cleaned_data['image']
                content = form.cleaned_data['content']
                small_desc = form.cleaned_data['small_desc']
                # project_Category = form.cleaned_data['project_Category']
                # blog_Category = form.cleaned_data['blog_Category']
                # course = form.cleaned_data['course']
                # is_serv = form.cleaned_data['is_serv']
                # is_project = form.cleaned_data['is_project']
                # is_blog = form.cleaned_data['is_blog']    
                
                
                
                
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                image = image , is_serv = True , content = content,
                small_desc = small_desc
            )
            print(blog_obj)
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_serv.html' , context)









def add_project(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'form' : ProjectForm,'home':home}
    try:
        if request.method == 'POST':
            form = ProjectForm(request.POST,request.FILES)
            user = request.user
            
            if form.is_valid():
                title = form.cleaned_data['title']
                image = form.cleaned_data['image']
                content = form.cleaned_data['content']
                project_Category = form.cleaned_data['project_Category']
                # blog_Category = form.cleaned_data['blog_Category']
                # course = form.cleaned_data['course']
                # is_serv = form.cleaned_data['is_serv']
                # is_project = form.cleaned_data['is_project']
                # is_blog = form.cleaned_data['is_blog']    
                small_desc = form.cleaned_data['small_desc']
                
                
                
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                image = image , is_project = True ,
                content = content,
                project_Category = project_Category , 
                small_desc = small_desc
            )
            print(blog_obj)
            return redirect('/projects/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_project.html' , context)










def pro_add_project(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'form' : ProjectForm,'home':home}
    try:
        if request.method == 'POST':
            form = ProjectForm(request.POST,request.FILES)
            user = request.user
            
            if form.is_valid():
                title = form.cleaned_data['title']
                image = form.cleaned_data['image']
                content = form.cleaned_data['content']
                project_Category = form.cleaned_data['project_Category']
                # blog_Category = form.cleaned_data['blog_Category']
                # course = form.cleaned_data['course']
                # is_serv = form.cleaned_data['is_serv']
                # is_project = form.cleaned_data['is_project']
                # is_blog = form.cleaned_data['is_blog']    
                small_desc = form.cleaned_data['small_desc']
                
                
                
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                image = image , is_project = True ,
                content = content,
                project_Category = project_Category , 
                small_desc = small_desc
            )
            print(blog_obj)
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_project.html' , context)







def add_course(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'form' : courseForm,'home':home}
    
    try:
        if request.method == 'POST':
            form = courseForm(request.POST,request.FILES)
            owner = request.user
                    
            if form.is_valid():
                title = form.cleaned_data['title']
                img = form.cleaned_data['img']
                disc = form.cleaned_data['disc']
                category = form.cleaned_data['category']
                
            blog_obj = Course.objects.create(
                owner = owner , title = title, 
                img = img , disc = disc,
                category = category
            )
            
            print(blog_obj)
            
            return redirect('/courses/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_course.html' , context)









def pro_add_course(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'form' : courseForm,'home':home}
    
    try:
        if request.method == 'POST':
            form = courseForm(request.POST,request.FILES)
            owner = request.user
                    
            if form.is_valid():
                title = form.cleaned_data['title']
                img = form.cleaned_data['img']
                disc = form.cleaned_data['disc']
                category = form.cleaned_data['category']
                
            blog_obj = Course.objects.create(
                owner = owner , title = title, 
                img = img , disc = disc,
                category = category
            )
            
            print(blog_obj)
            
            return redirect('/myprofile/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_course.html' , context)








def add_lesson(request):
    if request.user.is_tech == True and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''    
    context = {'form' : lessonForm,'home':home}
    try:
        if request.method == 'POST':
            form = lessonForm(request.POST,request.FILES)
            user = request.user
            
            
            if form.is_valid():
                title = form.cleaned_data['title']
                image = form.cleaned_data['image']
                content = form.cleaned_data['content']
                coursee = form.cleaned_data['course']
                is_project = form.cleaned_data['is_project']
                project_category = form.cleaned_data['project_Category']
                is_blog = form.cleaned_data['is_blog']
                blog_category = form.cleaned_data['blog_Category']
                
                
            blog_obj = BlogModel.objects.create(
                user = user ,
                title = title, 
                image = image,
                content = content,
                course = coursee,
                is_project = is_project,
                project_Category = project_category,
                is_blog = is_blog,
                blog_Category = blog_category,
                
            
            )
            

            return redirect('/courses/')
            
            


    except Exception as e :
        print(e)
    
    return render(request , 'add_lesson.html' , context)




def pro_add_lesson(request):
    
    context = {'form' : videoForm}
    try:
        if request.method == 'POST':
            form = videoForm(request.POST,request.FILES)
            user = request.user
            
            if form.is_valid():
                title = form.cleaned_data['title']
                image = form.cleaned_data['image']
                content = form.cleaned_data['content']
                is_blog = form.cleaned_data['is_blog']
                blog_Category = form.cleaned_data['blog_Category']
                is_project = form.cleaned_data['is_project']
                project_Category = form.cleaned_data['project_Category']                
                small_desc = form.cleaned_data['small_desc']
                course = form.cleaned_data['course']
            blog_obj = BlogModel.objects.create(
                user = user ,
                title = title, 
                image = image ,
                content = content,
                is_blog = is_blog ,
                blog_Category = blog_Category,
                is_project = is_project,
                project_Category = project_Category,
                small_desc = small_desc,
                course = course
            )
            

            return redirect('/myprofile/')
            
            


    except Exception as e :
        print(e)
    
    return render(request , 'add_lesson.html' , context)












def blog_delete(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/blog/')




def serv_delete(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/services/')





def project_delete(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/projects/')



def lesson_delete(request , id):
    
    
    try:
        blog_obj = Video.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('courses/')




def course_delete(request , id):
    try:
        blog_obj = Course.objects.get(id = id)
        
        if blog_obj.owner == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/courses/')





def delete_from_myprofile(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/myprofile/')




def delete_course_from_myprofile(request , id):
    try:
        blog_obj = Course.objects.get(id = id)
        
        if blog_obj.owner == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/myprofile/')







# def blog_update(request , id):
#     context = {}
#     try:
        
        
#         blog_obj = BlogModel.objects.get(id = id)
       
        
#         if blog_obj.user != request.user:
#             return redirect('/')
        
#         initial_dict = {'content': blog_obj.content,'small_desc':blog_obj.small_desc,'blog_Category':blog_obj.blog_Category}
#         form = BlogForm(initial = initial_dict)
#         if request.method == 'POST':
#             form = BlogForm(request.POST)
#                     print(request.FILES)
#             image = request.FILES['image']
#             title = request.POST.get('title')
#             user = request.user
            
#             if form.is_valid():
#                 content = form.cleaned_data['content']
            
#             blog_obj = BlogModel.objects.create(
#                 user = user , title = title, 
#                 content = content, image = image
#             )
        
        
#         context['blog_obj'] = blog_obj
#         context['form'] = form
#     except Exception as e :
#         print(e)

#     return render(request , 'update_blog.html' , context)








# def serv_update(request , id):
#     context = {}
#     try:
        
        
#         blog_obj = BlogModel.objects.get(id = id)
       
        
#         if blog_obj.user != request.user:
#             return redirect('/')
        
#         initial_dict = {'title':blog_obj.title,'image':blog_obj.image,'content': blog_obj.content,'small_desc':blog_obj.small_desc,}
#         form = servForm(initial = initial_dict)
#         if request.method == 'POST':
#             form = servForm(request.POST)
#             user = request.user
            
            
#             if form.is_valid():
#                 content = form.cleaned_data['content']
#                 title = form.cleaned_data['title']
#                 image = form.cleaned_data['image']
#                 small_desc = form.cleaned_data['small_desc']
            
#             blog_obj = BlogModel.objects.update(
#                 user = user , 
#                 title = title , image = image , 
#                 content = content , 
#                 small_desc = small_desc , 
#             )
        
        
#         context['blog_obj'] = blog_obj
#         context['form'] = form
#     except Exception as e :
#         print(e)

#     return render(request , 'update_service.html' , context)



def lesson_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    blog_id = Video.objects.get(id=id,user=request.user)
    if request.method == 'POST':
        blog_save = videoForm(request.POST , request.FILES , instance= blog_id)
        if blog_save.is_valid():
            blog_save.save()
            return redirect('/courses/')
    else:
        blog_save = videoForm(instance=blog_id)
        context = {
        'form' : blog_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )
    








def blog_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    blog_id = BlogModel.objects.get(id=id,is_blog=True)
    if request.method == 'POST':
        blog_save = BlogForm(request.POST , request.FILES , instance= blog_id)
        if blog_save.is_valid():
            blog_save.save()
            return redirect('/blog/')
    else:
        blog_save = BlogForm(instance=blog_id)
        context = {
        'form' : blog_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )
    








def pro_blog_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    blog_id = BlogModel.objects.get(id=id,is_blog=True)
    if request.method == 'POST':
        blog_save = BlogForm(request.POST , request.FILES , instance= blog_id)
        if blog_save.is_valid():
            blog_save.save()
            return redirect('/myprofile/')
    else:
        blog_save = BlogForm(instance=blog_id)
        context = {
        'form' : blog_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )
    












def pro_skl_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    blog_id = Coding_Skills.objects.get(id=id,user=request.user)
    if request.method == 'POST':
        blog_save = Coding_SkillsForm(request.POST , request.FILES , instance= blog_id)
        if blog_save.is_valid():
            blog_save.save()
            return redirect('/myprofile/')
    else:
        blog_save = Coding_SkillsForm(instance=blog_id)
        context = {
        'form' : blog_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )





def pro_skl_delete(request , id):
    try:
        blog_obj = Coding_Skills.objects.get(id = id,user = request.user)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/myprofile/')











def pro_prof_skl_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    blog_id = Professional_Skills.objects.get(id=id,user=request.user)
    if request.method == 'POST':
        blog_save = Professional_SkillsForm(request.POST , request.FILES , instance= blog_id)
        if blog_save.is_valid():
            blog_save.save()
            return redirect('/myprofile/')
    else:
        blog_save = Professional_SkillsForm(instance=blog_id)
        context = {
        'form' : blog_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )






def pro_prof_skl_delete(request , id):
    try:
        blog_obj = Professional_Skills.objects.get(id = id,user = request.user)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/myprofile/')








def pro_exp_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    blog_id = Experience.objects.get(id=id,user=request.user)
    if request.method == 'POST':
        blog_save = ExperienceForm(request.POST , request.FILES , instance= blog_id)
        if blog_save.is_valid():
            blog_save.save()
            return redirect('/myprofile/')
    else:
        blog_save = ExperienceForm(instance=blog_id)
        context = {
        'form' : blog_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )







def pro_exp_delete(request , id):
    try:
        blog_obj = Experience.objects.get(id = id,user = request.user)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/myprofile/')








def pro_edu_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    blog_id = Education.objects.get(id=id,user=request.user)
    if request.method == 'POST':
        blog_save = EducationForm(request.POST , request.FILES , instance= blog_id)
        if blog_save.is_valid():
            blog_save.save()
            return redirect('/myprofile/')
    else:
        blog_save = EducationForm(instance=blog_id)
        context = {
        'form' : blog_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )





def pro_edu_delete(request , id):
    try:
        blog_obj = Education.objects.get(id = id,user = request.user)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/myprofile/')








def course_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    course_id = Course.objects.get(id=id)
    if request.method == 'POST':
        course_save = courseForm(request.POST , request.FILES , instance= course_id)
        if course_save.is_valid():
            course_save.save()
            return redirect('/courses/')
    else:
        course_save = courseForm(instance=course_id)
        context = {
        'form' : course_save,
        'home':home
        }
        return render(request , 'update_course.html' ,context )
    








def pro_course_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    course_id = Course.objects.get(id=id)
    if request.method == 'POST':
        course_save = courseForm(request.POST , request.FILES , instance= course_id)
        if course_save.is_valid():
            course_save.save()
            return redirect('/myprofile/')
    else:
        course_save = courseForm(instance=course_id)
        context = {
        'form' : course_save,
        'home':home
        }
        return render(request , 'update_course.html' ,context )
    




def serv_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    serv_id = BlogModel.objects.get(id=id,is_serv=True)
    if request.method == 'POST':
        serv_save = servForm(request.POST , request.FILES , instance= serv_id)
        if serv_save.is_valid():
            serv_save.save()
            return redirect('/services/')
    else:
        serv_save = servForm(instance=serv_id)
        context = {
        'form' : serv_save,
        'home' : home
        }
        return render(request , 'update_blog.html' ,context )
    








def pro_serv_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    serv_id = BlogModel.objects.get(id=id,is_serv=True)
    if request.method == 'POST':
        serv_save = servForm(request.POST , request.FILES , instance= serv_id)
        if serv_save.is_valid():
            serv_save.save()
            return redirect('/myprofile/')
    else:
        serv_save = servForm(instance=serv_id)
        context = {
        'form' : serv_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )
    







def project_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    project_id = BlogModel.objects.get(id=id,is_project=True)
    if request.method == 'POST':
        project_save = ProjectForm(request.POST , request.FILES , instance= project_id)
        if project_save.is_valid():
            project_save.save()
            return redirect('/projects/')
    else:
        project_save = servForm(instance=project_id)
        context = {
        'form' : project_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )







def pro_project_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    project_id = BlogModel.objects.get(id=id,is_project=True,user=request.user)
    if request.method == 'POST':
        project_save = ProjectForm(request.POST , request.FILES , instance= project_id)
        if project_save.is_valid():
            project_save.save()
            return redirect('/myprofile/')
    else:
        project_save = servForm(instance=project_id)
        context = {
        'form' : project_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )








def video_update(request , id):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    video_id = BlogModel.objects.get(id=id,)
    if request.method == 'POST':
        video_save = videoForm(request.POST , request.FILES , instance= video_id)
        if video_save.is_valid():
            video_save.save()
            return redirect('course',slug=video_id.course.slug)
    else:
        video_save = videoForm(instance=video_id)
        context = {
        'form' : video_save,
        'home':home
        }
        return render(request , 'update_blog.html' ,context )





def home(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    serv=BlogModel.objects.filter(is_serv = True)
    course=Course.objects.all()
    blogs=BlogModel.objects.filter(is_blog=True)
    
    x={'services':serv,'home':home,'courses':course,'blogs':blogs,}
    return render(request,'home.html',x)



def home2(request):
    return render(request,'home2.html')




def services(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    serv=BlogModel.objects.filter(is_serv = True)
    x={'services':serv,'home':home,'courses':course,}
    return render(request,'services.html',x)


def projects(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    blogs=BlogModel.objects.filter(is_project=True)
    category = Project_Category.objects.all()
    x={'projects':blogs,'category':category,'home':home}
    
    return render(request,'projects.html',x)


def courses(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    course=Course.objects.all()
    category=Category.objects.all()
    x={'courses':course,
       'category':category,
       'home':home
       }
    
    return render(request,'courses.html',x)



            

def course(request, slug):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    coursee = Course.objects.get(slug=slug)
    video=Video.objects.filter(course=coursee)
    x={'cors': coursee,
       'vid':video,
       'home':home
       }
    
    return render(request,'video.html',x)






def serv_detail(request , slug):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'home':home,}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
        
 
        
    return render(request , 'serv_detail.html' , context)






def blog_detail(request , slug):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'home':home,}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
        
 
        
    return render(request , 'blog_detail.html' , context)






    







def blog_detail1(request , slug):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    context = {'home':home,}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        category=Category.objects.all()
        context['blog_obj'] =  blog_obj
        context['category'] =  category

    except Exception as e:
        print(e)
    return render(request , 'blog_detail1.html' , context)





def teachers(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    teatcer=Home.objects.all()
    x={'teachers':teatcer,'home':home}
    return render(request,'teachers.html',x)






def blog(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    blogs=BlogModel.objects.filter(is_blog=True)
    category = blog_Category.objects.all()
    x={'blogs':blogs.order_by('-created_at'),'category':category,'home':home}
    return render(request,'blog.html',x)






def contact(request):
    if request.user.is_authenticated and Home.objects.filter(user=request.user):
        home = Home.objects.get(user=request.user)
    else:
        home = ''
    contact=Contact.objects.all()
    myinfo = Message.objects.first()

    if request.method == 'POST' and request.user.is_authenticated:
        subject = request.POST['subject']
        if request.user.email:
            email = request.user.email
        elif request.user.username:
            email = request.user.username
        else:
            return redirect('/contact/')
        message = request.POST['message']

        send_mail(
            email,
            message,
            subject,
            
            
            
            
            [settings.EMAIL_HOST_USER],
        )
    x={'contact':contact,
       'myinfo':myinfo,
       'home':home
       }
    
    return render(request,'contact.html',x)

