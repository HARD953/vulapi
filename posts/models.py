from django.conf import settings
from django.utils import timezone
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin, AbstractBaseUser,BaseUserManager
from django.utils import timezone

from custumer.models import NewUser

# Create your models here.

# class District(models.Model):
#     district_list=(('A','Abidjan'),('B','Bas_Sassandra'),('C','Comoe'),('D','Denguele'),('G','Goh_Djiboua'),('L','Lacs'),('La','Lagunes'),('M','Montagnes'),('SM','Sassandra_Marahoue'),('Sa','Savanes'),('Va','Vallee_du_Bandama'),('W','Woroba'),('Y','Yamoussoukro'),('Za','Zanzan'))
#     district=models.CharField(max_length=100,blank=False,choices=district_list)
#     def __str__(self):
#         return '{}'.format(self.district)
# class Region(models.Model):
#     list_region=(('A','Abidjan'),('AT','Agneby_tiassa'),('Ba','Bafing'),('Ba','Bagoue'),('Be','Belier'),('B','Bere'),('Bo','Bounkani'),('Ca','Cavally'),('Fo','Folon'),('Gb','Gbeke'),('Gbo','Gbokle'),('Go','Goh'),('Gu','Guemon'),('In','Indenie_djuablin'),('Ka','Kabadougou'),('Na','Nawa'),('Lo','Loh_Djiboua'),('If',' Iffou'),('Mo','Moronou'),('Nz','Nzi'),('LM','La_Me'),('To','Tonkpi'),('Hs','Haut_Sassandra'),('Mr','Marahoué'),('Po','Poro'),('Tc','Tchologo'),('Ha','Hambol'),('Go','Gontougou'),('Sp','San_pedro'),('Sc','Sud_Comoe'),('Wo','Worodougou'))
#     region=models.CharField(max_length=100,blank=False,choices=list_region)
#     def __str__(self):
#         return '{}'.format(self.region)
# class Departement(models.Model):
#     departement=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}'.format(self.departement)
# class Sous_prefecture(models.Model):
#     sous_prefecture=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}'.format(self.sous_prefecture)
# class Commune(models.Model):
#     commune=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}'.format(self.commune)
# class Milieu(models.Model):
#     milieu_r=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}'.format(self.milieu_r)
# class Quartier(models.Model):
#     quartier=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}_{}'.format(self.quartier)

# class Affecter(models.Model):
#     agentr=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     localite=models.ForeignKey(Localite,on_delete=models.CASCADE)
#     create=models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return '{}_{}'.format(self.agentr,self.localite)

class Personne(NewUser):
    nom=models.CharField(max_length=100,blank=False)
    annee_naissance=models.DateField(blank=False)
    lieu_de_naissance=models.CharField(max_length=100,blank=False,default="abidjan")
    nationalite=models.CharField(max_length=100,blank=False,default="ivoirienne")
    numero_cni=models.CharField(max_length=100,blank=False)
    sexe=(('M','Maxculin'),('F','Feminin'))
    sexes=models.CharField(max_length=1,choices=sexe)
    ethnie=models.CharField(max_length=100,blank=False)
    numero=models.CharField(max_length=100,blank=False,unique=True)
    #Localisation
    milieu_r=models.CharField(max_length=100,blank=False,default='urbain')
    quartier=models.CharField(max_length=100,blank=False,default='Rue_12_Avenue_11')
    class Meta:
        abstract=True
    def __str__(self):
        return '{}_{}'.format(self.nom,self.first_name)

class Chef_menage(Personne):
    owner1 = models.CharField(max_length=100,blank=False)
    type_m=(('Mnf','Menage_non_familial'),('Mbn','Menage_biparental_nucléaire'),('Mbe','Ménage_Biparental_élargi'),('Mi','Ménage_isolé'),('Mm','Ménage_monoparental'),('Mme','Ménage_monoparental_elargi'))
    type_menage=models.CharField(max_length=100,blank=False,choices=type_m)
    nombre_enfant=models.IntegerField(default=0)
    nombre_enfant_v=models.IntegerField(default=0)
    nom_personne_charge=models.IntegerField(default=0)
    conjoints=models.BooleanField(default=False)
    immigre=models.BooleanField(default=False)
    date_depart=models.DateField(null=True)
    age_depart=models.PositiveBigIntegerField()
    motif=models.CharField(max_length=100,blank=False)
    migrant=models.BooleanField()
    annee_deplace=models.DateField(blank=False)
    lieu_residence_a=models.CharField(max_length=100,blank=False)
    intention_ret=models.BooleanField()
    vulnerablePhy=models.BooleanField(default=False)
    vulnerableCondi=models.BooleanField(default=False)
    vulnerableEtude=models.BooleanField(default=False)
    vulnerableOccup=models.BooleanField(default=False)
    individu=models.BooleanField(default=False)
    menage=models.BooleanField(default=False)
    def __str__(self):
        return '{}_{}'.format(self.nom,self.first_name)

