from dataclasses import field
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    list_chef_menage = serializers.HyperlinkedRelatedField(many=True, view_name='chef_menage-detail',read_only=True)
    list_equipement = serializers.HyperlinkedRelatedField(many=True, view_name='equipement-detail',read_only=True)
    list_commodite = serializers.HyperlinkedRelatedField(many=True, view_name='commodite-detail',read_only=True)
    list_enfant = serializers.HyperlinkedRelatedField(many=True, view_name='enfant-detail',read_only=True)
    list_deces = serializers.HyperlinkedRelatedField(many=True, view_name='deces-detail',read_only=True)
    list_conjoint = serializers.HyperlinkedRelatedField(many=True, view_name='conjoint-detail',read_only=True)
    list_recenser = serializers.HyperlinkedRelatedField(many=True, view_name='recenser-detail',read_only=True)
    list_charge = serializers.HyperlinkedRelatedField(many=True, view_name='charge-detail',read_only=True)
    enfant_rue=serializers.HyperlinkedRelatedField(many=True, view_name='enfant-rue',read_only=True)
    owner = serializers.ReadOnlyField(source='owner.user_name')
    class Meta:
        model = NewUser
        fields=['id','user_name','email','responsable','first_name','last_name','password','adresse','about_me','owner','is_agent','is_active','is_staff','list_chef_menage','list_equipement','list_commodite','list_enfant','list_deces','list_charge','list_conjoint','list_recenser','enfant_rue','district','region','departement','sous_prefecture','commune','last_login','updated_at','profile_image']
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance =self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class AdminSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user_name')
    class Meta:
        model = NewUser
        fields=['id','email','user_name','responsable','password','commune','first_name','last_name','adresse','about_me','is_user','owner','is_active','is_staff','last_login','profile_image']
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance =self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class SuperAdminSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user_name')
    class Meta:
        model = NewUser
        fields=['id','email','user_name','responsable','commune','first_name','last_name','adresse','about_me','is_active','is_staff','is_superuser','owner','last_login','updated_at','profile_image']
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance =self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class GeneraleSerialiser(serializers. HyperlinkedModelSerializer):
    class Meta:
        model = NewUser
        fields=['id','start_date','responsable','email','user_name','commune','first_name','last_name','adresse','about_me','is_user','is_superuser','is_agent','is_active','is_staff','profile_image','create','last_login','updated_at']
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance =self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        

