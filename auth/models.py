from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
    

class UserProfile(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)   
    date_of_birth = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    FITNESS_GOAL_CHOICES = [
        ('WL', 'Weight Loss'), 
        ('MG', 'Muscle Gain'), 
        ('MM', 'Maintain'), 
        ('OT', 'Other')
    ]
    fitness_goal = models.CharField(max_length=2, choices=FITNESS_GOAL_CHOICES, blank=True)
    provider = models.CharField(max_length=50, blank=True)  # Authentication provider
    health_data_consent = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email

class HealthData(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    weight = models.FloatField()  # in kg
    height = models.FloatField()  # in cm
    activity_level = models.CharField(max_length=50)
    sleep_hours = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    SOURCE_CHOICES = [
        ('manual', 'Manual'),
        ('google_fit', 'Google Fit'),
        ('apple_health', 'Apple Health')
    ]
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='manual')



class UserActivityLog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict)
    
    
class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    NOTIFICATION_TYPES = [
        ('meal_plan', 'Meal Plan Update'),
        ('new_video', 'New Video Content'),
        ('progress', 'Progress Check-in')
    ]
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)