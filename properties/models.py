from django.db import models
from agents.models import Agent
# Create your models here.


class Property(models.Model):
    PROPERTY_TYPE = (
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
    )

    STATUS_CHOICES = (
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('sold', 'Sold'),
    )

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.IntegerField(help_text='Area in square feet')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sale')
    featured_image = models.ImageField(upload_to='properties/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property-images/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image for {self.property.title}'
    