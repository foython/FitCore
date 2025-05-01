from django.db import models
from auth.models import UserProfile
# Create your models here.


class MealPlanTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    total_calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField(help_text="Grams per day")
    carbs = models.PositiveIntegerField(help_text="Grams per day")
    fat = models.PositiveIntegerField(help_text="Grams per day")
    recipes = models.JSONField()  # Structured recipe data
    is_premium = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class GeneratedMealPlan(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    meals = models.JSONField()  # Detailed meal structure
    is_customized = models.BooleanField(default=False)
    generation_source = models.CharField(
        max_length=20,
        choices=[('openai', 'OpenAI'), ('custom', 'Custom Model')]
    )
    created_at = models.DateTimeField(auto_now_add=True)