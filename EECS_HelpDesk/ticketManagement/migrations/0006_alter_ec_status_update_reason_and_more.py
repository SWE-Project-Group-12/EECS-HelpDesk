# Generated by Django 5.0.2 on 2024-03-24 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketManagement', '0005_ec_status_update_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ec',
            name='status_update_reason',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='technicalfault',
            name='status_update_reason',
            field=models.CharField(default='', max_length=150),
        ),
    ]
