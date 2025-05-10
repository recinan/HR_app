from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from evaulation.models import Evaulation
from users.models import Role
import os
from dotenv import load_dotenv
from hr_app import settings

@receiver(post_save, sender=Evaulation)
def send_email_to_canditate(sender, instance, **kwargs):
    application = instance.application
    sum_of_evaluators = Role.objects.filter(role_name='Evaluator').count()
    sum_of_evaluations = Evaulation.objects.filter(application=application).count()
    user_email = application.user.email
    print("Bura calisma olayi")

    if sum_of_evaluations >= sum_of_evaluators:
        user_email = application.user.email
        print("Bura calisma olayi")
        print(user_email)
        send_mail(
            subject="Your evaluation process has been completed!",
            message="You can view your evaluation on your board",
            from_email= settings.EMAIL_FROM,
            recipient_list=[user_email],
            fail_silently=False
        )


