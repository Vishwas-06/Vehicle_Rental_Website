from django.shortcuts import render
import cx_Oracle
# Create your views here.
fullname=''
Aadhar =''
User_email=''
phone_no =''
pass_word =''
gender=''


def registrationpage(request):
  global fullname,Aadhar,User_email,phone_no,pass_word,gender
  if request.method=="POST":
    connStr = 'vishwas/vishwasgama@localhost:1521/xe'
    conn = cx_Oracle.connect(connStr)
    cur = conn.cursor()
    d=request.POST
      #m.close()
    for key,value in d.items():
        if key=="NAME":
                fullname=value
        if key=="adrno":
                Aadhar=value
        if key=="email":
                User_email=value
        if key=="contact":
                phone_no=value
        if key=="pass":
            pass_word=value
        if key=="gender":
                gender=value
    sqltxt="insert into customers values('{}','{}','{}','{}','{}','{}')".format(fullname,Aadhar,User_email,phone_no,pass_word,gender)
    try:
        cur.execute(sqltxt)
        conn.commit()
        context1={

                'message1': 'User Registered Sucessfully '
            }
        return render(request,'login.html',context1)
    except cx_Oracle.IntegrityError as e:
        error, =e.args
        context2 = {
                'message2': 'User with this email id is already present'
        }
        return render(request,'registration.html',context2)
  else:
        return render(request,'registration.html')

  