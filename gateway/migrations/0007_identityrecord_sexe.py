# Generated by Django 5.0.3 on 2024-04-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0006_alter_identityrecord_distinctive_trait'),
    ]

    operations = [
        migrations.AddField(
            model_name='identityrecord',
            name='sexe',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=10),
        ),
    ]
