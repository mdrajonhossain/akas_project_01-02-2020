# Generated by Django 2.2 on 2020-02-01 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0008_logintype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintype',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Logintype', to=settings.AUTH_USER_MODEL),
        ),
    ]