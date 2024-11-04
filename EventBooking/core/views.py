from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact details to the database
            messages.success(request, 'Your message has been submitted successfully! We will get in touch soon.')
            return redirect('core:contact_us')  # Redirect back to the contact form page or any desired page
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

