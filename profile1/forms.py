from django import forms
from .models import Home,Coding_Skills,Professional_Skills,Experience,Education,file,SERVICES,Category,CONTACT_ME,Location
from pages2.models import BlogModel



class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['image','name','desciption']
        widgets = {
        
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
           

            'desciption': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),}
  
        
        
        
                
        
class Coding_SkillsForm(forms.ModelForm):
    class Meta:
        model = Coding_Skills
        fields = ['skl','mea']
        widgets = {
        
            'skl': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
           
            'mea': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }),}
        
        
        
        
class Professional_SkillsForm(forms.ModelForm):
    class Meta:
        model = Professional_Skills
        fields = ['skl','mea']
        widgets = {
        
            'skl': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
           
            'mea': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }),}
        
        
        
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title','discription']
        widgets = {
        
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
           
            'discription': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),}
            
        
        
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['title','discription']
        widgets = {
        
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
           
            'discription': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),}
        
        
        
class fileForm(forms.ModelForm):
    class Meta:
        model = file
        fields = ['file']
        widgets = {
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }),}   
        
        
        
        
class SERVICESForm(forms.ModelForm):
    class Meta:
        model = SERVICES
        fields = ['img','title','discription']
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
        
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title','content','image','small_desc']
        
        
