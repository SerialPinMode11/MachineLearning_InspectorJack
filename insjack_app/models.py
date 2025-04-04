from django.db import models
from datetime import datetime
import os
import uuid

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Username field, unique for each user
    password = models.CharField(max_length=128)  # Password field, typically hashed
    address = models.TextField()  # Address field for storing user addresses

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'usersTable'  # Set the table name to 'users' explicitly


def upload_to(instance, filename):
    """Generate a dynamic file path for uploaded images."""
    # Ensure a unique filename using UUID
    unique_name = f"{uuid.uuid4().hex}_{filename}"
    user_folder = instance.user.username if instance.user else "anonymous"
    return f'images/{user_folder}/{unique_name}'

class UploadedImage(models.Model):
    """Model for storing uploaded images and their classification results."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='uploaded_images',
        verbose_name="Uploader"
    )
    image = models.ImageField(upload_to=upload_to, verbose_name="Image File")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Upload Time")
    result = models.CharField(max_length=50, blank=True, null=True, verbose_name="Classification Result")
    confidence = models.FloatField(default=0.0, blank=True, null=True, verbose_name="Prediction Confidence")