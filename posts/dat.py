from .models import*
from .serializers import*
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

from posts.indicateur import*

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


def Information2(request):
    if request.method=="GET":
        data1={}
        data2={}
        chef=Chef_menage.objects.filter(vulnerablePhy=True, vulnerableCondi=True,vulnerableEtude=True,vulnerableOccup=True)
        chefs=PostChefMSerializer(chef,context={'request': request},many=True)
        dataf=[dict(i) for i in chefs.data]
        idf=[i['id'] for i in dataf]
        for i in idf:
            dataF={}
            niveauE=[]
            comodite=[]
            equipsd=[]
            equipse=[]
            equipsa=[]
            ageE=[]
            niveauc=[]
            agec=[]
            occupationc=[]
            niveauco=[]
            ageco=[]
            occupationco=[]
            niveauER=[]
            occupationR=[]
            handicapR=[]
            maladieR=[]
            situationMR=[]
            ageCh=[]
            sexeC=[]
            imi=[]
            nat=[]
            moyenne_age=[]
            niveau_scolaire=[]
            condition=[]
            condition1=0
            condition2=0
            condition3=0
            condition4=0
            condition5=0
            condition6=0
            condition7=0
            occupationg=[]
            datas=[]
            nbr=0
            dataMoyenne=0
            data={}
            dataE={}
            dataC={}
            dataCo={}
            dataEq={}
            dataCc={}
            dataCo={}
            dataR={}
            hand=[]
            occup=[]
            nivo=[]
            condition=0
            condition2=0
            data['chefmenage']=[dict(s) for s in PostChefMSerializer(Chef_menage.objects.filter(id=i),context={'request': request},many=True).data]
            if data['chefmenage']:
                nbr=nbr+1
                for z in data['chefmenage']:
                    age=z['annee_naissance'].split("-")
                    ages=calculate_age(date(int(age[0]),int(age[1]),int(age[2])))
                    nationalites=z['nationalite']
                    sexes=z['sexes']
                    immigres=z['immigre']
                    villes=z['commune']
                    milieu_ru=z['milieu_r']
                    moyenne_age.append(ages)
                dataR['age']=ages
                dataR['nationalite']=["score","{}".format(nationalite(nationalites))]
                dataR['sexe']=["score","{}".format(sexesChef(sexes))]
                dataR['immigre']=["score","{}".format(immigre(immigres))]
                condition1=(immigre(immigres)+nationalite(nationalites)+sexesChef(sexes)+ageMenage(ages))/4
            data['recenser']=[dict(s) for s in RecensementS(Recenser.objects.filter(parent=i),context={'request': request},many=True).data]
            if data['recenser']:
                for z in data['recenser']:
                    niveau_etude=z['niveau_instruction']
                    occupation=z['occupation_actuelle']
                    handicaps=z['handicap']
                    situation_matrimoniale=z['situation_matrimoniale']
                    maladie=z['maladie']
                    handicapR.append(handicaps)
                    maladieR.append(maladie)
                    niveau_scolaire.append(niveau_etude)
                    occupationg.append(occupation)

                dataR['niveau']=["score","{}".format(niveau(niveau_etude))]
                dataR['occupation']=["score","{}".format(occupations(occupation))]
                dataR['handicap']=["score","{}".format(handicap(handicaps))]
                dataR['situation_matrimoniale']=["score","{}".format(situation_matr(situation_matrimoniale))]
                dataR['maladie']=["score","{}".format(maladies(maladie))]

            dataF['recenser']=dataR
            data['enfant']=[dict(s) for s in EnfantS(Enfant.objects.filter(parentf=i),context={'request': request},many=True).data]
            if data['enfant']:
                for z in data['enfant']:
                    nbr=nbr+1
                    age=z['annee_naissance'].split("-")
                    ages=calculate_age(date(int(age[0]),int(age[1]),int(age[2])))
                    niveau_etude=z['niveau_etude']
                    handica=z['handicap']

                    moyenne_age.append(ages)
                    handicapR.append(handica)
                    niveau_scolaire.append(niveau_etude)

                dataE['age']=["score","{}".format(handicap(handica))]
                dataE['niveau']=["score","{}".format(niveau(niveau_etude))]
                dataE['handicap']=["score","{}".format(handicap(handica))]
            dataF['Enfant']=dataE
            data['charge']=[dict(s) for s in PostChargeSerializer(Charge.objects.filter(parentg=i),context={'request': request},many=True).data]
            if data['charge']:
                for s in data['charge']:
                    nbr=nbr+1
                    age=s['annee_naissance'].split("-")
                    ages=calculate_age(date(int(age[0]),int(age[1]),int(age[2])))
                    niveau_etude=s['niveau_etude']
                    occupation=s['occupation']
                    handica=s['handicap']

                    occupationg.append(occupation)
                    handicapR.append(handica)
                    moyenne_age.append(ages)
                    niveau_scolaire.append(niveau_etude)

                dataC['age']=["score","{}".format(handicap(handica))]
                dataC['niveau']=["score","{}".format(niveau(niveau_etude))]
                dataC['occupation']=["score","{}".format(occupations(occupation))]
                dataC['handicap']=["score","{}".format(handicap(handica))]
            dataF['Charge']=dataC
            data['conjoint']=[dict(s) for s in PostConjointSerializer(Conjoint.objects.filter(idc=i),context={'request': request},many=True).data]
            if data['conjoint']:
                
                for x in data['conjoint']:
                    nbr=nbr+1
                    age=x['annee_naissance'].split("-")
                    ages=calculate_age(date(int(age[0]),int(age[1]),int(age[2])))
                    niveau_etude=x['niveau_etude']
                    occupation=x['occupation']
                    handica=x['handicap']

                    occupationg.append(occupation)
                    handicapR.append(handica)
                    moyenne_age.append(ages)
                    niveau_scolaire.append(niveau_etude)

                dataCo['age']=["score","{}".format(handicap(handica))]
                dataCo['niveau']=["score","{}".format(niveau(handica))]
                dataCo['occupation']=["score","{}".format(occupations(handica))]
                dataCo['handicap']=["score","{}".format(handicap(handica))]

            dataF['Conjoint']=dataCo
            data['equipement']=[dict(s) for s in EquipementS(Equipement.objects.filter(parente=i),context={'request': request},many=True).data]
            if data['equipement']:
                for x in data['equipement']:
                    moyen_deplacement=x['moyen_deplacement'].split("+")
                    equipement_electr=x['equipement_electr'].split("+")
                    equipement_audio=x['equipement_audio'].split("+")
                    proprietaires=x['proprietaire']
                    equipsd.append(moyen_deplacement)
                    equipse.append(equipement_electr)
                    equipsa.append(equipement_audio)
                datas.append(equipsd)
                datas.append(equipse)   
                datas.append(equipsa) 
                dataEq['moyen_deplacement']=["score","{}_{}".format(EquipementMenage(moyen_deplacement),len(moyen_deplacement))]
                dataEq['equipement_electr']=["score","{}_{}".format(EquipementMenage(equipement_electr),len(equipement_electr))]
                dataEq['equipement_audio']=["score","{}_{}".format(EquipementMenage(equipement_audio),len(equipement_audio))]
                dataEq['proprietaire']=["score","{}".format(proprietaire(proprietaires))]
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
                    natur_m=x['nature_mur']
                    natur_t=x['nature_toit']
                    natur_s=x['nature_sol']
                    comodite.append(eclairage)
                    comodite.append(nombre_piece)
                    comodite.append(typelogement)
                    comodite.append(lieu_aisance)
                    comodite.append(cuissons)
                    comodite.append(alimentation_eau)
                dataCc['eclairage']=["score","{}".format(eclairages(eclairage))]
                dataCc['nombre_piece']=["score","{}".format(logement1(nombre_piece))]
                dataCc['typelogement']=["score","{}".format(logement2(typelogement))]
                dataCc['lieu_aisance']=["score","{}".format(aisance(lieu_aisance))]
                dataCc['alimentation_eau']=["score","{}".format(eaux(alimentation_eau))]
                dataCc['cuisson']=["score","{}".format(combustible(cuissons))]
                condition6=eclairages(eclairage)+logement1(nombre_piece)+aisance(lieu_aisance)+eaux(alimentation_eau)+combustible(cuissons)
                condition7=condition6+logement2(typelogement)+ville(villes)+amanegement(villes)
            
            w=[]
            w.append(moyenne_age)
            w.append(niveau_scolaire)
            condition6=condition6+EducationMenage(w)
            condition8=condition6+condition1
            condition9=condition6+condition2
            condition10=condition6+condition3
            condition11=condition6+condition4
            condition12=condition6+condition5
            dataF['commodite']=dataCc
            dataF['moyenneOccupation']=(moyenneOccup(occupationg))
            dataF['moyenHandicap']=(moyenneHand(handicapR))
            dataF['moyenneNiveau']=moyenneNiveau(niveau_scolaire)
            dataF['moyenneage']=moyenneage(moyenne_age)
            dataF['EducationDuMenage']=EducationMenage(w)
            data['deces']=[dict(s) for s in DeceS(Deces.objects.filter(parentd=i),context={'request': request},many=True).data]
            if datas:
                dataF['MoyenneEquip']=MoyenneEquipement(datas)
            dataF["info_chef"]=condition1
            dataF["info_handic"]=handicapR
            dataF['info_occup']=occupationg
            dataF['info_condi1_log']=condition6
            dataF['info_condi2_typ_log']=condition7
            dataF['info_condi3_info_chef']=condition8
            dataF['info_condi4_info_hand']=condition9
            dataF['info_condi5_info_occu']=condition10
            dataF['info_condi6_prop']=condition11
            dataF['info_condi7_bien']=condition12
            dataF["nombre_personne"]=nbr

            if condition6>0:
                chef=Chef_menage.objects.get(id=i)
                chef.vulnerableCondi=False
                chef.save(update_fields=['vulnerableCondi'])
            if moyenneHand(handicapR)>0: 
                chef=Chef_menage.objects.get(id=i)
                chef.vulnerablePhy=False
                chef.save(update_fields=['vulnerablePhy'])
            if EducationMenage(w)>condition6:
                chef=Chef_menage.objects.get(id=i)
                chef.vulnerableEtude=False
                chef.save(update_fields=['vulnerableEtude'])
            if moyenneOccup(occupationg)>condition6:
                chef=Chef_menage.objects.get(id=i)
                chef.vulnerableOccup=False
                chef.save(update_fields=['vulnerableOccup'])

            data1["{}".format(i)]=data
            data2["{}".format(i)]=dataF
        return JsonResponse({"data2":data2, "status":status.HTTP_200_OK,"message":"liste des récensers"})

x="youtube.com/watch?v=Q4ua3E3vH58"

