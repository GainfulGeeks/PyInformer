# Generated by Django 5.0.6 on 2024-05-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_worker_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='ssn',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]