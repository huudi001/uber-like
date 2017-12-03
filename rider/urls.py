from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url( r'^$', views.index, name="index"),
     url( r'^new/driver/', views.new_driver, name="newdriver"),

    url( r'^login/driver/', views.driver_login, name="driverlogin"),
