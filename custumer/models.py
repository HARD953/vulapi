from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin, AbstractBaseUser,BaseUserManager
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from distutils.command.upload import upload

from posts.critere.indicateur import moyenneage, niveau, occupations
from django.conf import settings

# Create your models here.

class CustumerAccountManager(BaseUserManager):
    def create_user(self, email, user_name,first_name,password, **other_fields):
        if not email:
            raise ValueError("you must provide a email address")
        email=self.normalize_email(email)
        user=self.model(email=email,user_name=user_name,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name,first_name, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email, user_name,first_name,**other_fields)

# class Localite(models.Model):
#     district_list=(('A','Abidjan'),('B','Bas_Sassandra'),('C','Comoe'),('D','Denguele'),('G','Goh_Djiboua'),('L','Lacs'),('La','Lagunes'),('M','Montagnes'),('SM','Sassandra_Marahoue'),('Sa','Savanes'),('Va','Vallee_du_Bandama'),('W','Woroba'),('Y','Yamoussoukro'),('Za','Zanzan'))
#     district=models.CharField(max_length=100,blank=False,choices=district_list)
#     list_region=(('A','Abidjan'),('AT','Agneby_tiassa'),('Ba','Bafing'),('Ba','Bagoue'),('Be','Belier'),('B','Bere'),('Bo','Bounkani'),('Ca','Cavally'),('Fo','Folon'),('Gb','Gbeke'),('Gbo','Gbokle'),('Go','Goh'),('Gu','Guemon'),('In','Indenie_djuablin'),('Ka','Kabadougou'),('Na','Nawa'),('Lo','Loh_Djiboua'),('If',' Iffou'),('Mo','Moronou'),('Nz','Nzi'),('LM','La_Me'),('To','Tonkpi'),('Hs','Haut_Sassandra'),('Mr','Marahoué'),('Po','Poro'),('Tc','Tchologo'),('Ha','Hambol'),('Go','Gontougou'),('Sp','San_pedro'),('Sc','Sud_Comoe'),('Wo','Worodougou'))
#     region=models.CharField(max_length=100,blank=False,choices=list_region)
#     departement=models.CharField(max_length=100,blank=False)
#     sous_prefecture=models.CharField(max_length=100,blank=False)
#     commune=models.CharField(max_length=100,blank=False)
#     milieu_r=models.CharField(max_length=100,blank=False)
#     quartier=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}_{}'.format(self.commune,self.quartier)

class NewUser(AbstractBaseUser,PermissionsMixin):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.user_name), filename])
    user_name=models.CharField(max_length=30,unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30,default="issa")
    start_date=models.DateTimeField(default=timezone.now)
    email=models.EmailField(max_length=255,unique=True)
    adresse=models.CharField(max_length=300, blank=True, null=True)
    about_me=models.TextField(max_length=500, blank=True, null=True)
    create=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image=models.ImageField(upload_to=nameFile,blank=True,default="issa")
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)
    is_agent=models.BooleanField(default=False)
    last_login = models.DateTimeField(('last_login'), default=timezone.now())
    responsable=models.CharField(max_length=30,default="issa")
    district_list=(('A','Abidjan'),('B','Bas_Sassandra'),('C','Comoe'),('D','Denguele'),('G','Goh_Djiboua'),('L','Lacs'),('La','Lagunes'),('M','Montagnes'),('SM','Sassandra_Marahoue'),('Sa','Savanes'),('Va','Vallee_du_Bandama'),('W','Woroba'),('Y','Yamoussoukro'),('Za','Zanzan'))

    district=models.CharField(max_length=100,blank=False)
    list_region=(('A','Abidjan'),('AT','Agneby_tiassa'),('Ba','Bafing'),('Ba','Bagoue'),('Be','Belier'),('B','Bere'),('Bo','Bounkani'),('Ca','Cavally'),('Fo','Folon'),('Gb','Gbeke'),('Gbo','Gbokle'),('Go','Goh'),('Gu','Guemon'),('In','Indenie_djuablin'),('Ka','Kabadougou'),('Na','Nawa'),('Lo','Loh_Djiboua'),('If',' Iffou'),('Mo','Moronou'),('Nz','Nzi'),('LM','La_Me'),('To','Tonkpi'),('Hs','Haut_Sassandra'),('Mr','Marahoué'),('Po','Poro'),('Tc','Tchologo'),('Ha','Hambol'),('Go','Gontougou'),('Sp','San_pedro'),('Sc','Sud_Comoe'),('Wo','Worodougou'))
    region=models.CharField(max_length=100,blank=False)
    departement=models.CharField(max_length=100,blank=False)
    sous_prefecture=models.CharField(max_length=100,blank=False)
    commune=models.CharField(max_length=100,blank=False)

    x=['district','region','departement','sous_prefecture','commune']

    objects=CustumerAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name','responsable','first_name']
    def __str__(self):
        return self.email

