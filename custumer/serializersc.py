from dataclasses import field
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class MySerializerChef(serializers.ModelSerializer):
    class Meta:
        model=CritereChef
        fields='__all__'

class MySerializerConj(serializers.ModelSerializer):
    class Meta:
        model=CritereConj
        fields='__all__'

class MySerializerEnfant(serializers.ModelSerializer):
    class Meta:
        model=CritereEnfant
        fields='__all__'

class MySerializerCharge(serializers.ModelSerializer):
    class Meta:
        model=CritereCharge
        fields='__all__'

class MySerializerEquipement(serializers.ModelSerializer):
    class Meta:
        model=CritereEquipement
        fields='__all__'

class MySerializerCommodite(serializers.ModelSerializer):
    class Meta:
        model=CritereCommodite
        fields='__all__'

class MySerializerDeces(serializers.ModelSerializer):
    class Meta:
        model=CritereDeces
        fields='__all__'

class MySerializerHabitat(serializers.ModelSerializer):
    class Meta:
        model=CritereHabitat
        fields='__all__'

class MySerializerMenage(serializers.ModelSerializer):
    class Meta:
        model=CritereMenage
        fields='__all__'

class MySerializerGeneral(serializers.ModelSerializer):
    class Meta:
        model=CritereGeneral
        fields='__all__'
