# Generated by Django 5.0.7 on 2024-07-16 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_alter_hotel_address_alter_hotel_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='bookings.hotel'),
        ),
    ]
