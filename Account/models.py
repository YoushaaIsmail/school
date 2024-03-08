from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django_resized import ResizedImageField

import os
def upload_to(inst,filename):
      base_path="profile"
      safe_filename=str(filename)
      final_path=os.path.join(base_path,safe_filename)
      return final_path
class Account(AbstractUser):
        listt=(
       ('parent', 'Parent'),
       ('teacher', 'Teacher'),
       ('supervisor', 'Supervisor'),
      ('employee', 'Employee')
)
        email=models.EmailField(unique=True)
        phone=models.CharField(max_length=15)
        first_name=models.CharField(max_length=30)
        last_name=models.CharField(max_length=30)
        photo=ResizedImageField(upload_to=upload_to,null=True,blank=True)
        identity=models.CharField(max_length=15,choices=listt)


class Parent(models.Model):
        account=models.OneToOneField(Account,on_delete=models.CASCADE,
            related_name='parent', null=True, blank=True)
        
