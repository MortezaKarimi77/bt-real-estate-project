from django.shortcuts import redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    print(request.POST)
    if request.method == 'POST':
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        listing_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        return_url = request.POST['return_url']

        if request.user.is_authenticated and \
                Contact.objects.filter(listing_id=listing_id, user_id=request.user.id).exists():
            messages.error(
                request, 'شما قبلا برای این آگهی درخواست داده‌اید!!! لطفا منتظر پاسخ بمانید.'
            )
            return redirect(return_url)

        Contact.objects.create(
            name=name, email=email, phone=phone, message=message,
            listing=listing, listing_id=listing_id, user_id=user_id
        )

        # Sendin Email
        # send_mail(
        #     subject=f'درخواست تماس برای آگهی {listing}',
        #     message=f'مشاور املاک عزیز، شما برای آگهی {listing} درخواست تماس داشته‌اید. برای اطلاعات بیشتر وارد پنل کاربری خود شوید.',
        #     from_email='info@bugnameh.ir', recipient_list=[realtor_email, 'mortezakarimi77m3@gmail.com'],
        # )

        messages.success(
            request, 'درخواست شما با موفقیت ارسال شد. لطفا منتظر پاسخ بمانید.'
        )
        return redirect(return_url)
