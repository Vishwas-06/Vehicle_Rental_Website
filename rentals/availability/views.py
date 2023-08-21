from django.shortcuts import render, redirect
import cx_Oracle

# Create your views here.
def availability(request):
  if request.method == 'POST':
    # Split the start and end date values at the "T" character
    start_parts = request.POST['start'].split('T')
    end_parts = request.POST['end'].split('T')
    vehicle_id = request.POST['id']
    vehicle_id = vehicle_id.strip()

    # Join the parts back together with a space character
    start_formatted = start_parts[0] + ' ' + start_parts[1]
    end_formatted = end_parts[0] + ' ' + end_parts[1]

    # Connect to the database
    connStr = 'vishwas/vishwasgama@localhost:1521/xe'
    conn = cx_Oracle.connect(connStr)
    cur1 = conn.cursor()
    cur2 = conn.cursor()

    # Use the formatted values in your SQL query
    sq2 = "SELECT * FROM availability WHERE vehicle_id = '{}' AND ((TO_DATE('{}', 'YYYY-MM-DD HH24:MI') < booking_start_date AND TO_DATE('{}', 'YYYY-MM-DD HH24:MI') < booking_start_date) OR (TO_DATE('{}', 'YYYY-MM-DD HH24:MI') > booking_end_date AND TO_DATE('{}', 'YYYY-MM-DD HH24:MI') > booking_end_date))".format(vehicle_id, start_formatted, end_formatted, start_formatted, end_formatted)
    sq3 = "SELECT * FROM availability WHERE vehicle_id = '{}'".format(vehicle_id)
    cur1.execute(sq2)
    cur2.execute(sq3)
    b = tuple(cur1.fetchall())
    c = tuple(cur2.fetchall())
    if b == c :
      context = {'vehicle_id': vehicle_id, 'start_formatted': start_formatted, 'end_formatted': end_formatted}
      return render(request, 'reservation.html',context)
    else:
      return redirect('http://127.0.0.1:8000/fleetpage/?show_popup=True&source=page1')
  return render(request, 'search.html')

