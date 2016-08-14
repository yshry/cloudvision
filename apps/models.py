from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

"""
DETECTION_CHOICES = (
    ('FACE_DETECTION', 'FACE_DETECTION'),
    ('LANDMARK_DETECTION', 'LANDMARK_DETECTION'),
    ('LOGO_DETECTION', 'LOGO_DETECTION'),
    ('LABEL_DETECTION', 'LABEL_DETECTION'),
    ('TEXT_DETECTION', 'TEXT_DETECTION'),
    ('SAGE_SEARCH_DETECTION', 'SAFE_SEARCH_DETECTION'),
    ('IMAGE_PROPERTIES', 'IMAGE_PROPERTIES)',
)
"""

class ImageFile(models.Model):
    DETECTION_CHOICES = (
        ('FACE_DETECTION', 'FACE_DETECTION'),
        ('LANDMARK_DETECTION', 'LANDMARK_DETECTION'),
        ('LOGO_DETECTION', 'LOGO_DETECTION'),
        ('LABEL_DETECTION', 'LABEL_DETECTION'),
        ('TEXT_DETECTION', 'TEXT_DETECTION'),
        ('SAGE_SEARCH_DETECTION', 'SAFE_SEARCH_DETECTION'),
        ('IMAGE_PROPERTIES', 'IMAGE_PROPERTIES'),
    )
    name = models.CharField(max_length = 100)
    detection = models.CharField(max_length = 32,  choices=DETECTION_CHOICES, default='LABEL_DETECTION')
    maxResult = models.IntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    result = models.TextField()
    data = models.ImageField(upload_to = 'apps/images/')
    
    def __str__ (self):
        return self.name
