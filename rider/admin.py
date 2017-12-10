from django.contrib import admin
from .models import CabDriver, CabDriverProfile, Rider, RiderProfile, DriverReview, RiderReview


admin.site.register(CabDriver)
admin.site.register(DriverProfile)
admin.site.register(Rider)
admin.site.register(RiderProfile)
admin.site.register(DriverReview)
admin.site.register(RiderReview)
