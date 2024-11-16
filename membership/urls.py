from django.urls import path
from . import views
from .views import CheckMembershipCodeView, check_code_view

urlpatterns = [
    path('active-codes/', views.active_codes, name='active_codes'),
    path('check-code/', CheckMembershipCodeView.as_view(), name='check_membership_code'),
    path('check-code-ui/', check_code_view, name='check_code_ui'),
]