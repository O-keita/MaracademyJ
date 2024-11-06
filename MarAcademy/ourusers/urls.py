from django.urls import path
from .views import home, login_view, register, dashboard, logout_view


urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("", login_view, name="logout"),
    
]


