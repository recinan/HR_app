from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from .models import Role

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    phone_number = PhoneNumberField(region='TR')
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2= serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','phone_number','password','password2')
        extra_kwargs = {
            'first_name':{'required':True},
            'last_name':{'required':True}
        }

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password':'Password fields didn't match"})
        return attrs
        
    def create(self, validated_data):
        default_role, _ = Role.objects.get_or_create(role_name='Candidate')

        user = CustomUser.objects.create(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_role=default_role
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token