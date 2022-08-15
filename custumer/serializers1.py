from rest_framework import serializers
from posts.models import *
from .models import*

class AffectaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affectation
        fields = '__all__'


class PostChefMSerializer(serializers.HyperlinkedModelSerializer):
    owner1 = serializers.ReadOnlyField(source='owner1.user_name')
    class Meta:
        model = Chef_menage
        fields=['owner1','id','url','nom','prenom','annee_naissance','lieu_de_naissance','nationalite','numero_cni','sexes','ethnie','numero','type_menage','nombre_enfant','nombre_enfant_v','nom_personne_charge','immigre','district','region','departement','sous_prefecture','commune','milieu_r','quartier','date_depart','motif','age_depart','migrant','lieu_residence_a','annee_deplace','intention_ret']

class PostConjointSerializer(serializers.HyperlinkedModelSerializer):
    owner2 = serializers.ReadOnlyField(source='owner2.user_name')
    class Meta:
        model = Conjoint
        fields=['owner2','id','url','annee_naissance','sexes','niveau_etude','occupation','idc']

class RecensementS(serializers.HyperlinkedModelSerializer):
    owner3 = serializers.ReadOnlyField(source='owner3.user_name')
    class Meta:
        model = Recenser
        fields=['url','id','branche_activite','situation_occupation','occupation_actuelle','status_occupation','niveau_instruction','alphabetisation','survie_de_pere','survie_de_mere','handicap','religion','parent','owner3','situation_matrimoniale']

class EnfantS(serializers.HyperlinkedModelSerializer):
    owner4 = serializers.ReadOnlyField(source='owner4.user_name')
    class Meta:
        model = Enfant
        fields=['owner4','id','url','annee_naissance','sexes','parentf','niveau_etude']

class CommoditeS(serializers.HyperlinkedModelSerializer):
    owner5 = serializers.ReadOnlyField(source='owner5.user_name')
    class Meta:
        model = Commodite
        fields =['owner5','id','url','loyer','evacuation_eau','evacuation_ordure','cuisson','eclairage','temps_acces_eau','parentc','nombre_piece','nombre_piece_dormir','nature_mur','nature_toit','lieu_aisance','nature_sol','alimentation_eau']

class EquipementS(serializers.HyperlinkedModelSerializer):
    owner6 = serializers.ReadOnlyField(source='owner6.user_name')
    class Meta:
        model = Equipement
        fields =['owner6','id','url','parente','moyen_deplacement','equipement_electr','equipement_audio','statut_occupation']

class DeceS(serializers.HyperlinkedModelSerializer):
    owner7 = serializers.ReadOnlyField(source='owner7.user_name')
    class Meta:
        model = Deces
        fields =['owner7','id','url','parentd','annee_deces','sexesd']

class PostChargeSerializer(serializers.HyperlinkedModelSerializer):
    owner8 = serializers.ReadOnlyField(source='owner8.user_name')
    class Meta:
        model = Charge
        fields=['owner8','id','url','annee_naissance','immigre','intention_ret','parentg','sexesd','niveau_etude','occupation']
