from apps.profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def profile_users_created(sender, instance, created, **kwargs):
    if created:
        profile =Profile.objects.create(user=instance)
        
