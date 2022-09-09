# Generated by Django 4.0.5 on 2022-09-09 14:47

import custumer.models
from django.conf import settings
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
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('adresse', models.CharField(blank=True, max_length=300, null=True)),
                ('about_me', models.TextField(blank=True, max_length=500, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('profile_image', models.ImageField(blank=True, upload_to=custumer.models.NewUser.nameFile)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_user', models.BooleanField(default=False)),
                ('is_agent', models.BooleanField(default=False)),
                ('responsable', models.CharField(default='issa', max_length=30)),
                ('district', models.CharField(choices=[('A', 'Abidjan'), ('B', 'Bas_Sassandra'), ('C', 'Comoe'), ('D', 'Denguele'), ('G', 'Goh_Djiboua'), ('L', 'Lacs'), ('La', 'Lagunes'), ('M', 'Montagnes'), ('SM', 'Sassandra_Marahoue'), ('Sa', 'Savanes'), ('Va', 'Vallee_du_Bandama'), ('W', 'Woroba'), ('Y', 'Yamoussoukro'), ('Za', 'Zanzan')], max_length=100)),
                ('region', models.CharField(choices=[('A', 'Abidjan'), ('AT', 'Agneby_tiassa'), ('Ba', 'Bafing'), ('Ba', 'Bagoue'), ('Be', 'Belier'), ('B', 'Bere'), ('Bo', 'Bounkani'), ('Ca', 'Cavally'), ('Fo', 'Folon'), ('Gb', 'Gbeke'), ('Gbo', 'Gbokle'), ('Go', 'Goh'), ('Gu', 'Guemon'), ('In', 'Indenie_djuablin'), ('Ka', 'Kabadougou'), ('Na', 'Nawa'), ('Lo', 'Loh_Djiboua'), ('If', ' Iffou'), ('Mo', 'Moronou'), ('Nz', 'Nzi'), ('LM', 'La_Me'), ('To', 'Tonkpi'), ('Hs', 'Haut_Sassandra'), ('Mr', 'Marahoué'), ('Po', 'Poro'), ('Tc', 'Tchologo'), ('Ha', 'Hambol'), ('Go', 'Gontougou'), ('Sp', 'San_pedro'), ('Sc', 'Sud_Comoe'), ('Wo', 'Worodougou')], max_length=100)),
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
                ('commune', models.CharField(max_length=100)),
                ('quartier', models.CharField(default='Rue_12_Avenue_11', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commune', models.CharField(max_length=100)),
                ('quartier', models.CharField(default='Rue_12_Avenue_11', max_length=100)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
