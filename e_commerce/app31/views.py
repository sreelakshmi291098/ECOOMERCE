from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login
from app31.models import Reg,Product
from django.contrib.auth.models import User
from django.contrib import messages
from.import models
# Create your views here.
def index(request):
    data=Product.objects.all()
    
    return render(request,'index.html',{'data':data})

def product(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.POST.get('image')
        status="0"
        userDetail=models.Product(name=name,description=description,price=price,image=image,status=status)
        userDetail.save()
        return redirect("index")
        
    else:
        return render(request,'product.html')
role=""
roles=""
def loginpage(request):
    global role
    global roles
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        data=User.objects.filter(username=username).values()
        print("userModelData==>",data)
        for i in data:
            id=i['id']
            u_name=i['username']
            print(".............",id,u_name)
 
            da=Reg.objects.filter(user_id=id).values()
            print("regdata==>",da)
            for i in da:
                roles=i['role']
                statuss=i['status']
                print(roles)

            

            user=authenticate(username=username,password=password)

            if user is not None and roles=='customer' and username==u_name and status=="1":
                auth_login(request,user)
                return redirect("customer")
            elif username=="sreelakshmi" and password=="sree123":
                return redirect("adminpage")

            
            else:pass
        else:
            messages.info(request,'Invalid credentials')
            return redirect("loginpage")
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        name=request.POST.get("name")
        username=request.POST.get("username")
        password1=request.POST.get("password")
        password2=request.POST.get("conformpassword")
        address=request.POST.get("address")
        email=request.POST.get("email")
        phonenumber=request.POST.get("phonenumber")
        gender=request.POST.get("gender")
        status="0"
        role="customer"

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()
                userDetail=models.Reg(user=user,name=name,address=address,email=email,phone_number=phonenumber,gender=gender,status=status,role=role)
                userDetail.save()

                print('user created')
        else:
            messages.info(request,"password is not matching")
            return redirect("register")
        return redirect("loginpage")
    else:
        return render(request,'registration.html')

def customer(request):
    return render(request,'customer.html')

def adminpage(request):
    return render(request,'admin.html')

def userpending(request):
    data=Reg.objects.all()
    return render(request,'viewuserpending.html',{'data':data})

def user_approve(request,reg_id):
    reg=Reg.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect("userpending")

def user_reject(request,reg_id):
    item=Reg.objects.get(id=reg_id)
    item.delete()
    messages.info(request,'delete successfull')
    return redirect("userpending")

def approveduser(request):
    data=Reg.objects.all()
    return render(request,'approveduser.html',{'data':data})

def user_delete(request,reg_id):
    add=Reg.objects.get(id=reg_id)
    add.delete()
    return redirect('approveduser')

def add_cart(request,reg_id):
    reg=Product.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect("index")

def cart(request):
    data=Product.objects.all()
    return render(request,'cart.html',{'data':data})

def pay(request):
    data=Product.objects.all()
    return render(request,'payment.html',{'data':data})

def buy_now(request,reg_id):
    reg=Product.objects.get(id=reg_id)
    reg.status=2
    reg.save()
    return redirect("pay")