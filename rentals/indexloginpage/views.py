from django.shortcuts import render

# Create your views here.
def indexloginpage(request):
    return render(request,'index_login.html')