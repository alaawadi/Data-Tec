from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import *
# # Register your models here.


admin.site.site_header= 'Data Tec'
admin.site.site_title= 'Personal websit'
# بهادي الطريقة بغير التايتل والهيدر

# class BLOGSadmin(admin.ModelAdmin):
#     fields=('img','title','description')
#     # بهادي الطريقة بتحكم بالفايلد الي بدي اياها تظهر فالادمن
#     list_display= ('title','create_py','description')
#         # بهادي الطريقة بعرض عناصر كل اوبجيكت على جنب اسمه
#     list_display_links=('description',)
#     # حولنا هدول الفيلد للينات 
#     list_editable=('title',)
#     # الي بيظهر فاللينك ما بنفع اعدله
#     # list_filter=('description','title',)
#     search_fields=('title',)

# # class BLOGSadmin(admin.ModelAdmin):
# #     fieldsets = (
# #         ('sec1', {
# #             'fields': ( 'img','create_py'),
# #         }),
        
# #         ('sec2', {
# #             'fields': ( 'date','title','description'),
# #         }),
# #     )
    
    
    
    
# # class inline_Category(admin.StackedInline):
# #     model= Category
# #     extra=1
    
# # class PORTFOLIO_admin(admin.ModelAdmin):
# #     inlines = [inline_Category]
    
admin.site.register(Home )
admin.site.register(Coding_Skills)
admin.site.register(Professional_Skills)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(SERVICES)
admin.site.register(Category)
# admin.site.register(PORTFOLIO)
# admin.site.register(BLOGS,BLOGSadmin)
admin.site.register(CONTACT_ME)
admin.site.register(Location)
admin.site.register(Message)
admin.site.register(file)
# admin.site.register(CustomUser)
# admin.site.unregister(Group)
# admin.site.unregister(User)

