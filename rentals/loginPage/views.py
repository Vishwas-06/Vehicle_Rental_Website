from django.shortcuts import render
import cx_Oracle
username=''
passwordd=''
# Create your views here.
def loginPage(request):
    global username,passwordd
    if request.method=="POST":
        connStr = 'vishwas/vishwasgama@localhost:1521/xe'
        #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
        conn = cx_Oracle.connect(connStr)
        cur = conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                username=value
            if key=="pass":
                passwordd=value
        sq1 = "SELECT * FROM CUSTOMERS WHERE Customer_Email='{}' AND customer_password='{}'".format(username,passwordd)
        print(sq1)
        cur.execute(sq1)
        a=tuple(cur.fetchall())      
        if a==():
            context = {
                'message': 'The username or password is incorrect.'
            }
            return render(request,'login.html',context)
        else:
            return render(request,"index_login.html")
    return render(request,'login.html')