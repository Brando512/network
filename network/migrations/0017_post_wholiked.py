# Generated by Django 3.0.8 on 2020-08-04 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_auto_20200801_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='whoLiked',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
