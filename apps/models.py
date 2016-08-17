from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.conf import settings
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import argparse
import base64
import httplib2

# Create your models here.



class ImageFile(models.Model):
    DETECTION_CHOICES = (
        ('FACE_DETECTION', 'FACE_DETECTION'),
        ('LANDMARK_DETECTION', 'LANDMARK_DETECTION'),
        ('LOGO_DETECTION', 'LOGO_DETECTION'),
        ('LABEL_DETECTION', 'LABEL_DETECTION'),
        ('TEXT_DETECTION', 'TEXT_DETECTION'),
        ('SAFE_SEARCH_DETECTION', 'SAFE_SEARCH_DETECTION'),
        ('IMAGE_PROPERTIES', 'IMAGE_PROPERTIES'),
    )
#    name = models.CharField(max_length = 100)
    detection = models.CharField(max_length = 32,  choices=DETECTION_CHOICES, default='LABEL_DETECTION')
    maxResult = models.IntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    result = models.TextField()
    data = models.ImageField(upload_to = 'apps/images/')
    datetime = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return self.data.name
    
    def detect(self):
        DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
        
        image_path = settings.MEDIA_ROOT+ '/'+ self.data.name
        print (image_path)
        credentials = GoogleCredentials.get_application_default()
        service = discovery.build('vision', 'v1', credentials=credentials, discoveryServiceUrl=DISCOVERY_URL)
        with open (image_path, 'rb') as image:
            image_content = base64.b64encode(image.read())
            service_request = service.images().annotate(body={
                'requests':[{
                    'image':{
                        'content': image_content.decode('UTF-8')
                        },
                    'features':[{
                        'type': self.detection,
                        'maxResults': self.maxResult
                    }]
                }]
            })
        response = service_request.execute()
        return response

    def save(self, *args, **kwargs):
        super(ImageFile, self).save(*args, **kwargs)
        self.result = self.detect()
        super(ImageFile, self).save(*args, **kwargs)
