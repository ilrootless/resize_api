# Generated by Django 3.0.8 on 2020-07-11 13:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('width', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('format', models.CharField(choices=[('png', 'png'), ('jpg', 'jpg')], max_length=5)),
                ('original', models.ImageField(upload_to='original', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])])),
                ('result', models.ImageField(blank=True, null=True, upload_to='result')),
            ],
        ),
    ]
