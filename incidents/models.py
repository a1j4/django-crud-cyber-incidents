from django.db import models

# Create your models here.
class Incident(models.Model):

    SEVERITY_CHOICES = [

        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
        ('Critical','Critical')

    ]

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES
    )

    reported_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    resolved = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title