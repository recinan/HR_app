from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    jobTitle = serializers.CharField(max_length=50)
    cvFilePath = serializers.FileField(required=True)
    description = serializers.CharField(max_length=256, allow_blank=True)
    class Meta:
        model = Application
        fields = ['id','jobTitle','cvFilePath','description','applied_at']