from django.shortcuts import render,redirect
import cx_Oracle

# Create your views here.
def reservation(request):
  if request.method == 'POST':
    # Get the form data
    email = request.POST['email']
    start_formatted = request.POST['start']
    end_formatted = request.POST['end']
    vehicle_id = request.POST['id']
    license_no = request.POST['license_no']
    ride=request.POST['ride']
    alno=request.POST['alno']
    

    # Strip leading and trailing whitespace from the vehicle_id
    vehicle_id = vehicle_id.strip()

    # Concatenate the vehicle_id and email fields
    reservation_id = vehicle_id + email

    # Connect to the database
    connStr = 'vishwas/vishwasgama@localhost:1521/xe'
    conn = cx_Oracle.connect(connStr)
    context = {'vehicle_id': vehicle_id, 'start_formatted': start_formatted, 'end_formatted': end_formatted,'email':email,'license_no':license_no,'ride':ride,'alno':alno,'reservation_id':reservation_id}
    return render(request, 'payment.html', context)
  else:
    return redirect('http://127.0.0.1:8000/fleetpage/?show_popup=True&source=page2')
