# Generated by Django 5.0.3 on 2024-04-01 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0008_alter_identityrecord_sexe'),
    ]

    operations = [
        migrations.AddField(
            model_name='identityrecord',
            name='profession',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='MarriageCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=100)),
                ('partner1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='gateway.identityrecord')),
                ('partner2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='gateway.identityrecord')),
            ],
        ),
    ]
