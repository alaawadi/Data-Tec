from django.shortcuts import redirect, render
from .forms import ProfileForm,SignupForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile
from django.urls import reverse
# Create your views here.
from django.contrib.auth import authenticate

from profile1.models import Home
# Create your views here.



def signup(request):
    
    home = ''

    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            auth_login(request,user)
            return redirect('/index')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form,'home':home,})


from django.views.generic.edit import CreateView

# بتزبط لو فش كستم يوزر
# class SignUpView(CreateView):
#     template_name = 'registration/signup.html'
#     form_class = UserCreationForm




# import json

# from django.http import JsonResponse
# from django.contrib.auth import get_user_model



# def validate_username(request): 
#     username = request.GET.get('username')
#     is_taken = get_user_model.objects.filter(username__iexact=username).exists()
#     data = {'is_taken':is_taken}
#     if data['is_taken']: 
#         data['error_message'] = "The username already taken"
#     return JsonResponse(data)



# def signup(request):
#     form = UserCreationForm()
#     if request.method=="POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             authenticate.login(request,user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request,'registration/signup.html',{'form':form})




# def profile(request):
#     profile = Profile.objects.get(user=request.user)
#     return render(request,'accounts/profile.html',{'profile': profile})



def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('profile'))

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})