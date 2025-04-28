from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import os
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    def image_upload_to(self, image):
        extension = image.split('.')[-1]
        unique_id = uuid.uuid4()
        filename = f"{unique_id}.{extension}"
        str_phone_number = str(self.phone_number)
        if image:
            return os.path.join('images/user_images',f"{str_phone_number}_{filename}")
        return None
    email=models.EmailField(max_length=150,unique=True)
    phone_number=PhoneNumberField(unique=True)
    user_image = models.ImageField(upload_to=image_upload_to,default="images/user_images/user.jpg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','first_name','last_name']

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"