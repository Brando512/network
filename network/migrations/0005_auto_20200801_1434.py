# Generated by Django 3.0.8 on 2020-08-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20200801_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(null=True, to='network.Comments'),
        ),
    ]
