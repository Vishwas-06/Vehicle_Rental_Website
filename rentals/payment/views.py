from django.shortcuts import render,redirect
from django.contrib import messages
import cx_Oracle

# Create your views here.
def payment(request):
  if request.method == 'POST':
    # Get the form data
    print(request.POST)
    email = request.POST['email']
    start_formatted = request.POST['start']
    end_formatted = request.POST['end']
    vehicle_id = request.POST['id']
    license_no = request.POST['license_no']
    ride=request.POST['ride']
    alno=request.POST['alno']
    user_name=request.POST['user_name']
    ph_no=request.POST['ph_no']
    amt=request.POST['amt']
    addr=request.POST['addr']
    state=request.POST['state']   
    zp_code=request.POST['zp_code']
    nameoncard=request.POST['nameoncard']
    card_no=request.POST['card_no']
    exp_month=request.POST['exp_month']
    exp_year=request.POST['exp_year']
    cvv=request.POST['cvv']
    reservation_id=request.POST['reservation_id']


    # Strip leading and trailing whitespace from the vehicle_id
    vehicle_id = vehicle_id.strip()

    # Concatenate the vehicle_id and email fields
    reservation_id = vehicle_id + email
    payment_id= reservation_id+cvv

    # Connect to the database
    connStr = 'vishwas/vishwasgama@localhost:1521/xe'
    conn = cx_Oracle.connect(connStr)
    cur = conn.cursor()

    # Use the form data in your SQL insert statement
    sq1 = "INSERT INTO availability(vehicle_id, booking_start_date, booking_end_date) VALUES ('{}', TO_DATE('{}', 'YYYY-MM-DD HH24:MI'), TO_DATE('{}', 'YYYY-MM-DD HH24:MI'))".format(vehicle_id, start_formatted, end_formatted)
    sq2 = "INSERT INTO reservation(res_id,customer_email,license_no,vehicle_id,type_of_ride, booking_start_date, booking_end_date,alternate_mobile_no) VALUES ('{}','{}','{}','{}','{}', TO_DATE('{}', 'YYYY-MM-DD HH24:MI'), TO_DATE('{}', 'YYYY-MM-DD HH24:MI'), '{}')".format(reservation_id,email,license_no,vehicle_id,ride, start_formatted, end_formatted,alno)
    sq3 = "INSERT INTO payment(customer_name,mobile_no,state_,city,zip_code,res_id, payment_id,card_no,name_on_card,expiry_month,expiry_year,cvv,amount_paid_through_card) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(user_name,ph_no,state,addr,zp_code,reservation_id,payment_id,card_no,nameoncard,exp_month,exp_year,cvv,amt)
    print(sq1)
    print(sq2)
    print(sq3)
    
 
    try:
        cur.execute(sq1)
        cur.execute(sq2)
        cur.execute(sq3)
        conn.commit()
        return redirect('http://127.0.0.1:8000/fleetpage/?show_popup=True&source=page3')
    except cx_Oracle.IntegrityError as e:
        error, =e.args
        return redirect('http://127.0.0.1:8000/fleetpage/?show_popup=True&source=page2')
  else:
        return render(request,'payment.html')