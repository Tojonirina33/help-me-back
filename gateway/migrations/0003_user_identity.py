# Generated by Django 5.0.3 on 2024-03-31 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0002_identityrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identity',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='gateway.identityrecord'),
        ),
    ]
