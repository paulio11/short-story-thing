# Generated by Django 4.2.19 on 2025-02-25 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='public',
            new_name='is_public',
        ),
    ]
