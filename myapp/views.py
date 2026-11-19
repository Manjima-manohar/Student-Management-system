from django.shortcuts import render,HttpResponse,redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Index(request):
    #return HttpResponse("welcome")
    n="manjima"
    age=10
    return render(request,"index.html",{"name":n,"age":age})

# @login_required(login_url="/login")
def about(request):
	form=EmployeeForm() #constructor
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("display")
	return render(request,"about.html",{"form":form})


def contact(request):
    return HttpResponse("<h1>contact page</h1>")

def Add_data(request):
    Name=request.POST["username"]
    Address=request.POST["address"]
    emplist=Employee.objects.create(name=Name,address=Address)
    emplist.save()
    return render(request,"about.html",{"msg":"Registration completed"})


def display(request):
	empdtls=Employee.objects.all()
	return render(request,"contact.html",{'emp':empdtls})

# select * from myapp_employee where name="manjima"


def update_employee(request,eid):

	emp=Employee.objects.get(id=eid)

	if request.method == "POST":
		emp.name = request.POST["name"]
		emp.address = request.POST["address"]
		emp.save()
		return redirect("display") 

	return render(request,"update.html",{"emp":emp})


def delete_employee(request, eid):
    emp = Employee.objects.get(id=eid)
    emp.delete()
    return redirect("display")



#update using filter
def updatename(request):
	try:
		Oldname=request.POST["oldname"]
		Newname=request.POST["newname"]
		emp=Employee.objects.filter(name=Oldname)#.update(name=Newname)
		if emp.exists():
			emp.update(name=Newname)
			return render(request,"about.html",{'msg2':"Updated"})
		else:
			return render(request,"about.html",{'msg2':"no records found"})
	except Exception as e:
			print(e)
			return render(request,"about.html",{'msg2':"no updated"})
	

'''
#Upadte using get
oldname=request.POST["oldname"]
newname=request.POST["newname"]
emp=Employee.objects.get(name=oldname)
emp.name=newname
emp.save()
return render(request,"index.html",{'msg1':"Updated"})
'''



# crud-create
# read





# '{"email":"manjima@gmail.com","password":7556}'

# Data=>JSON serialization

# JSON=Data deserialization