from django.db import models
from auth.models import UserProfile

# Create your models here.


class WorkoutVideo(models.Model):
    CATEGORY_CHOICES = [
        ('WL', 'Weight Loss'),
        ('MG', 'Muscle Gain'),
        ('CB', 'Cardio'),
        ('FL', 'Flexibility')
    ]
    INTENSITY_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    intensity = models.CharField(max_length=1, choices=INTENSITY_CHOICES)
    duration = models.DurationField()  # Stored as timedelta
    video_file = models.URLField()  # Stored in cloud storage
    is_premium = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    uploader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
