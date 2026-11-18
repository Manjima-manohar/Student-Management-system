from django.shortcuts import render,redirect

# from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm

from django.contrib.auth import authenticate, login

# Create your views here.

def register_view(request):
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Successfully")
            return render(request,'index.html')
    return render(request,'register.html',{'form':form})





# def user_login(request):
#     print("hello")
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(
#             request,
#             username=username,
#             password=password
#         )

#         if user is not None:
#             login(request, user)
#             return redirect("index")

#     return render(request, "login.html")


# def home(request):
#     # print(request.COOKIES)
#     v=int(request.COOKIES.get('visits',0))
#     v=v+1
#     response= render(request,"cookies.html",{'visits':v})
#     response.set_cookie('visits',v)
    # return response
    # return render(request,"cookies.html")


def home(request):
    c=int(request.session.get('count',0))
    c=c+1
    request.session['count']=c
    return render(request,"cookies.html",{'visits':c})
    








