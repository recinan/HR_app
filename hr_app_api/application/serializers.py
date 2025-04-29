from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    cvFilePath = serializers.FileField()
    class Meta:
        model = Application
        fields = ['jobTitle','cvFilePath','description']