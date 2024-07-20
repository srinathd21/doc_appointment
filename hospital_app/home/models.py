from django.db import models
import datetime
import os

# Create your models here.

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
    type = models.CharField(max_length = 150, null=False, blank = False)
    image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    avelable=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type
    
class Doctors(models.Model):
    category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    id_number = models.TextField(max_length=255, null=False, blank=False)
    qulification=models.CharField(max_length=150,null=False,blank=False)
    contact = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=128, null=False, blank=False)
    doc_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    special=models.TextField(max_length=500,null=False,blank=False)
    languages=models.TextField(max_length=100,null=False,blank=False)
    experience=models.IntegerField(null=False,blank=False)
    fees=models.FloatField(null=False,blank=False)
    avel_dates=models.TextField(max_length=100,null=False,blank=False)
    in_out_time=models.TextField(max_length=50,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    doc_avelable=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    address = models.TextField(max_length=255, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    # Your fields here
    pid = models.CharField(max_length=20)
    doctor = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    fh = models.CharField(max_length=50,default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    contact = models.CharField(max_length=20)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class prescription(models.Model):
    doctor = models.CharField(max_length=255,default=0)
    name = models.CharField(max_length=255)
    fh = models.CharField(max_length=100)
    nadate = models.CharField(max_length=20,default=0)
    description = models.TextField()
    prc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
