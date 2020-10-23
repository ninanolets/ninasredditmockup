from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.core.mail import send_mail

from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        contact_date = timezone.datetime.now()


        # Check if user has sent > 3 messages
        has_contacted = Contact.objects.all().filter(email=email, contact_date=contact_date).count()
        if has_contacted >= 3:
            messages.error(request, mark_safe('You already contacted us 3 times today. <br/>Relax, we\'ll get back to you SOON.'))
            return redirect('index')


        contact = Contact(name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # # send email after form is saved
        # send_mail(
        #     'A user just made contact!',
        #     'User ' + name + ' (' +  email + ') wants to talk to the team. Sign in to the Admin Panel for more info.',
        #     'marinaa.noleto@gmail.com',
        #     ['test@gmail.com', 'test@gmail.com'], # list of other emails to send the message
        #     fail_silently=False
        # )

        messages.success(request, mark_safe('Your message was successifully sent.<br/> Nina\'s Reddit Team will get back to you soon.'))

        return redirect('index')
    return render(request, 'contacts/contact.html')