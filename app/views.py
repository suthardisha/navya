from django.shortcuts import render
from .models import *
from random import randint

# Create your views here.
def IndexView(request):
    return render(request,"app/app.html")

def registeruser(request):
    try:
        if request.POST['role']=='doctor':
             role=request.POST['role']
             firstname=request.POST['firstname']
             lastname=request.POST['lastname']
             password=request.POST['password']
             confirmpassword=request.POST['confirmpassword']
             gender=request.POST['gender']
             email=request.POST['email']
             speciality=request.POST['speciality']
             birthdate=request.POST['birthdate']
             city=request.POST['city']
             mobile=(request.POST['phone'])

             user1 = User.objects.filter(email=email)

             if user1:
                 message='This email already exits'
                 return render(request, 'app/app.html',{'message':message})

             else :
                  if password==confirmpassword:
                      otp=randint(10000,99999)
                      newuser = User.objects.create(email=email, password=password, roal=role)
                      newdoctor=doctor.objects.create(user_id=newuser,firstname=firstname,lastname=lastname,gender=gender,speciality=speciality,city=city,mobile=mobile,birthdate=birthdate)
                      return HttpResponseRedirect(reverse('p_data'))
                  else:
                    message='password does not match'
                    return render(request,'app/app.html',{'message':message})
        else:
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            confirmpassword = request.POST['confirm']
            gender = request.POST['gender']
            email = request.POST['email']
            birthdate = request.POST['birthdate']
            city = request.POST['city']
            mobile = str(request.POST['phone'])
            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request, 'app.html', {'message': message})
            else:
                if password == confirmpassword:
                    otp = randint(100000, 9999999)
                    newuser = User.objects.create(
                        email=email, password=password, role=role, otp=otp)
                    newpatient = Patient.objects.create(user_id=newuser, firstname=firstname, lastname=lastname, gender=gender, city=city, mobile=mobile, birthdate=birthdate)
                    return HttpResponseRedirect(reverse('D_data'))
                    
                   
                else:
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app.html', {'message': message})

                
    except User.DoesNotExist:
        message = 'This email already exists'
        return render(request, 'app.html', {'message': message})
def Patientdata(request):
    Patientdata = Patient.objects.all()
    return render(request,'app/sucess.html',{'Patientdata':Patientdata})
def doctordata(request):
    doctordata = doctor.objects.all()
    return  render(request,'app/sucess.html',{'doctordata':doctordata})

         