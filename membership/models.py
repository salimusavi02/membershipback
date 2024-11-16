from django.db import models
from django.utils import timezone


class MembershipCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.code

    def is_active(self):
        today = timezone.now().date()

        # بررسی تاریخ شروع
        if not self.start_date:
            return False, "تاریخ شروع تنظیم نشده است"
        if self.start_date > today:
            return False, "هنوز فعال نشده است"

        # بررسی تاریخ پایان
        if self.end_date and self.end_date < today:
            return False, "منقضی شده است"

        # اگر همه شرایط رعایت شد، عضویت فعال است
        if self.start_date <= today :
            return True, "فعال است"
