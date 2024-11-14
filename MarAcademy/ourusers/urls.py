from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, login_view, register, dashboard, logout_view


urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout", logout_view, name="logout"),
    
]


