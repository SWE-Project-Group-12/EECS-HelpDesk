# Generated by Django 5.0.2 on 2024-03-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketManagement', '0004_alter_technicalfault_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='ec',
            name='status_update_reason',
            field=models.CharField(default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='technicalfault',
            name='status_update_reason',
            field=models.CharField(default=' ', max_length=150),
        ),
    ]