class Recenser(models.Model):
    parent=models.CharField(max_length=100,blank=False)
    owner3 = models.CharField(max_length=100,blank=False)
    list_handicap=(('S','Sans_Handicap'),('Nv','Non_voyant'),('So','Sourd'),('Mu','Muet'),('Be','Begue'),('Al','Albinos'),('Hms','Handicap_membre_superieurs'),('Hmi','Handicap_membre_inferieurs'),('Hp','Handicap_physiques'),('Au','Autre_handicap'))
    handicap=models.CharField(max_length=100,blank=False,choices=list_handicap)
    maladie=models.CharField(max_length=100,blank=False)
    list1=(('Vm','Vie_Ménage'),('Hm','Hors_Ménage'),('D','Décédé'),('N','RAS'))
    survie_de_mere=models.BooleanField(default=True)
    survie_de_pere=models.BooleanField(default=True )
    niveau_instruction=models.CharField(max_length=100,blank=False)
    occupation_actuelle=models.CharField(max_length=100,blank=False)
    situation_matrimoniale=models.CharField(max_length=100,blank=False)
    list_religion=(('C','Catholique'),('M','Méthodique'),('E','Evangélique'),('Ce','Céleste'),('H','Harriste'),('Au','AutreRC'),('Mu','Mulsuman'),('An','Animiste'),('Au','AutreR'),('S','Sans_Religion'))
    religion=models.CharField(max_length=100,blank=False,choices=list_religion)
    class Meta:
        ordering=['parent']
    def __str__(self):
        return '{}'.format(self.parent)
        
class Conjoint(models.Model):
    niveau_etude=models.CharField(max_length=100,blank=True,default='master')
    occupation=models.CharField(max_length=100,blank=True,default='Informaticien')
    annee_naissance=models.DateField(blank=False)
    idc=models.CharField(max_length=100,blank=False)
    sexe=(('M','Maxculin'),('F','Feminin'))
    sexes=models.CharField(max_length=1,choices=sexe)
    list_handicap=(('S','Sans_Handicap'),('Nv','Non_voyant'),('So','Sourd'),('Mu','Muet'),('Be','Begue'),('Al','Albinos'),('Hms','Handicap_membre_superieurs'),('Hmi','Handicap_membre_inferieurs'),('Hp','Handicap_physiques'),('Au','Autre_handicap'))
    handicap=models.CharField(max_length=100,blank=False,choices=list_handicap)
    owner2 = models.CharField(max_length=100,blank=False)
    maladie=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return '{}'.format(self.idc)

class Enfant(models.Model):
    parentf=models.CharField(max_length=100,blank=False)
    annee_naissance=models.DateField(blank=False)
    owner4 = models.CharField(max_length=100,blank=False)
    niveau_etude=models.CharField(max_length=100,blank=True,default='master')
    sexe=(('M','Maxculin'),('F','Feminin'))
    sexes=models.CharField(max_length=1,choices=sexe)
    list_handicap=(('S','Sans_Handicap'),('Nv','Non_voyant'),('So','Sourd'),('Mu','Muet'),('Be','Begue'),('Al','Albinos'),('Hms','Handicap_membre_superieurs'),('Hmi','Handicap_membre_inferieurs'),('Hp','Handicap_physiques'),('Au','Autre_handicap'))
    handicap=models.CharField(max_length=100,blank=False,choices=list_handicap)
    maladie=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return '{}'.format(self.parentf)
  
class Commodite(models.Model):
    parentc=models.CharField(max_length=100,blank=False)
    owner5 = models.CharField(max_length=100,blank=False)
    nombre_piece=models.IntegerField(default=1)
    nombre_piece_dormir=models.IntegerField(default=1)
    typelogement=models.CharField(max_length=100,blank=False)
    
    lieu_aisance=models.CharField(max_length=100,blank=False)
    alimentation_eau=models.CharField(max_length=100,blank=False)
    eclairage=models.CharField(max_length=100,blank=False)
    cuisson=models.CharField(max_length=100,blank=False)
    evacuation_ordure=models.CharField(max_length=100,blank=False)
    evacuation_eau=models.CharField(max_length=100,blank=False)
    loyer=models.CharField(max_length=100,blank=False)
    class Meta:
        ordering=['parentc']

class Equipement(models.Model):
    parente=models.CharField(max_length=100,blank=False)
    owner6 = models.CharField(max_length=100,blank=False)
    equipement_electr=models.CharField(max_length=100,blank=False)
    equipement_audio=models.CharField(max_length=100,blank=False)
    moyen_deplacement=models.CharField(max_length=100,blank=False)
    proprietaire=models.BooleanField(default=True)
    class Meta:
        ordering=['parente']

