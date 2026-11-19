from django.urls import path
from . import views


urlpatterns = [
    path("",views.Index,name="index"),
    path("aboutpage",views.about,name="aboutt"),
    path("contact",views.contact,name="contact"),

    path("addpage",views.Add_data,name="add"),

    path("display",views.display,name="display"),
    
    path("updateid/<int:eid>",views.update_employee,name="update_employee"),

    path("deleteid/<int:eid>", views.delete_employee, name="delete_employee"),

    path("update",views.updatename,name="update"),

    

]