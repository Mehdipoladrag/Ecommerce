from kavenegar import *
import ghasedakpack
from django.contrib.auth.mixins import UserPassesTestMixin

def send_otp_code(phone_number, code):
    api_key = "API KEY"
    sms = ghasedakpack.Ghasedak(api_key)
    sms.send({'message': 'hello world!', 'receptor': '09xxxxxxxxx', 'linenumber': '3000xxxxx'})
    try:

        response = sms.verification({
            'receptor': phone_number,
            'type': '1',
            'template': 'Your Template',
            'param1': f'{code} کد تایید'
        })


        print("وضعیت ارسال پیام:", response)

    except Exception as e:
        print("خطا در ارسال پیام:", e)





class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
