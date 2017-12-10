from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django import template

register = template.Library()



User = get_user_model()


class Journey(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pool_members')
    starting_from = models.CharField(max_length=255)
    starting_from_longitude = models.FloatField(null=True)
    starting_from_latitude = models.FloatField(null=True)
    going_to = models.CharField(max_length=255)
    going_to_longitude = models.FloatField(null=True)
    going_to_latitude = models.FloatField(null=True)
    description = models.TextField(blank=True, default='')
    # members = models.ManyToManyField(User, through="JourneyMember")
    members = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now=True)
    going_date = models.DateField()
    going_time = models.TimeField()

    def __str__(self):
        return self.created_by.username + "_" + self.starting_from + "-" + self.going_to

    def get_absolute_url(self):
        return reverse("journeys:single")

    @classmethod
    def add_member(cls, journey, current_user):
        journey.members.add(current_user)

    @classmethod
    def remove_member(cls, journey, current_user):
        journey.members.remove(current_user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
