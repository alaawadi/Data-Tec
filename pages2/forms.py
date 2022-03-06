from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class BlogForm(forms.ModelForm):
    # blog_Category = forms.ModelChoiceField(queryset=blog_Category.objects.all(), initial=0)
    # Project_Category = forms.ModelChoiceField(queryset=Project_Category.objects.all(), initial=0)
    # course = forms.ModelChoiceField(queryset=Course.objects.all(), initial=0)
    class Meta:
        model = BlogModel
        fields = [ 'title','image', 'content','small_desc','blog_Category']
        widgets = {
        
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
           
            'small_desc': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'blog_Category': forms.Select(
                attrs={
                    'class': 'form-control'
                }),


        
        }
    
    
    
    
    
class ProjectForm(forms.ModelForm):
    # blog_Category = forms.ModelChoiceField(queryset=blog_Category.objects.all(), initial=0)
    # Project_Category = forms.ModelChoiceField(queryset=Project_Category.objects.all(), initial=0)
    # course = forms.ModelChoiceField(queryset=Course.objects.all(), initial=0)
    class Meta:
        model = BlogModel
        fields = ['title','image','content','small_desc','project_Category']
        widgets = {
        
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
           
            'small_desc': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'project_Category': forms.Select(
                attrs={
                    'class': 'form-control'
                }),


        
        }
    
    
    
  
class servForm(forms.ModelForm):
    # blog_Category = forms.ModelChoiceField(queryset=blog_Category.objects.all(), initial=0)
    # Project_Category = forms.ModelChoiceField(queryset=Project_Category.objects.all(), initial=0)
    # course = forms.ModelChoiceField(queryset=Course.objects.all(), initial=0)
    class Meta:
        model = BlogModel
        image = forms.ImageField(required=True)
        fields = ['title','image','content','small_desc']
        widgets = {
        
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
           
            'small_desc': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            
            
            

        
        }
    
    
    
    
    

class courseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','img','disc','category']
        widgets = {
        
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'disc': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }),
            

        
        }
        
    
    

class videoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video','title','content','course']
        widgets = {
        
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),

        }        
        
        

class lessonForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title','image','content','course','is_project','project_Category','is_blog','blog_Category']
        widgets = {
        
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),

            'course': forms.Select(
                attrs={
                    'class': 'form-control'
                }),
            
            
        }        