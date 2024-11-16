
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MembershipCode
from .serializers import MembershipCodeSerializer


def active_codes(request):
    active_codes = MembershipCode.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
    return render(request, 'membership/active_codes.html', {'active_codes': active_codes})

def check_code_view(request):
    return render(request, 'membership/check_code.html')

# active_memberships = Membership.objects.filter(start_date__lte=today, end_date__gte=today)

class CheckMembershipCodeView(APIView):
    def post(self, request, *args, **kwargs):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'Code is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            membership_code = MembershipCode.objects.get(code=code)
        except MembershipCode.DoesNotExist:
            return Response({"code": code,"is_active":[False,"not defined"]})

        serializer = MembershipCodeSerializer(membership_code)
        return Response(serializer.data, status=status.HTTP_200_OK)