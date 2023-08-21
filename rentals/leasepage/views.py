from django.shortcuts import render
import cx_Oracle
# Create your views here.
fullname=''
User_email=''
phone_no =''
Aadhar =''
Vehrgid=''
vehtype =''
vehmodel=''
kms_driven =''


def leasepage(request):
  global fullname,User_email,phone_no,Aadhar,Vehrgid,vehtype,vehmodel,kms_driven
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
        if key=="contact":
                phone_no=value
        if key=="adrno":
                Aadhar=value
        if key=="rgno":
            Vehrgid=value
        if key=="vehtype":
                vehtype=value
        if key=="kms":
                kms_driven=value
        if key=="vehmodel":
                vehmodel=value
        
    sqltxt="insert into Lease_your_vehicle values('{}','{}','{}','{}','{}','{}','{}','{}')".format(fullname,User_email,phone_no,Aadhar,Vehrgid,vehtype,kms_driven,vehmodel)
    try:
        cur.execute(sqltxt)
        conn.commit()
        context1={

                'message1': 'Details Registered Sucessfully our executive will contact you shortly '
            }
        return render(request,'Lease.html',context1)
    except cx_Oracle.IntegrityError as e:
        error, =e.args
        context2 = {
                'message2': 'Vehicle with same regid present'
        }
        return render(request,'Lease.html',context2)
  else:
        return render(request,'Lease.html')