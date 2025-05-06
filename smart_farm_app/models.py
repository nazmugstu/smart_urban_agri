from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    soil_moisture = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    light_level = models.FloatField()

    def __str__(self):
        return f"Data at {self.timestamp}"

class CropHealth(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    disease_detected = models.BooleanField(default=False)
    yield_prediction = models.FloatField()

    def __str__(self):
        return f"Health at {self.timestamp}"

class ControlSystem(models.Model):
    irrigation = models.BooleanField(default=False)
    climate_control = models.CharField(max_length=10, choices=[('heat', 'Heat'), ('cool', 'Cool'), ('off', 'Off')], default='off')
    nutrient_delivery = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Control at {self.timestamp}"

class EducationalContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='resources/', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ForumPost(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user} at {self.created_at}"

class ForumReply(models.Model):
    post = models.ForeignKey(ForumPost, related_name='replies', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user} at {self.created_at}"
