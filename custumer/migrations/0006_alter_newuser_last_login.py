# Generated by Django 4.0.5 on 2022-09-12 09:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0005_alter_affectation_agent_alter_newuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 9, 58, 34, 652520, tzinfo=utc), verbose_name='last_login'),
        ),
    ]
