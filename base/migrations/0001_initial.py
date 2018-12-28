# Generated by Django 2.1.3 on 2018-12-28 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_formed', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('is_supported', models.BooleanField(default=True)),
                ('num_users', models.IntegerField(default=0)),
            ],
        ),
    ]