class Deces(models.Model):
    parentd=models.CharField(max_length=100,blank=False)
    owner7 = models.CharField(max_length=100,blank=False)
    sexed=(('M','Maxculin'),('F','Feminin'))
    sexesd=models.CharField(max_length=1,choices=sexed)
    annee_deces=models.DateField(blank=False)
    class Meta:
        ordering=['parentd']
    def __str__(self):
        return '{}'.format(self.parentd)

class Charge(models.Model):
    parentg=models.CharField(max_length=100,blank=False)
    sexed=(('M','Maxculin'),('F','Feminin'))
    sexesd=models.CharField(max_length=1,choices=sexed)
    annee_naissance=models.DateField(blank=False)
    owner8 = models.CharField(max_length=100,blank=False)
    niveau_etude=models.CharField(max_length=100,blank=True,default='master')
    occupation=models.CharField(max_length=100,blank=True,default='Informaticien')
    immigre=models.BooleanField(default=False)
    intention_ret=models.BooleanField()
    list_handicap=(('S','Sans_Handicap'),('Nv','Non_voyant'),('So','Sourd'),('Mu','Muet'),('Be','Begue'),('Al','Albinos'),('Hms','Handicap_membre_superieurs'),('Hmi','Handicap_membre_inferieurs'),('Hp','Handicap_physiques'),('Au','Autre_handicap'))
    handicap=models.CharField(max_length=100,blank=False,choices=list_handicap)
    maladie=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return '{}'.format(self.parentg)

class Enfant_R(NewUser):
    annee_nais=models.DateField(blank=False)
    maladie=models.CharField(max_length=100,blank=False)
    lieu_nais=models.CharField(max_length=100,blank=False)
    owner9  = models.CharField(max_length=100,blank=False)
    niveau_etude=models.CharField(max_length=100,blank=True,default='master')
    sexe=models.CharField(max_length=30)
    handicap=models.CharField(max_length=100,blank=False)
    battu=models.BooleanField(default=False)
    tuteur=models.BooleanField(default=False)
    tutrice=models.BooleanField(default=False)
    pere=models.BooleanField(default=False)
    mere=models.BooleanField(default=False)
    scolariser=models.BooleanField(default=False)
    quartier=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return '{}'.format(self.niveau_etude)
    #x=['nom','prenom','annee_naissance','owner4','niveau_etude','sexes','scolariser','mere','pere','tuteur','handicap','battue']


class Test1(models.Model):
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.nom)

class Test2(models.Model):
    classe=models.CharField(max_length=255)
    niveau=models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.classe)
        
class DonsArgent(models.Model):
    iddons=models.CharField(max_length=30,default=1)
    beneficiaire=models.CharField(max_length=30,default='issa')
    donateur=models.CharField(max_length=30,default='issa')
    typePersonne=models.CharField(max_length=100,default='null')
    typeDons=models.CharField(max_length=30,default='null')
    montant=models.CharField(max_length=100,default='null')
    create=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    idTransaction=models.CharField(max_length=100,default='null')
    def __str__(self):
        return '{}'.format(self.beneficiaire) 

# class DonsNature(models.Model):
    # def nameFile(instance, filename):
    #     return '/'.join(['images', str(instance.donateur), filename])
#     iddons=models.CharField(max_length=30,default=1)
#     beneficiaire=models.CharField(max_length=30,default='issa')
#     donateur=models.CharField(max_length=30,default='issa')
#     typePersonne=models.CharField(max_length=100,default='null')
#     typeDons=models.CharField(max_length=30,default='null')
#     categorieObjet=models.CharField(max_length=100,default='null')
#     typeObjet=models.CharField(max_length=30,default='null')
#     lieu_reception=models.CharField(max_length=100,default='null')
#     photo=models.ImageField(upload_to=nameFile,blank=True)
#     Etat=models.CharField(max_length=100,default='null')
#     create=models.DateTimeField(auto_now_add=True)
#     status=models.BooleanField(default=False)
#     idTransaction=models.CharField(max_length=100,default='null')
#     def __str__(self):
#         return '{}'.format(self.beneficiaire)

class DonsNature(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.donateur), filename])
    iddons=models.CharField(max_length=30,default=1)
    beneficiaire=models.CharField(max_length=30,default='issa')
    donateur=models.CharField(max_length=30,default='issa')
    lieu_reception=models.CharField(max_length=100,default='null')
    photo=models.ImageField(upload_to=nameFile,blank=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return '{}'.format(self.beneficiaire)
   
   
    
   







