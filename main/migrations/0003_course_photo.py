# Generated by Django 4.2.1 on 2023-05-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='photo',
            field=models.ImageField(null=True, upload_to='course/images/'),
        ),
    ]