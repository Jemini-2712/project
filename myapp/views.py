#from import email
#from import imp

from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from random import choices,randrange
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'index.html',{'uid':uid})
    except:
        return render(request,'sign-in.html',{'msg':'session has expired'})    

def sign_in(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            if request.POST['password'] == uid.password:
                request.session ['email'] = request.POST['email']
                return redirect('dashboard')
            return render(request,'sign-in.html',{'msg':'password is incorrect'})    
        except:
            return render(request,'sign-in.html',{'msg':'Account does not exist'})
    return render(request,'sign-in.html')

def sign_up(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg = "Email Already Exist"
            return render(request,'sign-up.html',{'msg':msg})
        except:
           if request.POST['password'] == request.POST['cpassword']:
                otp = randrange(1000,9999)
                subject = 'OTP verification'
                message = f'Your otp is {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp 
                temp = {
                    'fname' : request.POST['fname'],
                    'lname' : request.POST['lname'],
                    'email' : request.POST['email'],
                    'mobile' : request.POST['mobile'],
                    'password' : request.POST['password'],
                }
                return render(request,'otp.html',{'msg':'OTP sent on your email','otp':otp})
        return render(request,'sign-up.html',{'msg':'Both are not same'}) 
    return render(request,'sign-up.html') 
 
def profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.mobile = request.POST['mobile'][4:]
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.address = request.POST['address']
        uid.save()
        return render(request,'profile.html',{'uid':uid,'msg':'Profile has been updated successfully'})
    return render(request,'profile.html',{'uid':uid})


def rtl(request):
    return render(request,'rtl.html')

def virtual_reality(request):
    return render(request,'virtual-reality.html')

def dashboard(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'dashboard.html',{'uid':uid})

def otp(request):
    if request.POST['uotp'] == request.POST['otp']:
        global temp
        User.objects.create(
            fname = temp['fname'],
            lname = temp['lname'],
            email = temp['email'],
            mobile = temp['mobile'],
            password = temp['password'],
        )
        del temp
        return render(request,'sign-in.html',{'msg':'Account Created!!'})
    return render(request,'otp.html',{'msg':'Invalid OTP','otp':request.POST['otp']})

def logout(request):
    del request.session['email']
    return render(request,'sign-in.html')

def forgot_psw(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])  
            s = 'dnfckqwertwshfbwdkfihwehdbkjedhbcdg1234567890'
            password = ''.join(choices(s,k=8))
            subject = 'Password Has been Reset'
            message = f'Your New Password is {password}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            uid.password = password
            uid.save()
            return render(request,'forgot-psw.html',{'msg':'New Password sent on your email'})
        except:
            return render(request,'forgot-psw.html',{'msg':'Account does not exist'})
    return render(request,'forgot-psw.html')

def service(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Service.objects.create(
            provider = uid,
            name = request.POST['sname'],
            sector = request.POST['sector'],
            min_charge = request.POST['charge'],
            des = request.POST['des'],
            area = request.POST['area']
        )
        msg = 'YOur service added successfully'

        return render(request,'service.html',{'uid': uid,'msg':msg})
    return render(request,'service.html',{'uid': uid})