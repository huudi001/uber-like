from django import forms
from .models import CabDriver, CabDriverProfile, Rider, RiderProfile, DriverReview

class NewCabDriver(forms.ModelForm):

    class Meta:
        model = CabDriver
        fields = ('first_name', 'last_name', 'phone_number')
class UpdateCabProfile(forms.ModelForm):

    class Meta:
        model = CabDriverProfile
        fields =  'profile_pic', 'car_image', 'car_capacity', 'car_number_plate', 'car_color')
