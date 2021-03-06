# Generated by Django 3.1.7 on 2021-11-22 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 22, 22, 3, 15, 964414)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='firstname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lastname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
