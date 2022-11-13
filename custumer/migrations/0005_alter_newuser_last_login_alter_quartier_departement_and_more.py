# Generated by Django 4.0.5 on 2022-11-13 18:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0004_alter_newuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 13, 18, 2, 18, 871225, tzinfo=utc), verbose_name='last_login'),
        ),
        migrations.AlterField(
            model_name='quartier',
            name='departement',
            field=models.CharField(default='Abidjan', max_length=100),
        ),
        migrations.AlterField(
            model_name='quartier',
            name='district',
            field=models.CharField(default='Abidjan', max_length=100),
        ),
        migrations.AlterField(
            model_name='quartier',
            name='region',
            field=models.CharField(default='Abidjan', max_length=100),
        ),
        migrations.AlterField(
            model_name='quartier',
            name='sous_prefecture',
            field=models.CharField(default='Abidjan', max_length=100),
        ),
    ]
