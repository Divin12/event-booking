from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .forms import ComposeMessageForm

@login_required
def compose_message(request):
    if request.method == 'POST':
        form = ComposeMessageForm(request.POST)
        if form.is_valid():
            receiver_username = form.cleaned_data['receiver']
            receiver = User.objects.get(username=receiver_username)
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            message = Message(sender=request.user, receiver=receiver, subject=subject, message=message)
            message.save()

            return redirect('messaging:inbox')
    else:
        form = ComposeMessageForm()

    return render(request, 'compose_message.html', {'form': form})

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'messaging/inbox.html', {'received_messages': received_messages})

@login_required
def view_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    return render(request, 'messaging/message_detail.html', {'message': message})
