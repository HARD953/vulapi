from posts.models import*
from posts.serializers import*
from django.http import HttpResponseGone,JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
import jwt,datetime
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from rest_framework import status
from django.http import Http404
from datetime import date
import pandas as pd

from posts.critere.indicateur import*
from ..critere.indicateurs import*

# def niveau_etude_menage()
# x="1998-07-21"
# z=x.split("-")
# print(calculate_age(date(int(z[0]), int(z[1]), int(z[2]))))
# data=2
# ni=[]
# if data:
#     for i in [1,2,3]:
#         ni.append(i)
# if data:
#     for s in [1,2,3]:
#         ni.append(s)
# print(ni)


def ana(request,pk):
    if request.method=="GET":
        dataR={}
        dataF={}
        dataE={}
        dataC={}
        dataCo={}
        dataEq={}
        dataCc={}
        aget=[]
        chef=Chef_menage.objects.filter(id=pk)
        chefs=PostChefMSerializer(chef,context={'request': request},many=True)
        dataf=[dict(i) for i in chefs.data]
        idf=[i['id'] for i in dataf]
        for i in idf:
            data={}
            data['chefmenage']=[dict(s) for s in PostChefMSerializer(Chef_menage.objects.filter(id=i),context={'request': request},many=True).data]
            if data['chefmenage']:
                for z in data['chefmenage']:
                    age=z['annee_naissance'].split("-")
                    ages=calculate_age(date(int(age[0]),int(age[1]),int(age[2])))
                    aget.append(ages)
                dataR['age']=ages
            data['recenser']=[dict(s) for s in RecensementS(Recenser.objects.filter(parent=i),context={'request': request},many=True).data]
            if data['recenser']:
                for z in data['recenser']:
                    niveau_etude=z['niveau_instruction']
                    occupation=z['occupation_actuelle']
                    handicaps=z['handicap']
                    situation_matrimoniale=z['situation_matrimoniale']
                    maladie=z['maladie']

                dataR['niveau']="{}".format(niveau_etude)
                dataR['occupation']="{}".format(occupation)
                dataR['handicap']="{}".format(handicaps)
                dataR['maladie']="{}".format(maladie)
            dataF['recenser']=dataR
            data['enfant']=[dict(s) for s in EnfantS(Enfant.objects.filter(parentf=i),context={'request': request},many=True).data]
            dataF['nombre_enfant']=len([dict(s) for s in EnfantS(Enfant.objects.filter(parentf=i),context={'request': request},many=True).data])
            if data['enfant']:
                ag=[]
                ni=[]
                ha=[]
                for z in data['enfant']:
                    age=z['annee_naissance'].split("-")
                    ages=calculate_age(date(int(age[0]),int(age[1]),int(age[2])))
                    niveau_etude=z['niveau_etude']
                    handica=z['handicap']
                    ag.append(ages)
                    ni.append(niveau_etude)
                    ha.append(handica)
                dataE['age']=ag
                dataE['niveau']=ni
                dataE['handicap']=ha
            dataF['Enfant']=dataE
            data['charge']=[dict(s) for s in PostChargeSerializer(Charge.objects.filter(parentg=i),context={'request': request},many=True).data]
            dataF['nombre_charge']=len([dict(s) for s in PostChargeSerializer(Charge.objects.filter(parentg=i),context={'request': request},many=True).data])
            if data['charge']:
                ag=[]
                ni=[]
                ha=[]
                oc=[]
                for s in data['charge']:
                    age=s['annee_naissance'].split("-")
                    ages=calculate_age(date(int(age[0]),int(age[1]),int(age[2])))
                    niveau_etude=s['niveau_etude']
                    occupation=s['occupation']
                    handica=s['handicap']
                    ag.append(ages)
                    ni.append(niveau_etude)
                    ha.append(handica)
                    oc.append(occupation)
                dataC['age']=ag
                dataC['niveau']=ni
                dataC['handicap']=ha
                dataC['occupation']=oc
            dataF['Charge']=dataC
            data['conjoint']=[dict(s) for s in PostConjointSerializer(Conjoint.objects.filter(idc=i),context={'request': request},many=True).data]
            dataF['nombre_conjoint']=len([dict(s) for s in PostConjointSerializer(Conjoint.objects.filter(idc=i),context={'request': request},many=True).data])
            if data['conjoint']:
                ag=[]
                ni=[]
                ha=[]
                oc=[]
                for x in data['conjoint']:
                    age=x['annee_naissance'].split("-")
                    ages=calculate_age(date(int(age[0]),int(age[1]),int(age[2])))
                    niveau_etude=x['niveau_etude']
                    occupation=x['occupation']
                    handica=x['handicap']
                    ag.append(ages)
                    ni.append(niveau_etude)
                    ha.append(handica)
                    oc.append(occupation)
                dataCo['age']=ag
                dataCo['niveau']=ni
                dataCo['handicap']=ha
                dataCo['occupation']=oc
            dataF['Conjoint']=dataCo
            data['equipement']=[dict(s) for s in EquipementS(Equipement.objects.filter(parente=i),context={'request': request},many=True).data]
            if data['equipement']:
                for x in data['equipement']:
                    moyen_deplacement=x['moyen_deplacement'].split("+")
                    equipement_electr=x['equipement_electr'].split("+")
                    equipement_audio=x['equipement_audio'].split("+")
                    proprietaires=x['proprietaire']
                dataEq['moyen_deplacement']=moyen_deplacement
                dataEq['equipement_electr']=equipement_electr
                dataEq['equipement_audio']=equipement_audio
                dataEq['proprietaire']=proprietaires
            dataF['equipement']=dataEq
            data['commodite']=[dict(s) for s in CommoditeS(Commodite.objects.filter(parentc=i),context={'request': request},many=True).data]
            if data['commodite']:
                for x in data['commodite']:
                    nombre_piece=x['nombre_piece']
                    typelogement=x['typelogement']
                    alimentation_eau=x['alimentation_eau']
                    eclairage=x['eclairage']
                    lieu_aisance=x['lieu_aisance']
                    cuissons=x['cuisson']
                dataCc['eclairage']="{}".format(eclairage)
                dataCc['nombre_piece']="{}".format(nombre_piece)
                dataCc['typelogement']="{}".format(typelogement)
                dataCc['lieu_aisance']="{}".format(lieu_aisance)
                dataCc['alimentation_eau']="{}".format(alimentation_eau)
                dataCc['cuisson']="{}".format(cuissons)
            dataF['commodite']=dataCc
        return JsonResponse(dataF)

