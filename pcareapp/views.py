from django.shortcuts import render
from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
import pymysql
import datetime
import smtplib 
import urllib.request
import webbrowser
from django.contrib import messages

#Create your Database connection
# con = pymysql.connect("localhost","root","","pcare")

con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="pcare"
)
c = con.cursor()
# Create your views here.
def sendsms(ph,msg):

    sendToPhoneNumber= "+91"+ph
    userid = "2000022557"
    passwd = "54321@lcc"
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)

def login(request):
    msg=""
    if request.POST:
        try:
            user_name = request.POST.get("uid")
            password = request.POST.get("pswd")
            s = "select * from login where user_name='"+str(user_name)+"' and password='"+str(password)+"'"
            print(s)
            c.execute(s)
            con.commit()
            log_count = c.fetchone()
            print(log_count)
            
            if log_count[4] == "public":
                request.session["u_id"]=log_count[2]
                # request.session["username"]=log_count[2]
                # request.session["type"]=log_count[4]
                return HttpResponseRedirect("/usrhome") 
            else:
                msg = "Invalid User"
                return render(request,"login.html",{"msg":msg}) 
        
        except:
            msg = "Invalid User"
            return render(request,"login.html",{"msg":msg})

    return render(request,"login.html")
def loginadmin(request):
    msg=""
    if request.POST:
        try:
            user_name = request.POST.get("uid")
            password = request.POST.get("pswd")
            s = "select * from login where user_name='"+str(user_name)+"' and password='"+str(password)+"'"
            print(s)
            c.execute(s)
            con.commit()
            log_count = c.fetchone()
            print(log_count)
            if log_count[4] == "admin":
                return HttpResponseRedirect("/adminhome")
            else:
                msg = "Invalid User"
                return render(request,"loginadmin.html",{"msg":msg}) 
        
        except:
            msg = "Invalid User"
            return render(request,"loginadmin.html",{"msg":msg})

    return render(request,"loginadmin.html")
def loginclerk(request):
    msg=""
    if request.POST:
        try:
            user_name = request.POST.get("uid")
            password = request.POST.get("pswd")
            s = "select * from login where user_name='"+str(user_name)+"' and password='"+str(password)+"'"
            print(s)
            c.execute(s)
            con.commit()
            log_count = c.fetchone()
            print(log_count)
            
            if log_count[4] == "clerk":
                request.session["u_id"]=log_count[2]
                # request.session["username"]=log_count[2]
                # request.session["type"]=log_count[4]
                return HttpResponseRedirect("/clerkhome") 
            else:
                msg = "Invalid User"
                return render(request,"loginclerk.html",{"msg":msg}) 
        
        except:
            msg = "Invalid User"
            return render(request,"loginclerk.html",{"msg":msg})

    return render(request,"loginclerk.html")
def loginauthority(request):
    msg=""
    if request.POST:
        try:
            user_name = request.POST.get("uid")
            password = request.POST.get("pswd")
            s = "select * from login where user_name='"+str(user_name)+"' and password='"+str(password)+"'"
            print(s)
            c.execute(s)
            con.commit()
            log_count = c.fetchone()
            print(log_count)
           
            if log_count[4] == "authority":
                request.session["u_id"]=log_count[2]
                print(log_count[2])
                # request.session["username"]=log_count[2]
                # request.session["type"]=log_count[4]
                return HttpResponseRedirect("/authorityhome")
            else:
                msg = "Invalid User"
                return render(request,"loginathority.html",{"msg":msg}) 
        
        except:
            msg = "Invalid User"
            return render(request,"loginathority.html",{"msg":msg})

    return render(request,"loginathority.html")

