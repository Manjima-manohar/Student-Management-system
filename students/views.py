from django.shortcuts import render
from .models import Student
# Create your views here.

def index(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Address=request.POST.get("address")
        Photo=request.FILES.get("image")
        Student.objects.create(name=Name,address=Address,photo=Photo)
        return render(request,"index.html",{"msg":"registered"})
    return render(request,"index.html")