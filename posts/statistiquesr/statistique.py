from custumer.models import Quartier
from custumer.serializers1 import*
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

class StatcircleM(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if request.user.is_superuser:
                data1={}
                data1["physique"]=Chef_menage.objects.filter(vulnerablePhy=True,menage=True).count()
                data1["condition"]=Chef_menage.objects.filter(vulnerableCondi=True,menage=True).count()
                data1["etude"]=Chef_menage.objects.filter(vulnerableEtude=True,menage=True).count()
                data1["occupation"]=Chef_menage.objects.filter(vulnerableOccup=True,menage=True).count()
                data={}
                data["menage"]=data1
                return JsonResponse(data)
            else:
                data1={}
                data1["physique"]=Chef_menage.objects.filter(vulnerablePhy=True,menage=True,commune=request.user.commune).count()
                data1["condition"]=Chef_menage.objects.filter(vulnerableCondi=True,menage=True,commune=request.user.commune).count()
                data1["etude"]=Chef_menage.objects.filter(vulnerableEtude=True,menage=True,commune=request.user.commune).count()
                data1["occupation"]=Chef_menage.objects.filter(vulnerableOccup=True,menage=True,commune=request.user.commune).count()
                data={}
                data["menage"]=data1
                return JsonResponse(data)
        else:
            return JsonResponse({'message':'Personne'})


def statcircleI(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            data={}
            data1={}
            if request.user.is_superuser:
                data1["physique"]=Chef_menage.objects.filter(vulnerablePhy=True,individu=True).count()
                data1["condition"]=Chef_menage.objects.filter(vulnerableCondi=True,individu=True).count()
                data1["etude"]=Chef_menage.objects.filter(vulnerableEtude=True,individu=True).count()
                data1["occupation"]=Chef_menage.objects.filter(vulnerableOccup=True,individu=True).count()
                data={}
                data["individu"]=data1
                return JsonResponse(data)
            else:
                data1["physique"]=Chef_menage.objects.filter(vulnerablePhy=True,individu=True,commune=request.user.commune).count()
                data1["condition"]=Chef_menage.objects.filter(vulnerableCondi=True,individu=True,commune=request.user.commune).count()
                data1["etude"]=Chef_menage.objects.filter(vulnerableEtude=True,individu=True,commune=request.user.commune).count()
                data1["occupation"]=Chef_menage.objects.filter(vulnerableOccup=True,individu=True,commune=request.user.commune).count()
                data["individu"]=data1
                return JsonResponse(data)
        else:
            return JsonResponse({'message':'Personne'})


def statbarM(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            if request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                data1={}
                data2={}
                data3={}
                data4={}
                for quartier in quartierT:
                    data1["{}".format(quartier)]=Chef_menage.objects.filter(vulnerablePhy=True,menage=True,commune=quartier).count()
                    data2["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableCondi=True,menage=True,commune=quartier).count()
                    data3["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableEtude=True,menage=True,commune=quartier).count()
                    data4["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableOccup=True,menage=True,commune=quartier).count()
                    data["physique"]=data1
                    data["condition"]=data2
                    data["etude"]=data3
                    data["sans-emploi"]=data4
                return JsonResponse({"menage":data})
            else:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                data1={}
                data2={}
                data3={}
                data4={}
                for quartier in quartierT:
                    data1["{}".format(quartier)]=Chef_menage.objects.filter(vulnerablePhy=True,menage=True,commune=request.user.commune,quartier=quartier).count()
                    data2["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableCondi=True,menage=True,commune=request.user.commune,quartier=quartier).count()
                    data3["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableEtude=True,menage=True,commune=request.user.commune,quartier=quartier).count()
                    data4["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableOccup=True,menage=True,commune=request.user.commune,quartier=quartier).count()
                    data["physique"]=data1
                    data["condition"]=data2
                    data["etude"]=data3
                    data["sans-emploi"]=data4
                return JsonResponse({"menage":data})
        else:
            return JsonResponse({'message':'Personne'})

def statbarI(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            if request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                data1={}
                data2={}
                data3={}
                data4={}
                for quartier in quartierT:
                    data1["{}".format(quartier)]=Chef_menage.objects.filter(vulnerablePhy=True,individu=True,commune=quartier).count()
                    data2["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableCondi=True,individu=True,commune=quartier).count()
                    data3["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableEtude=True,individu=True,commune=quartier).count()
                    data4["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableOccup=True,individu=True,commune=quartier).count()
                    data["physique"]=data1
                    data["condition"]=data2
                    data["etude"]=data3
                    data["sans-emploi"]=data4
                return JsonResponse({"individu":data})
            else:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                data1={}
                data2={}
                data3={}
                data4={}
                for quartier in quartierT:
                    data1["{}".format(quartier)]=Chef_menage.objects.filter(vulnerablePhy=True,individu=True,commune=request.user.commune,quartier=quartier).count()
                    data2["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableCondi=True,individu=True,commune=request.user.commune,quartier=quartier).count()
                    data3["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableEtude=True,individu=True,commune=request.user.commune,quartier=quartier).count()
                    data4["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableOccup=True,individu=True,commune=request.user.commune,quartier=quartier).count()
                    data["physique"]=data1
                    data["condition"]=data2
                    data["etude"]=data3
                    data["sans-emploi"]=data4
                return JsonResponse({"individu":data})
        return JsonResponse({'message':'Personne'})

def statevaluation(request,slug,slug2):
    if request.method=="GET":
        data={}
        data["physique"]=Chef_menage.objects.filter(vulnerablePhy=True,individu=True,commune=slug,quartier=slug2).count()
        data["condition"]=Chef_menage.objects.filter(vulnerableCondi=True,individu=True,commune=slug,quartier=slug2).count()
        data["etude"]=Chef_menage.objects.filter(vulnerableEtude=True,individu=True,commune=slug,quartier=slug2).count()
        data["occupation"]=Chef_menage.objects.filter(vulnerableOccup=True,individu=True,commune=slug,quartier=slug2).count()
        return JsonResponse(data)
    else:
        return JsonResponse({'message':'Personne'})

# def statbar(request,slug,slug2):
#     if request.method=="GET":
#         quartier=Quartier.objects.all()
#         data={}
#         for quartier in quartiers:
#             data["{}".format(quartier)]=Chef_menage.objects.filter(vulnerablePhy=True,individu=True,commune=slug,quartier=quartier).count()
#             data["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableCondi=True,individu=True,commune=slug,quartier=quartier).count()
#             data["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableEtude=True,individu=True,commune=slug,quartier=quartier).count()
#             data["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableOccup=True,individu=True,commune=slug,quartier=quartier).count()
#         return JsonResponse(data)
#     else:
#         return Response({'message':'Personne'})

# def statmenage(request,slug,slug2):
#     if request.method=="GET":
#         quartier=Quartier.objects.all()
#         data={}
#         for quartier in quartiers:
#             data["{}".format(quartier)]=Chef_menage.objects.filter(vulnerablePhy=True,menage=True,commune=slug,quartier=quartier).count()
#             data["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableCondi=True,menage=True,commune=slug,quartier=quartier).count()
#             data["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableEtude=True,menage=True,commune=slug,quartier=quartier).count()
#             data["{}".format(quartier)]=Chef_menage.objects.filter(vulnerableOccup=True,menage=True,commune=slug,quartier=quartier).count()
#         return JsonResponse(data)
#     else:
#         return Response({'message':'Personne'})



    
    