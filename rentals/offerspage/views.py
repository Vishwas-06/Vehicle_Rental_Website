from django.shortcuts import render

# Create your views here.
def offerspage(request):
    return render(request,'Offers.html')