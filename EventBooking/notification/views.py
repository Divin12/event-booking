from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Notification

@login_required
def show_notifications(request):
    user_notifications = Notification.objects.filter(user=request.user)
    return render(request, 'notifications.html', {'user_notifications': user_notifications})


def mark_as_read(request, notification_id):
    notification = Notification.objects.get(pk=notification_id)
    notification.is_read = True
    notification.save()
    return redirect('show-notifications')
