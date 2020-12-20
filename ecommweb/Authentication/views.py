from django.conf import settings
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.core.mail import send_mail
import random
from django.http import HttpResponse

def otpGenerator():
    otp=""

    for i in range(6):
      x=random.randint(0,9)
      otp +=  str(x)  
    return int(otp)

def verify_otp(request):
    
    
    if request.method=="POST":
        
        user_otp = request.POST['otp']
        print("user otp : ",user_otp)
        sys_otp = request.session['sys_otp']
        print("sys_otp : ",sys_otp)
        
        if int(user_otp) == sys_otp:
            print("user saved")  
                        
            user = User.objects.create_user(username=request.session['username'],password=request.session['password'],email=request.session['email'])
            user.save()
            print("user details saved")
            del request.session['username']
            del request.session['password']
            del request.session['email']
            del request.session['sys_otp']
            
            Profile.objects.create(
            user = user,
            first_name = request.session['first_name'],
            #print("user fn : ",Profile.first_name)
            last_name = request.session['last_name'],
            contact_no = request.session['contact_no'],
            address1 = request.session['address1'],
            city = request.session['city'],
            state = request.session['state'],
            pincode = request.session['pincode'])
            
            print('profile form saved')
            login(request,user)
            
            return redirect("shopHome")
            
# Here both user obj and profile obj can be useful while accessing their fields via .name1 in html file    

        else:
            print('user not saved')
            return render(request, 'verify_otp.html',{ 'error':'OTP didnot match'})

    return render(request,'verify_otp.html')

def SignupUSER(request):
    if(request.method=="GET"):
        return render(request,"SignUp.html",{'fname':'demo','profileform':UserProfileForm()})
    else:
        #Create a user
        #First check both passwords matched
        if(request.POST['PassWord1']==request.POST['PassWord2']):

            #Then check proper username..1)alphabets+nums=alphanums 2)all nums not and not any special chars. 3)length not more than 15 --means only alphabets or alpha+nums valid.
            if (not request.POST['UserName'].isalnum() or request.POST['UserName'].isdecimal() or len(request.POST['UserName'])>15):
                print("error")
                return render(request, 'SignUp.html',{'profileform':UserProfileForm(), 'error':"Username should not contain any special characters and length must be less than 15 characters"})

            #If proper then go
            else:
                #Then See this username used by someone?
        
                try:
                    
                    if not User.objects.filter(username=request.POST['UserName']).exists():
                        
                        #send_mail
                        sys_otp = otpGenerator()
                        subject = 'VERIFY YOUR EMAIL'
                        message = f'{sys_otp} is the OTP to register.'
                        print(message)
                        email_from = settings.EMAIL_HOST_USER 
                        recipient_list = [request.POST['email'], settings.EMAIL_HOST_USER] 
                        send_mail(subject, message, email_from, recipient_list) 

                        request.session['username'] = request.POST['UserName']
                        request.session['password'] = request.POST['PassWord1']
                        request.session['email'] = request.POST['email']
                        request.session['sys_otp'] = sys_otp
                        request.session['first_name'] = request.POST['first_name']
                        request.session['last_name'] = request.POST['last_name']
                        request.session['contact_no'] = request.POST['contact_no']
                        request.session['address1'] = request.POST['address1']
                        request.session['city'] = request.POST['city']
                        request.session['state'] = request.POST['state']
                        request.session['pincode'] = request.POST['pincode']
                        
                        return redirect('verify_otp')  
                        profile_form = UserProfileForm(request.POST)
# Here name1 = req.post[name2]. in which name1 can be anything and used when accessing User detail in html file,and name2 must be same as provided by default styling of django user signin in Users model (for lastname = last_name,Email=email)
                                                    
                    else:
                        return render(request,'SignUp.html',{'profileform':UserProfileForm(),'error':'Username already taken'})


                except IntegrityError:
                    return render(request, 'SignUp.html',{'profileform':UserProfileForm(),'error':'Username already taken'})
        else:
            return render(request,'SignUp.html',{'fname':'demo','profileform':UserProfileForm(),'error':"Passwords didn't match."})

def LoginUSER(request):
    if (request.method == 'GET'):
        return render(request, 'LoginPage.html')
    else:
        user = authenticate(request,username=request.POST['UserName'],password=request.POST['PassWord'])

        if user is None:
            return render(request, 'LoginPage.html', {'error': "Don't match username and password"})
        else:
            login(request, user)
            return redirect('shopHome')

def LogoutUSER(request):
    if request.method == 'POST':
        logout(request)
        return redirect('shopHome')


