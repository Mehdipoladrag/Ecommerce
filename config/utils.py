from kavenegar import *
import ghasedakpack


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





# try:
    #     api = KavenegarAPI('API KEY')
    #     params = {
    #         'sender': '',  # optional, specify if needed
    #         'receptor': phone_number,
    #         'message': f'کد تایید شما: {code}',
    #     }
    #     response = api.sms_send(params)
    #     print(response)
    # except APIException as e:
    #     print(f"Kavenegar API Exception: {e}")
    # except HTTPException as e:
    #     print(f"HTTP Exception: {e}")
