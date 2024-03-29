# Generated by Django 5.0.2 on 2024-03-07 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0004_initial'),
        ('ticketManagement', '0002_delete_ec_delete_technicalfault'),
    ]

    operations = [
        migrations.CreateModel(
            name='EC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('UPDATED', 'Updated'), ('VOIDED', 'Void'), ('PENDING', 'Pending')], default='PENDING', max_length=10)),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('module', models.CharField(max_length=100)),
                ('component', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TechnicalFault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('UPDATED', 'Updated'), ('VOIDED', 'Void'), ('PENDING', 'Pending')], default='PENDING', max_length=10)),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('location', models.CharField(choices=[('ITL', 'ITL'), ('ITS', 'ITS'), ('Library', 'Library')], max_length=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
