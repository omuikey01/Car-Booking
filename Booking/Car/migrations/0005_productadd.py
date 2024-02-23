# Generated by Django 5.0.1 on 2024-02-23 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0004_rename_photo_images_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_id', models.IntegerField()),
                ('car_name', models.CharField(max_length=100)),
                ('car_color', models.CharField(max_length=100)),
                ('amt_per_km', models.IntegerField()),
                ('discount_per', models.IntegerField(blank=True)),
                ('image1', models.ImageField(blank=True, upload_to='images')),
                ('image2', models.ImageField(blank=True, upload_to='images')),
                ('image3', models.ImageField(blank=True, upload_to='images')),
                ('image4', models.ImageField(blank=True, upload_to='images')),
                ('image5', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
