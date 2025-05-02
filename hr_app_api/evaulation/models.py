from django.db import models
from users.models import CustomUser
from application.models import Application

# Create your models here.

class Evaulation(models.Model):
    user_evaulator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=3, decimal_places=2)
    evaulation_description = models.TextField(blank=True)
    evaulated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('application', 'user_evaulator')

    def __str__(self):
        return f"Evaulated by {self.user_evaulator.first_name} {self.user_evaulator.last_name} for {self.application.user.get_full_name()}"