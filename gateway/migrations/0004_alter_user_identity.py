# Generated by Django 5.0.3 on 2024-03-31 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0003_user_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='identity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gateway.identityrecord'),
        ),
    ]
