# Generated by Django 5.0.3 on 2024-04-01 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0004_alter_user_identity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identityrecord',
            old_name='identity_id',
            new_name='identity_key',
        ),
    ]
