from django.db import models
from users.models import CustomUser
import os, uuid
# Create your models here.

def cv_upload_to(instance,file):
    extension = file.split('.')[-1]
    unique_id = uuid.uuid4()
    filename = f"{unique_id}.{extension}"
    str_phone_number = str(instance.user.phone_number)
    if file:
        return os.path.join('cv_files/',f"cv_sample_{str_phone_number}_{filename}")
    return None

class Application(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=50)
    cvFilePath = models.FileField(upload_to=cv_upload_to)
    description = models.CharField(max_length=256, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.user.first_name} {self.user.last_name} - {self.jobTitle}"
    
