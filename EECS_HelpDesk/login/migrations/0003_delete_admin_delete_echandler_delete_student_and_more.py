# Generated by Django 5.0.2 on 2024-03-07 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_admin_id_remove_echandler_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='ECHandler',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='TechnicalFaultHandler',
        ),
    ]