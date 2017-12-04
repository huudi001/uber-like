from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

url( r'^new/cabdriver/', views.new_cabdriver, name="newcabdriver"),

    url( r'^login/cabdriver/', views.cabdriver_login, name="cabdriverlogin"),

    url( r'^cabdriver/(\d+)', views.cabdriver, name="driver"),

    url( r'^update/cabdriver/profile/(\d+)', views.update_cabdriver_profile, name="updateCAbDriverProfile"),

    url( r'^new/rider', views.rider, name="newrider"),

    url( r'^rider/(\d+)', views.rider, name="rider"),

    url( r'^login/rider/', views.rider_login, name="riderlogin"),

    url( r'^update/rider/profile/(\d+)', views.updateriderprofile, name="updateRiderProfile"),

    url( r'^cabdrivers/(\d+)', views.cabdrivers, name="cabdrivers"),

    url( r'^profile/cabdriver/(\d+)/(\d+)', views.cabdriver_profile, name="cabdriverProfile"),

    url( r'^ajax/review-cabdriver/profile/cabdriver/(\d+)/(\d+)', views.review_cabdriver, name="reviewCabDriver"),

]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
