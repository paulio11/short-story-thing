# Generated by Django 4.2.19 on 2025-03-01 23:21

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_alter_activity_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='progress',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00')), django.core.validators.MaxValueValidator(Decimal('100.00'))]),
        ),
    ]
