# Generated by Django 4.0.6 on 2022-08-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t6_dashboard', '0003_rename_point_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
