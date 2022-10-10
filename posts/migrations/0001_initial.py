# Generated by Django 4.0.5 on 2022-10-10 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custumer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef_menage',
            fields=[
                ('newuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nom', models.CharField(max_length=100)),
                ('annee_naissance', models.DateField()),
                ('lieu_de_naissance', models.CharField(default='abidjan', max_length=100)),
                ('nationalite', models.CharField(default='ivoirienne', max_length=100)),
                ('numero_cni', models.CharField(max_length=100)),
                ('sexes', models.CharField(choices=[('M', 'Maxculin'), ('F', 'Feminin')], max_length=1)),
                ('ethnie', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100, unique=True)),
                ('milieu_r', models.CharField(default='urbain', max_length=100)),
                ('quartier', models.CharField(default='Rue_12_Avenue_11', max_length=100)),
                ('type_menage', models.CharField(choices=[('Mnf', 'Menage_non_familial'), ('Mbn', 'Menage_biparental_nucléaire'), ('Mbe', 'Ménage_Biparental_élargi'), ('Mi', 'Ménage_isolé'), ('Mm', 'Ménage_monoparental'), ('Mme', 'Ménage_monoparental_elargi')], max_length=100)),
                ('nombre_enfant', models.IntegerField(default=0)),
                ('nombre_enfant_v', models.IntegerField(default=0)),
                ('nom_personne_charge', models.IntegerField(default=0)),
                ('conjoints', models.BooleanField(default=False)),
                ('immigre', models.BooleanField(default=False)),
                ('date_depart', models.DateField(null=True)),
                ('age_depart', models.PositiveBigIntegerField()),
                ('motif', models.CharField(max_length=100)),
                ('migrant', models.BooleanField()),
                ('annee_deplace', models.DateField()),
                ('lieu_residence_a', models.CharField(max_length=100)),
                ('intention_ret', models.BooleanField()),
                ('vulnerablePhy', models.BooleanField(default=False)),
                ('vulnerableCondi', models.BooleanField(default=False)),
                ('vulnerableEtude', models.BooleanField(default=False)),
                ('vulnerableOccup', models.BooleanField(default=False)),
                ('individu', models.BooleanField(default=False)),
                ('menage', models.BooleanField(default=False)),
                ('owner1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_chef_menage', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('custumer.newuser',),
        ),
        migrations.CreateModel(
            name='DonsArgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiaire', models.CharField(default='issa', max_length=30)),
                ('donateur', models.CharField(default='issa', max_length=30)),
                ('typeDons', models.CharField(default='null', max_length=30)),
                ('montant', models.CharField(default='null', max_length=100)),
                ('typePersonne', models.CharField(default='null', max_length=100)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonsNature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiaire', models.CharField(default='issa', max_length=30)),
                ('donateur', models.CharField(default='issa', max_length=30)),
                ('typeDons', models.CharField(default='null', max_length=30)),
                ('categorieObjet', models.CharField(default='null', max_length=100)),
                ('typeObjet', models.CharField(default='null', max_length=30)),
                ('lieu_reception', models.CharField(default='null', max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to=posts.models.DonsNature.nameFile)),
                ('Etat', models.CharField(default='null', max_length=100)),
                ('typePersonne', models.CharField(default='null', max_length=100)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.CharField(max_length=255)),
                ('niveau', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recenser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handicap', models.CharField(choices=[('S', 'Sans_Handicap'), ('Nv', 'Non_voyant'), ('So', 'Sourd'), ('Mu', 'Muet'), ('Be', 'Begue'), ('Al', 'Albinos'), ('Hms', 'Handicap_membre_superieurs'), ('Hmi', 'Handicap_membre_inferieurs'), ('Hp', 'Handicap_physiques'), ('Au', 'Autre_handicap')], max_length=100)),
                ('maladie', models.CharField(max_length=100)),
                ('survie_de_mere', models.BooleanField(default=True)),
                ('survie_de_pere', models.BooleanField(default=True)),
                ('niveau_instruction', models.CharField(max_length=100)),
                ('occupation_actuelle', models.CharField(max_length=100)),
                ('situation_matrimoniale', models.CharField(max_length=100)),
                ('religion', models.CharField(choices=[('C', 'Catholique'), ('M', 'Méthodique'), ('E', 'Evangélique'), ('Ce', 'Céleste'), ('H', 'Harriste'), ('Au', 'AutreRC'), ('Mu', 'Mulsuman'), ('An', 'Animiste'), ('Au', 'AutreR'), ('S', 'Sans_Religion')], max_length=100)),
                ('owner3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_recenser', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.chef_menage')),
            ],
            options={
                'ordering': ['parent'],
            },
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moyen_deplacement', models.CharField(max_length=100)),
                ('equipement_electr', models.CharField(max_length=100)),
                ('equipement_audio', models.CharField(max_length=100)),
                ('proprietaire', models.BooleanField(default=True)),
                ('owner6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_equipement', to=settings.AUTH_USER_MODEL)),
                ('parente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.chef_menage')),
            ],
            options={
                'ordering': ['parente'],
            },
        ),
        migrations.CreateModel(
            name='Enfant_R',
            fields=[
                ('newuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nom', models.CharField(max_length=100)),
                ('annee_naissance', models.DateField()),
                ('maladie', models.CharField(max_length=100)),
                ('niveau_etude', models.CharField(blank=True, default='master', max_length=100)),
                ('sexes', models.CharField(choices=[('M', 'Maxculin'), ('F', 'Feminin')], max_length=1)),
                ('handicap', models.CharField(choices=[('S', 'Sans_Handicap'), ('Nv', 'Non_voyant'), ('So', 'Sourd'), ('Mu', 'Muet'), ('Be', 'Begue'), ('Al', 'Albinos'), ('Hms', 'Handicap_membre_superieurs'), ('Hmi', 'Handicap_membre_inferieurs'), ('Hp', 'Handicap_physiques'), ('Au', 'Autre_handicap')], max_length=100)),
                ('battue', models.BooleanField(default=False)),
                ('tuteur', models.BooleanField(default=False)),
                ('pere', models.BooleanField(default=False)),
                ('mere', models.BooleanField(default=False)),
                ('scolariser', models.BooleanField(default=False)),
                ('quartier', models.CharField(max_length=100)),
                ('owner9', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enfant_rue', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('custumer.newuser',),
        ),
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_naissance', models.DateField()),
                ('niveau_etude', models.CharField(blank=True, default='master', max_length=100)),
                ('sexes', models.CharField(choices=[('M', 'Maxculin'), ('F', 'Feminin')], max_length=1)),
                ('handicap', models.CharField(choices=[('S', 'Sans_Handicap'), ('Nv', 'Non_voyant'), ('So', 'Sourd'), ('Mu', 'Muet'), ('Be', 'Begue'), ('Al', 'Albinos'), ('Hms', 'Handicap_membre_superieurs'), ('Hmi', 'Handicap_membre_inferieurs'), ('Hp', 'Handicap_physiques'), ('Au', 'Autre_handicap')], max_length=100)),
                ('maladie', models.CharField(max_length=100)),
                ('owner4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_enfant', to=settings.AUTH_USER_MODEL)),
                ('parentf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.chef_menage')),
            ],
        ),
        migrations.CreateModel(
            name='Deces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexesd', models.CharField(choices=[('M', 'Maxculin'), ('F', 'Feminin')], max_length=1)),
                ('annee_deces', models.DateField()),
                ('owner7', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_deces', to=settings.AUTH_USER_MODEL)),
                ('parentd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.chef_menage')),
            ],
            options={
                'ordering': ['parentd'],
            },
        ),
        migrations.CreateModel(
            name='Conjoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau_etude', models.CharField(blank=True, default='master', max_length=100)),
                ('occupation', models.CharField(blank=True, default='Informaticien', max_length=100)),
                ('annee_naissance', models.DateField()),
                ('sexes', models.CharField(choices=[('M', 'Maxculin'), ('F', 'Feminin')], max_length=1)),
                ('handicap', models.CharField(choices=[('S', 'Sans_Handicap'), ('Nv', 'Non_voyant'), ('So', 'Sourd'), ('Mu', 'Muet'), ('Be', 'Begue'), ('Al', 'Albinos'), ('Hms', 'Handicap_membre_superieurs'), ('Hmi', 'Handicap_membre_inferieurs'), ('Hp', 'Handicap_physiques'), ('Au', 'Autre_handicap')], max_length=100)),
                ('maladie', models.CharField(max_length=100)),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.chef_menage')),
                ('owner2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_conjoint', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commodite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_piece', models.IntegerField(default=1)),
                ('nombre_piece_dormir', models.IntegerField(default=1)),
                ('typelogement', models.CharField(max_length=100)),
                ('lieu_aisance', models.CharField(max_length=100)),
                ('alimentation_eau', models.CharField(max_length=100)),
                ('eclairage', models.CharField(max_length=100)),
                ('cuisson', models.CharField(max_length=100)),
                ('evacuation_ordure', models.CharField(max_length=100)),
                ('evacuation_eau', models.CharField(max_length=100)),
                ('loyer', models.CharField(max_length=100)),
                ('owner5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_commodite', to=settings.AUTH_USER_MODEL)),
                ('parentc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.chef_menage')),
            ],
            options={
                'ordering': ['parentc'],
            },
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexesd', models.CharField(choices=[('M', 'Maxculin'), ('F', 'Feminin')], max_length=1)),
                ('annee_naissance', models.DateField()),
                ('niveau_etude', models.CharField(blank=True, default='master', max_length=100)),
                ('occupation', models.CharField(blank=True, default='Informaticien', max_length=100)),
                ('immigre', models.BooleanField(default=False)),
                ('intention_ret', models.BooleanField()),
                ('handicap', models.CharField(choices=[('S', 'Sans_Handicap'), ('Nv', 'Non_voyant'), ('So', 'Sourd'), ('Mu', 'Muet'), ('Be', 'Begue'), ('Al', 'Albinos'), ('Hms', 'Handicap_membre_superieurs'), ('Hmi', 'Handicap_membre_inferieurs'), ('Hp', 'Handicap_physiques'), ('Au', 'Autre_handicap')], max_length=100)),
                ('maladie', models.CharField(max_length=100)),
                ('owner8', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_charge', to=settings.AUTH_USER_MODEL)),
                ('parentg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.chef_menage')),
            ],
        ),
    ]
