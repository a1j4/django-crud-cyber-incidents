from django.db import models
from django.contrib.auth.models import User
class Incident(models.Model):

    SEVERITY_CHOICES = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
        ('Critical','Critical')
    ]

    title=models.CharField(max_length=200)

    description=models.TextField()

    severity=models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES
    )

    reported_at=models.DateTimeField(
        auto_now_add=True
    )

    updated_at=models.DateTimeField(
        auto_now=True
    )

    resolved=models.BooleanField(
        default=False
    )

    reported_by=models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='incidents'
    )

    def __str__(self):
        return self.title