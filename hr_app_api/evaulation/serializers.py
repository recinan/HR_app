from rest_framework import serializers
from .models import Evaulation
from application.serializers import ApplicationSerializer

class EvaulationSerializer(serializers.ModelSerializer):
    evaulator_name = serializers.SerializerMethodField()
    applicant_name = serializers.SerializerMethodField()
    application_detail = ApplicationSerializer(source='application', read_only=True)
    class Meta:
        model = Evaulation
        fields = ['id','application','application_detail','score','evaulation_description','evaulated_at','applicant_name', 'evaulator_name']

    def get_evaulator_name(self, obj):
        return f"{obj.user_evaulator.first_name} {obj.user_evaulator.last_name}"
    
    def get_applicant_name(self, obj):
        return f"{obj.application.user.first_name} {obj.application.user.last_name}"

class EvaulationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaulation
        fields = ['application','score','evaulation_description']

    def create(self, validated_data):
        validated_data['user_evaulator'] = self.context['request'].user
        return super().create(validated_data)