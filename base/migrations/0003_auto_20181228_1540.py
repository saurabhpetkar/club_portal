# Generated by Django 2.1.3 on 2018-12-28 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20181228_0711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='description',
            new_name='about',
        ),
    ]
