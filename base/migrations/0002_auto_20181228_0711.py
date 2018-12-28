# Generated by Django 2.1.3 on 2018-12-28 07:11

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='description',
            field=models.TextField(default=' ', help_text='Say a few lines about your club'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=100, validators=[base.models.club_name_validator]),
        ),
    ]
