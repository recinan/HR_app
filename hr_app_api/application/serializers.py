from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    jobTitle = serializers.CharField(max_length=50)
    cvFilePath = serializers.FileField(required=True)
    description = serializers.CharField(max_length=256, allow_blank=True)
    user_email = serializers.SerializerMethodField()
    class Meta:
        model = Application
        fields = ['id','user_email','jobTitle','cvFilePath','description','applied_at']

    def get_user_email(self, obj):
        return f"{obj.user.email}"


