from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from auth.models import UserProfile

# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    PLAN_TYPES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ]
    plan_type = models.CharField(max_length=10, choices=PLAN_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True)

class Purchase(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    purchase_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    transaction_id = models.CharField(max_length=255)