def authlog(request):
    role="authority"
    print("hai")
    msg=" "
    if request.POST:
        print("hello")
        name=request.POST.get("name")
        aid=request.POST.get("a_id")
        office=request.POST.get("office")
        phno=request.POST.get("phno")
        district=request.POST.get("district")
        email=request.POST.get("email")
        password=request.POST.get("pswd")
        c_count = "select count(*) from authorityreg where email = '"+str(email)+"' and phno= '"+str(phno)+"' and role='Authority'"
        c.execute(c_count)
        con.commit()
        data = c.fetchone()
        print(data)
        if data[0] == 0:
            s="insert into authorityreg(`name`,`aid`,`office`,`phno`,`district`,`email`,`password`,`role`)values('"+str(name)+"','"+str(aid)+"','"+str(office)+"','"+str(phno)+"','"+str(district)+"','"+str(email)+"','"+str(password)+"','"+str(role)+"')"
            print(s)
            c.execute(s)
            con.commit()
            print("hello")
            s1 = "insert into login(`register_id`,`user_name`,`password`,`role`) values((select max(aregister_id) from authorityreg),'"+str(phno)+"','"+str(password)+"','"+str(role)+"')"
            c.execute(s1)
            con.commit()
            msg = "User Registered Successfully"
            return render(request,"authlog.html",{"msg":msg})
        else: 
            msg = "Account Already Exists"
            return render(request,"authlog.html",{"msg":msg})
    return render(request,"authlog.html")
def clerkreg(request):
    role="clerk"
    print("hai")
    msg=" "
    if request.POST:
        print("hello")
        name=request.POST.get("name")
        aid=request.POST.get("a_id")
        office=request.POST.get("office")
        phno=request.POST.get("phno")
        district=request.POST.get("district")
        email=request.POST.get("email")
        password=request.POST.get("pswd")
        c_count = "select count(*) from clerk where email = '"+str(email)+"' and phno= '"+str(phno)+"' and role='Authority'"
        c.execute(c_count)
        con.commit()
        data = c.fetchone()
        print(data)
        if data[0] == 0:
            s="insert into clerk(`name`,`aid`,`office`,`phno`,`district`,`email`,`password`,`role`)values('"+str(name)+"','"+str(aid)+"','"+str(office)+"','"+str(phno)+"','"+str(district)+"','"+str(email)+"','"+str(password)+"','"+str(role)+"')"
            print(s)
            c.execute(s)
            con.commit()
            print("hello")
            s1 = "insert into login(`register_id`,`user_name`,`password`,`role`) values((select max(aregister_id) from clerk),'"+str(phno)+"','"+str(password)+"','"+str(role)+"')"
            c.execute(s1)
            con.commit()
            msg = "User Registered Successfully"
            return render(request,"clerkreg.html",{"msg":msg})
        else: 
            msg = "Account Already Exists"
            return render(request,"clerkreg.html",{"msg":msg})
    return render(request,"clerkreg.html")

def publicreg(request):   
    role="public"
    print("hai")
    msg=" "
    if request.POST:
        print("hello")
        name=request.POST.get("name")
        address=request.POST.get("address")
        age=request.POST.get("age")
        phno=request.POST.get("phno")
        dob=request.POST.get("dob")
        gender=request.POST.get("gender")
        email=request.POST.get("email")
        password=request.POST.get("pswd")
        c_count = "select count(*) from userreg where email = '"+str(email)+"' and phno= '"+str(phno)+"' and role='public'"
        c.execute(c_count)
        con.commit()
        data = c.fetchone()
        print(data)
        if data[0] == 0:
            s="insert into userreg(`name`,`address`,`age`,`phno`,`dob`,`gender`,`email`,`password`,`role`)values('"+str(name)+"','"+str(address)+"','"+str(age)+"','"+str(phno)+"','"+str(dob)+"','"+str(gender)+"','"+str(email)+"','"+str(password)+"','"+str(role)+"')"
            print(s)
            c.execute(s)
            con.commit()
            print("hello")
            s1 = "insert into login(`register_id`,`user_name`,`password`,`role`) values((select max(register_id) from userreg),'"+str(phno)+"','"+str(password)+"','"+str(role)+"')"
            c.execute(s1)
            con.commit()
            msg = "User Registered Successfully"
            return render(request,"publicreg.html",{"msg":msg})
            return HttpResponseRedirect("/login")
        else: 
            msg = "Account Already Exists"
            return render(request,"publicreg.html",{"msg":msg})
    return render(request,"publicreg.html")

