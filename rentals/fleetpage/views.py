from django.shortcuts import render
import cx_Oracle

# views.py


def fleetpage(request):
    if request.method=="GET":
        company = request.GET.get('company', None)
        if company:
            connStr = 'vishwas/vishwasgama@localhost:1521/xe'
            conn = cx_Oracle.connect(connStr)
            cur = conn.cursor()
            sq1 = "SELECT * FROM vehicle WHERE vehicle_brand = '{}'".format(company)
            print(sq1)
            cur.execute(sq1)
            
            rows = cur.fetchall()
            print(rows)
            if not rows:
                return render(request,'fail.html')         
            else:
                # Create a list of dictionaries, where each dictionary represents a row of data
                data = [{'vehicle_id': row[0], 'vehicle_brand': row[1], 'vehicle_model': row[2], 'vehicle_type': row[3], 'color': row[4], 'seating_capacity': row[5], 'Vehicle_price_per_Day': row[6], 'kms_driven': row[7], 'rent_location_id': row[8], 'image_path': row[9]} for row in rows]
                # Render the other template and pass the data as a context parameter
                return render(request, 'Brand_wise.html', {'data': data})
    return render(request,'fleet.html')



