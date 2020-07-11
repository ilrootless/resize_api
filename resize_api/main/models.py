from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models

class Resize(models.Model):
    height = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)], blank=False)
    width = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)], blank=False)
    FORMAT_CHOICES = [
        ('png', 'png'),
        ('jpg', 'jpg'),
    ]
    format = models.CharField(max_length=5, choices=FORMAT_CHOICES, blank=False)
    original = models.ImageField(upload_to='original', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])], blank=False)
    result = models.ImageField(upload_to='result', blank=True, null=True)
