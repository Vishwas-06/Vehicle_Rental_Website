from django.shortcuts import render
import cx_Oracle
# Create your views here.
fullname=''
User_email=''
phone_no =''
subject =''
message=''



def contactpage(request):
  global fullname,User_email,phone_no,subject,message
  if request.method=="POST":
    connStr = 'vishwas/vishwasgama@localhost:1521/xe'
    conn = cx_Oracle.connect(connStr)
    cur = conn.cursor()
    d=request.POST
      #m.close()
    for key,value in d.items():
        if key=="NAME":
                fullname=value
        if key=="email":
                User_email=value
        if key=="phno":
                phone_no=value
        if key=="subject":
                subject=value
        if key=="message":
            message=value
    sqltxt="insert into COMPLAINT values('{}','{}','{}','{}','{}')".format(fullname,User_email,phone_no,subject,message)
    rows_affected = cur.execute(sqltxt)
    conn.commit()
    if rows_affected == 0:
        message = "Try Again"
    else:
        message = "Data entered Successfully"
    return render(request,'Contact.html',{'message': message})
  
  return render(request,'Contact.html')