def usrhome(request):
    msg="User logged in"
    return render(request,"usrhome.html",{"msg":msg})
def applypension(request):
    status="applied"
    uid=request.session["u_id"]
    msg=" "
    category=request.GET.get("category")
    amount=request.GET.get("amount")
    print(category)
    if request.POST.get("submit"):
        myfile1 = request.FILES["proof"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile1.name, myfile1)
        uploaded_file_url = fs.url(filename)
        bank=request.POST.get("bank")
        c_count = "select count(*) from pension where register_id= '"+str(uid)+"' and category= '"+str(category)+"'"
        c.execute(c_count)
        con.commit()
        data1= c.fetchone()
        if data1[0] == 0:
            s1 = "insert into pension(`register_id`,`category`,`bank`,`proof`,`status`,`amount`) values('"+str(uid)+"','"+str(category)+"','"+str(bank)+"','"+str(filename)+"','"+str(status)+"','"+str(amount)+"')" 
            c.execute(s1)
            con.commit()
            msg = "User Applied for pension"
        else:
            msg="already applied"
    b="select * from pension where register_id='"+str(uid)+"'"
    c.execute(b)
    data=c.fetchall()
    print(data)
    return render(request,"applypension.html",{"uid":uid,"msg":msg,"data":data,"category":category,"amount":amount})

def about(request):
    print("------------------inside about-------------------")

    return render(request,"about.html")

def feedback(request):
    print("------------------inside feedback-------------------")
    uid=request.session["u_id"]
    if 'submit' in request.POST:
        msg = request.POST.get("msg")
        s = " insert into feedback(`user_id`,`message`) values('"+str(uid)+"','"+str(msg)+"')"
        c.execute(s)
        con.commit()
        alert= "Successfully Submitted"
        return render(request,"feedback.html",{"msg":alert})
    return render(request,"feedback.html")

def authorityhome(request):
    msg="authority logged in"
    return render(request,"authorityhome.html",{"msg":msg})
def mainhome(request):
    
    return render(request,"mainhome.html")

def bank1(request):
    st="applied"
    b="select * from pension where status='"+str(st)+"'" 
    c.execute(b)
    data=c.fetchall()
    b="select proof from pension where status='"+str(st)+"'" 
    c.execute(b)
    data4=c.fetchone()
    fl="approved"
    y="select * from pension where status='"+str(fl)+"'" 
    c.execute(y)
    data1=c.fetchall()
    de="rejected"
    u="select * from pension where status='"+str(de)+"'" 
    c.execute(u)
    data2=c.fetchall()
    if request.POST.get("accept"):
        status="approved"
        d="update pension set status='"+str(status)+"'"
        print(d)
        c.execute(d)
        con.commit()
    if request.POST.get("reject"):
        status="rejected"
        d="update pension set status='"+str(status)+"'"
        print(d)
        c.execute(d)
        con.commit()
    return render(request,"bank1.html",{"data":data,"data1":data1,"data2":data2,"data4":data4})

def bank(request):
    st="applied"
    b="select * from pension where status='"+str(st)+"'" 
    c.execute(b)
    data=c.fetchall()
    b="select proof from pension where status='"+str(st)+"'" 
    c.execute(b)
    data4=c.fetchone()
    fl="approved"
    y="select * from pension where status='"+str(fl)+"'" 
    c.execute(y)
    data1=c.fetchall()
    de="rejected"
    u="select * from pension where status='"+str(de)+"'" 
    c.execute(u)
    data2=c.fetchall()
    if request.POST.get("accept"):
        status="approved"
        d="update pension set status='"+str(status)+"'"
        print(d)
        c.execute(d)
        con.commit()
    if request.POST.get("reject"):
        status="rejected"
        d="update pension set status='"+str(status)+"'"
        print(d)
        c.execute(d)
        con.commit()
    return render(request,"bank.html",{"data":data,"data1":data1,"data2":data2,"data4":data4})
