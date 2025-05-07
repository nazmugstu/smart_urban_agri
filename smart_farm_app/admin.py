from django.contrib import admin
from .models import Device, SensorData, CropHealth, ControlSystem, EducationalContent, ForumPost, ForumReply

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'last_updated')

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'soil_moisture', 'temperature', 'humidity', 'light_level')

@admin.register(CropHealth)
class CropHealthAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'disease_detected', 'yield_prediction')

@admin.register(ControlSystem)
class ControlSystemAdmin(admin.ModelAdmin):
    list_display = ('irrigation', 'climate_control', 'nutrient_delivery', 'timestamp')

@admin.register(EducationalContent)
class EducationalContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'created_at')

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')

@admin.register(ForumReply)
class ForumReplyAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')