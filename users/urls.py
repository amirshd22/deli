from django.urls import path
from . import views



urlpatterns =[
    path("login/", views.MyTokenObtainPairView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="Register"),
    path("get-all-students/<str:id>/",views.getStudent,name="Students")

]

