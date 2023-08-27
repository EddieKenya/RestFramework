from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(verbose_name=_("Profile Picture"), upload_to="profile_pictures/", blank=True, null=True)
    bio = models.TextField(verbose_name=_("Bio"), blank=True)
    date_of_birth = models.DateField(verbose_name=_("Date of Birth"), blank=True, null=True)
    location = models.CharField(verbose_name=_("Location"), max_length=100, blank=True)
    website = models.URLField(verbose_name=_("Website"), blank=True)
    
    # Add more fields as needed
    
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
    
    def __str__(self):
        return self.user.username
