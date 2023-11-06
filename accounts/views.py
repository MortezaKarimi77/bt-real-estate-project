from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from listings.models import Listing


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == '' or password == '':
            messages.error(request, 'نام کاربری و رمز عبور نباید خالی باشد')
            return redirect('login')

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'شما با موفقیت وارد حساب خود شدید')
            return redirect('dashboard')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')

    context = {
        'login_active': 'active',
        'title': 'ورود به حساب',
    }

    return render(request, 'accounts/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


def signup(request):
    errors_count = 0
    context = {
        'signup_active': 'active',
        'title': 'ثبت نام',
    }

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if first_name == '':
            messages.error(request, 'نام نباید خالی باشد')
            errors_count += 1
        else:
            context['first_name'] = first_name

        if last_name == '':
            messages.error(request, 'نام خانوادگی نباید خالی باشد')
            errors_count += 1
        else:
            context['last_name'] = last_name

        if username == '':
            messages.error(request, 'نام کاربری نباید خالی باشد')
            errors_count += 1
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلا استفاده شده است')
            errors_count += 1
        else:
            context['username'] = username

        if password == '' or password2 == '':
            messages.error(request, 'رمز عبور و تکرار آن نباید خالی باشند')
            errors_count += 1

        if password != password2:
            messages.error(request, 'رمز عبور و تکرار آن برابر نمی‌باشند')
            errors_count += 1

        if len(password) < 8:
            messages.error(request, 'رمز عبور نباید کمتر از ۸ کاراکتر باشد')
            errors_count += 1

        try:
            validate_email(email)
            if User.objects.filter(email=email).exists():
                messages.error(
                    request, 'این پست الکترونیکی قبلا استفاده شده است'
                )
                errors_count += 1
            else:
                context['email'] = email
        except:
            messages.error(request, 'پست الکترونیکی نامعتبر است')
            errors_count += 1

        if errors_count == 0:
            User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username,
                email=email, password=password
            )
            messages.success(request, 'حساب شما با موفقیت ایجاد شد')
            return redirect('login')

    return render(request, 'accounts/signup.html', context)


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    user_contacts = Contact.objects.filter(
        user_id=user.id
    ).order_by('-contact_date')

    context = {
        'dashboard_active': 'active',
        'title': 'داشبورد',
        'welcome_message': f'خوش آمدید {user.first_name} {user.last_name}',
        'message': 'در حال حاضر چیزی برای نمایش وجود ندارد',
        'contacts': user_contacts,
    }

    return render(request, 'accounts/dashboard.html', context)
