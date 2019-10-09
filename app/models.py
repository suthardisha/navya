from django.db import models

# Create your models here


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    roal = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.role

    
class doctor(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    qualifiction = models.CharField(max_length=20,blank=True)
    speciality = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20,blank=True)
    clinic= models.CharField(max_length=20,blank=True)
    adress = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=20,blank=True)
    state = models.CharField(max_length=20,blank=True)
    gender= models.CharField(max_length=20,blank=True)
    location = models.CharField(max_length=20,blank=True)
    birthdate = models.DateField()
    about_doc = models.CharField(max_length=20,blank=True)
    # profile_pic = models.File.Field(upload_to="D/Image/",default='doc.jpg')

    def __str__(self):
        return self.firstname


class patient(models.Model):

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20,blank=True)
    clinic= models.CharField(max_length=20,blank=True)
    adress =models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=20,blank=True)
    state = models.CharField(max_length=20,blank=True)
    gender= models.CharField(max_length=20,blank=True)
    location = models.CharField(max_length=20,blank=True)
    birthdate = models.DateField()
    blood_group = models.CharField(max_length=20,blank=True)
    blood_pressure = models.CharField(max_length=20,blank=True)
    # profile_pic = models.File.Field(upload_to="D/Image/",default='doc.jpg')

    def __str__(self):
        return self.firstname
        

