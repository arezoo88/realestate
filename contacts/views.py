from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contact
from listings.models import Listing
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = Listing.objects.get(id=listing_id)

        if request.user.is_authenticated:
            send = Contact.objects.filter(listing=listing, user_id=request.user.id)
            if send.exists():
                return JsonResponse({'code': 101, 'error': 'You have already made an inquiry for this listing.'})
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if name.strip() == '':
            return JsonResponse({'code': 101, 'error': 'name can not be empty.'})
        if email == '':
            return JsonResponse({'code': 101, 'error': 'email can not be empty.'})

        if phone == '':
            return JsonResponse({'code': 101, 'error': 'phone can not be empty.'})

        if message == '':
            return JsonResponse({'code': 101, 'error': 'message can not be empty.'})

        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        contact = Contact(user_id=user_id, message=message, phone=phone, email=email, name=name, listing=listing)
        contact.save()
        send_mail(
            'Property listing inquiry',
            'There has been inquiry for ' + listing.title,
            'kmg.d145@gmail.com',
            [realtor_email, 'arezoo.darvish6969@gmail.com'],
            fail_silently=False,
        )

        return JsonResponse({'code': 100, 'url': '/listings/' + listing_id})
