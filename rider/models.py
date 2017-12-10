from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
DEFAULTVEHICLE = "vehicle-image/vehicle-default.png"
DEFAULTDRIVERPROFILEPIC = "driver/profile-pic/user-icon.png"
DEFAULTRIDERPROFILEPIC = "rider/profile-pic/user-icon.png"
class CabDriver(models.Model):

    first_name = models.CharField(max_length=180)

    last_name = models.CharField(max_length=180)

    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name  + ' ' + self.last_name

    @classmethod
    def get_all_commuters(cls):
        commuters = CabDriver.objects.all()

        return commuters

class CabDriverProfile(models.Model):
    driver = models.OneToOneField(CabDriver, on_delete=models.CASCADE)

    profile_pic = models.ImageField(blank=True,upload_to="driver/profile-pic", default=DEFAULTDRIVERPROFILEPIC)

    car_image = models.ImageField(blank=True,upload_to="vehicle-image/", default=DEFAULTVEHICLE)

    car_capacity = models.PositiveIntegerField(default=0, blank=True)

    car_number_plate = models.CharField(blank=True, max_length=60, validators=[alphanumeric])

    car_color = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.driver.first_name + ' ' + self.driver.last_name
    @classmethod
    def get_cab_profiles(cls):
        driver_profiles = CabDriverProfile.objects.all()
        return driver_profile

   receiver(post_save, sender=CabDriver)
   def create_cabprofile(sender, instance, created, **kwargs):
       if created:
           CabDriverProfile.objects.create(driver=instance)



   @receiver(post_save, sender=CabDriver)
   def save_cabprofile(sender, instance, **kwargs):
       instance.driverprofile.save()


class Rider(models.Model):
    first_name = models.CharField(max_length=180)

    last_name = models.CharField(max_length=180)

    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name  + ' ' + self.last_name

    @classmethod
    def get_riders(cls):
        riders = Rider.objects.all()

        return riders

class RiderProfile(models.Model):
    rider = models.OneToOneField(Rider, on_delete=models.CASCADE)

    profile_pic = models.ImageField(blank=True, upload_to="passenger/profile-pic", default=DEFAULTPASSANGERPROFILEPIC)
    general_location = models.CharField(blank=True,max_length=255)

    def __str__(self):
        return self.rider.first_name + ' ' + self.rider.last_name

    @classmethod
    def get_rider_profiles(cls):
        rider_profiles = RiderProfile.objects.all()

        return rider_profiles

    @receiver(post_save, sender=Rider)
def create_rider_profile(sender, instance, created, **kwargs):
    if created:
        RiderProfile.objects.create(rider=instance)

@receiver(post_save, sender=Rider)
def save_riderprofile(sender, instance, **kwargs):
    instance.Riderprofile.save()


class DriverReview(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)

    driver_profile = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)

    review = models.TextField()

    def __str__(self):
        return self.rider.first_name + ' ' + self.rider.last_name

    @classmethod
    def get_driver_reviews(self,driver_profile_id):
        driver_reviews = DriverReview.objects.filter(driver_profile=driver_profile_id)

        return driver_reviews


class RiderReview(models.Model):

    driver = models.ForeignKey(CabDriver, on_delete=models.CASCADE)

    rider_profile = models.ForeignKey(RiderProfile, on_delete=models.CASCADE)

    review = models.TextField()

    def __str__(self):
        return self.driver.first_name + ' ' + self.driver.last_name

    @classmethod
    def get_rider_reviews(self,passenger_profile_id):

        rider_reviews = RiderReview.objects.filter(rider_profile=rider_profile_id)

        return rider_reviews
