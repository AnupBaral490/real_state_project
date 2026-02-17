from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('agent', 'Agent'),
        ('buyer', 'Buyer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True, help_text="Upload your profile photo")

    def __str__(self):
        return self.username
    
    def get_role_display_custom(self):
        return dict(self.ROLE_CHOICES).get(self.role, self.role)

    
