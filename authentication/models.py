from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# class User(AbstractUser):
#     # user = models.ForeignKey(User,on_delete=models.CASCADE,max_length=300, related_name='User')
#     is_email_verified = models.BooleanField(default=False)
    

#     def __str__(self):
#         return self.email