class Quartier(models.Model):
    district=models.CharField(max_length=100,blank=False,default='Abidjan')
    region=models.CharField(max_length=100,blank=False,default='Abidjan')
    departement=models.CharField(max_length=100,blank=False,default='Abidjan')
    sous_prefecture=models.CharField(max_length=100,blank=False,default='Abidjan')
    commune=models.CharField(max_length=100,blank=False)
    quartier=models.CharField(max_length=100,blank=False,default='Rue_12_Avenue_11')
    def __str__(self):
        return self.quartier

class Zone(models.Model):
    nomz=models.CharField(max_length=100,blank=False,primary_key=True)
    commune=models.CharField(max_length=100,blank=False,default='issa')
    q1=ArrayField(models.CharField(max_length=100))
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.nomz

class Affectation(models.Model):
    owner=models.CharField(max_length=100,blank=False,default='issa')
    agent=models.CharField(max_length=100,blank=False)
    quartier=models.ForeignKey(Zone,on_delete=models.CASCADE)
    create=models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.agent

# class Zone(models.Model):
#     quartier=models.CharField(max_length=100,blank=False,default='Rue_12_Avenue_11')
#     def __str__(self):
#         return self.quartier


class CritereChef(models.Model):
    sexeChef=ArrayField(models.FloatField())
    agechef=ArrayField(models.FloatField())
    nationalite=ArrayField(models.FloatField())
    niveauEtude=ArrayField(models.FloatField())
    maladie=ArrayField(models.FloatField())
    handicap=ArrayField(models.FloatField())
    occupations=ArrayField(models.FloatField())
    x="chefmenage"
    def __str__(self):
        return self.x

class CritereConj(models.Model):
    agec=ArrayField(models.FloatField())
    niveauEtude=ArrayField(models.FloatField())
    maladie=ArrayField(models.FloatField())
    handicap=ArrayField(models.FloatField())
    occupations=ArrayField(models.FloatField())
    x="conjoint"
    def __str__(self):
        return self.x

class CritereEnfant(models.Model):
    agec=ArrayField(models.FloatField())
    niveauEtude=ArrayField(models.FloatField())
    maladie=ArrayField(models.FloatField())
    handicap=ArrayField(models.FloatField())
    x="enfant"
    def __str__(self):
        return self.x
    
class CritereCharge(models.Model):
    agec=ArrayField(models.FloatField())
    niveauEtude=ArrayField(models.FloatField())
    maladie=ArrayField(models.FloatField())
    handicap=ArrayField(models.FloatField())
    occupations=ArrayField(models.FloatField())
    x="charge"
    def __str__(self):
        return self.x

class CritereCommodite(models.Model):
    eclairage=ArrayField(models.FloatField())
    cuisson=ArrayField(models.FloatField())
    aeaux=ArrayField(models.FloatField())
    ordure=ArrayField(models.FloatField())
    nombrep=ArrayField(models.FloatField())
    aisance=ArrayField(models.FloatField())
    loyer=ArrayField(models.FloatField())
    typelogement=ArrayField(models.FloatField())
    x="commodite"
    def __str__(self):
        return self.x

class CritereEquipement(models.Model):
    moyend=ArrayField(models.FloatField())
    equipee=ArrayField(models.FloatField())
    equipepo=ArrayField(models.FloatField())
    x="equipement"
    def __str__(self):
        return self.x

class CritereDeces(models.Model):
    agec=ArrayField(models.FloatField())
    
class CritereMenage(models.Model):
    moyenneage=ArrayField(models.FloatField())
    niveauEtudeM=ArrayField(models.FloatField())
    typeMenage=ArrayField(models.FloatField())
    occupations=ArrayField(models.FloatField())
    x="menage"
    def __str__(self):
        return self.x

class CritereHabitat(models.Model):
    ville=ArrayField(models.FloatField())
    quartier=ArrayField(models.FloatField())
    x="habitat"
    def __str__(self):
        return self.x

class CritereGeneral(models.Model):
    conditionvie=ArrayField(models.FloatField())
    conditionphy=ArrayField(models.FloatField())
    conditionoccup=ArrayField(models.FloatField())
    conditionnivee=ArrayField(models.FloatField())
    x="generale"
    def __str__(self):
        return self.x









    
