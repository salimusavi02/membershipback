from django.contrib import admin
from .models import MembershipCode

@admin.register(MembershipCode)
class MembershipCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'start_date', 'end_date', 'is_active')
    search_fields = ('code',)