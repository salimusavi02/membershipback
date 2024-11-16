from rest_framework import serializers
from .models import MembershipCode

class MembershipCodeSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = MembershipCode
        fields = ['code', 'is_active']

    def get_is_active(self, obj):
        return obj.is_active()