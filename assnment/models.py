from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
 


#class Person(User):

   # start_time=models.DateTimeField(auto_now=True)
   # tz=models.DateTimeField(default=timezone.now)
   # endtime=models.DateTimeField(auto_now=True)

    #class Meta:
     #   proxy=True
        
#class information(models.Model):
    #userid=models.ForeignKey(User,on_delete=models.CASCADE,related_name="loginid")
    #sername=models.ForeignKey(User,on_delete=models.CASCADE,related_name="loginname")
    #start_time=models.DateTimeField(auto_now=True)
    #tz=models.DateTimeField(default=timezone.now)

#class logoutinfrmation(models.Model):
   #  logoutuserid=models.ForeignKey(User,on_delete=models.CASCADE)
    # endtime=models.DateTimeField(auto_now=True)
#
# Create your models here.
