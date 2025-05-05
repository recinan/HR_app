from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import os
import uuid
from django.utils.text import slugify

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.role_name

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
    created_at = models.DateTimeField(auto_now_add=True)
    user_role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','first_name','last_name']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not self.username:
            base_username = slugify(f"{self.first_name}{self.last_name}")
            username = base_username
            counter = 1
            while CustomUser.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            self.username = username
        super().save(*args, **kwargs)

