# Generated by Django 4.1.4 on 2024-04-20 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 20, 9, 22, 3, 437473, tzinfo=datetime.timezone.utc), verbose_name='last_login'),
        ),
    ]
