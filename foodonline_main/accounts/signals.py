from django.dispatch import receiver
from .models import User, UserProfile
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            instance.userprofile.save()
        except:
            UserProfile.objects.create(user=instance)
