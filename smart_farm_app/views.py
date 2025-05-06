from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import Device, SensorData, CropHealth, ControlSystem, EducationalContent, ForumPost, ForumReply
from django.utils import timezone
import random

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'dashboard/signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/signup.html')

def signout(request):
    logout(request)
    return redirect('community')

def dashboard(request):
    # Latest sensor data
    data = SensorData.objects.last()
    # Last 10 sensor data points for chart
    sensor_data = SensorData.objects.order_by('-timestamp')[:10]
    # Devices
    devices = Device.objects.all()
    # AI Recommendations (placeholder)
    watering_schedule = "Water crops at 6 PM today."
    crop_health_status = "Healthy, no diseases detected."
    # Alerts (placeholder)
    alerts = ["Low soil moisture detected!", "Check nutrient levels."] if data and data.soil_moisture < 30 else []
    return render(request, 'dashboard/dashboard.html', {
        'data': data,
        'sensor_data': sensor_data,
        'devices': devices,
        'watering_schedule': watering_schedule,
        'crop_health_status': crop_health_status,
        'alerts': alerts,
    })

def control(request):
    if request.method == 'POST':
        device_id = request.POST.get('device_id')
        action = request.POST.get('action')
        if device_id and action:
            device = Device.objects.get(id=device_id)
            if action == 'turn_on':
                device.status = True
            elif action == 'turn_off':
                device.status = False
            device.save()
        elif action == 'irrigate':
            # Placeholder for IoT command
            ControlSystem.objects.create(irrigation=True)
            print("Irrigation started!")
    latest_data = SensorData.objects.last()
    devices = Device.objects.all()
    return render(request, 'control/control.html', {
        'latest_data': latest_data,
        'devices': devices,
    })

def analytics(request):
    total_contents = EducationalContent.objects.count()
    total_views = sum(content.views for content in EducationalContent.objects.all())
    total_posts = ForumPost.objects.count()
    recent_contents = EducationalContent.objects.order_by('-created_at')[:5]
    return render(request, 'dashboard/analytics.html', {
        'total_contents': total_contents,
        'total_views': total_views,
        'total_posts': total_posts,
        'recent_contents': recent_contents,
    })

def community(request):
    resources = EducationalContent.objects.all()
    posts = ForumPost.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'post':
            user = request.POST.get('user')
            content = request.POST.get('content')
            if user and content:
                ForumPost.objects.create(user=user, content=content)
                return redirect('community')
        elif form_type == 'reply':
            post_id = request.POST.get('post_id')
            reply_user = request.POST.get('reply_user')
            reply_content = request.POST.get('reply_content')
            if post_id and reply_user and reply_content:
                post = ForumPost.objects.get(id=post_id)
                ForumReply.objects.create(post=post, user=reply_user, content=reply_content)
                return redirect('community')
    return render(request, 'community/community.html', {'resources': resources, 'posts': posts})
