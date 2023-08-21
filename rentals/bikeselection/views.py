
from django.shortcuts import render
import cx_Oracle

def bikeselection(request):
    if request.method == "GET":
        vehicle_model = request.GET.get('vehicle_model', None)
        if vehicle_model:
            connStr = 'vishwas/vishwasgama@localhost:1521/xe'
            conn = cx_Oracle.connect(connStr)
            cur = conn.cursor()
            sq1 = "SELECT * FROM vehicle WHERE vehicle_model = '{}'".format(vehicle_model)
            print(sq1)
            cur.execute(sq1)
            rows = cur.fetchall()
            print(rows)
            if not rows:
                return render(request,'fail.html')         
            else:
                data1 = [{'vehicle_id': row[0], 'vehicle_brand': row[1], 'vehicle_model': row[2], 'vehicle_type': row[3], 'Vehicle_color': row[4], 'seating_capacity': row[5], 'Vehicle_price_per_Day': row[6], 'kms_driven': row[7], 'rent_location_id': row[8], 'image_path': row[9]} for row in rows]
                print(data1)
                
                return render(request, 'Search.html', {'data': data1})
    return render(request,'Brand_wise.html')