def deposit(request):
    uid=request.session["u_id"]
    k="select * from deposit where aregister_id='"+str(uid)+"'"
    c.execute(k)
    data3=c.fetchall()
    print(data3)
    h="select register_id from pension"
    c.execute(h)
    data2=c.fetchall()
    l="select * from pension"
    print(data2)
    if request.POST.get("submit"):
        bank_name = request.POST.get("bank")
        month = request.POST.get("month")
        amount=request.POST.get("amount")
        ss="select count(*) from deposit where bank_name='"+str(bank_name)+"' AND month='"+str(month)+"'"
        c.execute(ss)
        data1 = c.fetchone()
        if(data1[0]==0):
            msg="Dear PCare Customer,   User id:'"+str(bank_name)+"' Your pension:'"+str(amount)+"'for this '"+str(month)+"' is sanctioned. please collect from your bank account. if any queries occur pls contact:'"+str(uid)+"'"
            print(msg)
            sendsms(bank_name,msg)
            s = "insert into deposit(`aregister_id`,`bank_name`,`month`, `amount`) values('"+str(uid)+"','"+str(bank_name)+"','"+str(month)+"','"+str(amount)+"')"
            print (s)
            c.execute(s)
            con.commit()
            alert= "Successfully Submitted"
            
            return render(request,"deposit.html",{"msg":alert,"data2":data2,"data3":data3})
        else:
            alert="The pension is already alloted to user this month"
            return render(request,"deposit.html",{"msg":alert,"data2":data2,"data3":data3})
    return render(request,"deposit.html",{"data2":data2,"data3":data3})   
def adminhome(request):
    msg="admin logged in"
    return render (request,"adminhome.html",{"msg":msg}) 

def activities(request):
    b="SELECT userreg.name,pension.category from userreg join pension on userreg.phno=pension.register_id" 
    c.execute(b)
    data=c.fetchall()
    print(data)
    m= "select * from userreg"
    c.execute(m)
    data1=c.fetchall()
    print(data1)
    h="SELECT userreg.name,deposit.month,deposit.amount from userreg join deposit on userreg.phno=deposit.bank_name"
    c.execute(h)
    data2=c.fetchall()
    print(data2)
    return render(request,"activities.html",{"data":data,"data1":data1,"data2":data2})

def pensionplan(request):
    alert=""
    h="select * from  pensionplans"
    c.execute(h)
    data=c.fetchall()
    if request.POST.get("submit"):
        planname = request.POST.get("planname")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        c_count = "select count(*) from pensionplans where planname = '"+str(planname)+"' and description= '"+str(description)+"'"
        c.execute(c_count)
        con.commit()
        data1= c.fetchone()
        if data1[0] == 0:
            s = "insert into pensionplans(`planname`,`description`,`amount`) values('"+str(planname)+"','"+str(description)+"','"+str(amount)+"')"
            print (s)
            c.execute(s)
            con.commit()
            alert= "Successfully Added"
    return render(request,"pensionplan.html",{"msg":alert,"data":data})

def pension(request):
    h="select * from  pensionplans"
    c.execute(h)
    data=c.fetchall()
    return render(request,"pension.html",{"data":data})

def notify(request):
    uid=request.session["u_id"]
    h="select * from  deposit where bank_name='"+str(uid)+"'"
    c.execute(h)
    data=c.fetchall()
    h="select sum(amount) from  deposit where bank_name='"+str(uid)+"'"
    c.execute(h)
    data1=c.fetchone()
    return render(request,"notify.html",{"data":data,"data1":data1[0]})
def publicprofile(request):
    uid=request.session["u_id"]
    h="select * from  userreg where register_id='"+str(uid)+"'"
    c.execute(h)
    data=c.fetchall()
    
    return render(request,"publicprofile.html",{"data":data})
    