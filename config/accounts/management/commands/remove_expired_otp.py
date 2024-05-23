from django .core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime, timedelta
class Command(BaseCommand):
    help = 'remove all expired otp code'
    def handle(self, *args, **options):
        expired_time = datetime.now() - timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expired_time).delete()
        self.stdout.write(self.style.SUCCESS('all expired otp Removed'))