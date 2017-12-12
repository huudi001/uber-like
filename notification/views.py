from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views import generic
from journeys.models import Journey
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required()
def delete_notification(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.viewed = True
    notification.save()
    return HttpResponseRedirect(reverse("notification:all"))


class SingleNotification(LoginRequiredMixin, generic.DetailView):
    model = Notification


class ListNotifications(LoginRequiredMixin, generic.ListView):
    model = Notification
