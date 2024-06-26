# Generated by Django 4.1.4 on 2024-04-20 09:21

import custumer.models
import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CritereCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agec', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('niveauEtude', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('maladie', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('handicap', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('occupations', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CritereChef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexeChef', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('agechef', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('nationalite', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('niveauEtude', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('maladie', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('handicap', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('occupations', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CritereCommodite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eclairage', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('cuisson', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('aeaux', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('ordure', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('nombrep', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('aisance', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('loyer', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('typelogement', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CritereConj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agec', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('niveauEtude', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('maladie', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('handicap', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('occupations', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CritereDeces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agec', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CritereEnfant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agec', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('niveauEtude', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('maladie', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('handicap', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CritereEquipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moyend', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('equipee', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('equipepo', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CritereGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditionvie', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('conditionphy', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('conditionoccup', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('conditionnivee', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CritereHabitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('quartier', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CritereMenage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moyenneage', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('niveauEtudeM', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('typeMenage', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('occupations', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Quartier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(default='Abidjan', max_length=100)),
                ('region', models.CharField(default='Abidjan', max_length=100)),
                ('departement', models.CharField(default='Abidjan', max_length=100)),
                ('sous_prefecture', models.CharField(default='Abidjan', max_length=100)),
                ('commune', models.CharField(max_length=100)),
                ('quartier', models.CharField(default='Rue_12_Avenue_11', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('nomz', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('commune', models.CharField(default='issa', max_length=100)),
                ('q1', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(default='issa', max_length=100)),
                ('agent', models.CharField(max_length=100)),
                ('create', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('quartier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custumer.zone')),
            ],
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(default='issa', max_length=30)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('adresse', models.CharField(blank=True, max_length=300, null=True)),
                ('about_me', models.TextField(blank=True, max_length=500, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_image', models.ImageField(blank=True, default='issa', upload_to=custumer.models.NewUser.nameFile)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_user', models.BooleanField(default=False)),
                ('is_agent', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(default=datetime.datetime(2024, 4, 20, 9, 21, 44, 441098, tzinfo=datetime.timezone.utc), verbose_name='last_login')),
                ('responsable', models.CharField(default='issa', max_length=30)),
                ('district', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('departement', models.CharField(max_length=100)),
                ('sous_prefecture', models.CharField(max_length=100)),
                ('commune', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