def account(request):
    status1 = False
    status2 = False
    x = get_object_or_404(Profile,user=request.user)
    
    if(x.default_address_value==1):
        status1 =True
        # print("status1 set")
    elif(x.default_address_value==2):
        status2 =True
        # print("status2 set")

    if request.method == 'GET':
        f = UserProfileForm(instance=x)
        
        # print("stat1 : ",status1 , "stat2 ",status2)
        return render(request,'Account.html',{'obj':x,'form':f,'status1':status1,'status2':status2})
    else:
        return render(request,'Account.html')
    
    return render(request,'Account.html',{'obj':x})

def add_address(request):
    if request.method == 'GET':
        return render(request, 'Add_address.html', {'form': UserProfileForm()})
    else:
        try:
            active_user = request.user
            x = Profile.objects.get(user=active_user)    
            
            if(x.address1 == ""):
                x.first_name = request.POST.get('first2')
                x.last_name = request.POST.get('last2')
                x.contact_no = request.POST.get('contact2')
                x.address1 = request.POST.get("ad2")
                x.pincode = request.POST.get('pin2')
                x.state = request.POST.get('st2')
                x.city = request.POST.get('cit2')
            else:    
                x.first_name2 = request.POST.get('first2')
                x.last_name2 = request.POST.get('last2')
                x.contact_no2 = request.POST.get('contact2')
                x.address2 = request.POST.get("ad2")
                x.pincode2 = request.POST.get('pin2')
                x.state2 = request.POST.get('st2')
                x.city2 = request.POST.get('cit2')
            x.save()
         
            return redirect('Account')
        except ValueError:
            return render(request, 'Add_address.html', {'form': UserProfileForm(), 'error': 'Bad values passed'})


def account_settings_1(request):
    x = get_object_or_404(Profile,user=request.user)
    # print(x)
    if request.method == 'GET':
        f = UserProfileForm(instance=x)
        return render(request, 'Account_settings_1.html', {'obj': x, 'form': f})
    else:
        try:
            f = UserProfileForm(request.POST, instance=x)
            f.save()
            return redirect('Account')
        except ValueError:
            return render(request, 'Account_settings_1.html', {'form': f, 'error': 'Bad values passed'})

def account_settings_2(request):
    x = get_object_or_404(Profile,user=request.user)        
    # print(x)
    if request.method == 'GET':
        f = UserProfileForm(instance=x)
        return render(request, 'Account_settings_2.html', {'obj': x, 'form': f})
    else:
        try:
            user_profile = Profile.objects.get(user=request.user)
 
            f = UserProfileForm(request.POST, instance=x)
            
            user_profile.address2 = request.POST.get('address2')
            user_profile.first_name2 = request.POST.get('first_name2')
            user_profile.pincode2 = request.POST.get('pincode2')
            user_profile.last_name2 = request.POST.get('last_name2')
            user_profile.state2 = request.POST.get('state2')
            user_profile.city2 = request.POST.get('city2')
            user_profile.contact_no2 = request.POST.get('contact_no2')
            user_profile.save()
            
            return redirect('Account')
        except ValueError:
            return render(request, 'Account_settings_2.html', {'form': f, 'error': 'Bad values passed'})


def set_default_address(request):
    
    if request.method=="GET":
        return redirect('Account')
    else:

        x = Profile.objects.get(user = request.user)
        addval = request.POST.get('value')
        # print(addval)
        if(addval=="1"):
            x.default_address_value = 1
            # print("1 setted")
        elif (addval=="2"):
            x.default_address_value = 2
            # print("2 setted")
        x.save()
        return redirect("Account")

    return render(request,'Account.html')
    

def deleteAd(request,objId):
    x = get_object_or_404(Profile,user=request.user)
    
    if request.method == 'POST':
        if(objId==1):
            print("Address1 is deleted ...")
            x.first_name = x.first_name2
            x.last_name = x.last_name2
            x.contact_no = x.contact_no2
            x.address1 = x.address2
            x.city = x.city2
            x.state = x.state2
            x.pincode = x.pincode2
            x.first_name2 = ""
            x.last_name2 = ""
            x.contact_no2 = 0
            x.address2 = ""
            x.city2 = ""
            x.state2 = ""
            x.pincode2 = 0
            x.default_address_value = 1

        elif(objId==2):
            print("Address2 is deleted ...")
            x.first_name2 = ""
            x.last_name2 = ""
            x.contact_no2 = 0
            x.address2 = ""
            x.city2 = ""
            x.state2 = ""
            x.pincode2 = 0
            x.default_address_value = 1

        x.save()

        return redirect('Account')

