from django.shortcuts import render, redirect
from django.views import View
from accounts.models import OtpCode, User
from accounts.forms import UserRegistrationForm, VerifyCodeForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
import random
from utils import send_otp_code
from django.contrib import messages


# Create your views here.

# UserRegisterView
class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            # We Save Data in Sessions Because We Want to Redirect A user to Verify
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password']
            }
            messages.success(request, 'we send you a code', 'success')
            return redirect('accounts:verify_code')
        return render(request, self.template_name, {'form': form})


# UserRegisterVerifyCode
class UserRegisterVerifyCode(View):
    form_class = VerifyCodeForm
    template_name = 'accounts/verify.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'], user_session['full_name'],
                                         user_session['password'])
                code_instance.delete()
                messages.success(request, 'you registred', 'success')
                return redirect('home:home')

            else:
                messages.error(request, 'this code is wrong', 'danger')
                return redirect('accounts:verify_code')
        return redirect('home:home')


# UserLoginView
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = "accounts/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login Successfully' 'success')
                return redirect('home:home')
            messages.error(request, 'phone or password is wrong', 'danger')
        return render(request, self.template_name, {'form': form})


# UserLogOutView
class UserLogOutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logout', 'success')
        return redirect('home:home')
