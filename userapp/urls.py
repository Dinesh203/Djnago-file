from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('Signup', views.signup, name="SignUp"),
    path("login", views.login, name="login"),
    path('getuser', views.getuser, name="getuser"),
    # path('update', views.update, name="updateprofile"),


]
