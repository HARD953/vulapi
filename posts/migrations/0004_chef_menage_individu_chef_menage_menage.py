# Generated by Django 4.0.5 on 2022-08-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_chef_menage_vulnerableetude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef_menage',
            name='individu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chef_menage',
            name='menage',
            field=models.BooleanField(default=False),
        ),
    ]
