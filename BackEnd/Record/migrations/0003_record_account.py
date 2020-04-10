# Generated by Django 3.0.5 on 2020-04-09 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Record', '0002_auto_20200409_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
