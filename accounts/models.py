from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    ROLE_CHOICES = [
        ('analyst', 'Analyst'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='analyst'
    )

    bio = models.TextField(blank=True)

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user.username} ({self.role})'

    # 🔐 PERMISOS DEL LAB
    def is_admin(self):
        return self.role == 'admin'

    def is_analyst(self):
        return self.role == 'analyst'

    ROLE_CHOICES = [
        ('analyst', 'Analyst'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='analyst'
    )

    bio = models.TextField(blank=True)

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user.username} ({self.role})'
    
    def is_admin(self):
        return self.role == 'admin'
    
    def is_analyst(self):
        return self.role == 'analyst'