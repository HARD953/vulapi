from custumer.models import Quartier
from custumer.serializers1 import*
from posts.critere.indicateur import handicap
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

class Individug(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Chef_menage.objects.filter(individu=True,commune=quartier).count()
                return JsonResponse(data)
            else:
                quartiers=QuartierSerializer(Quartier.objects.filter(commune=self.request.user.commune),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Chef_menage.objects.filter(individu=True,commune=self.request.user.commune,quartier=quartier).count()
                return JsonResponse(data)
        else:
            return JsonResponse({'message':'Personne'})


class Homme(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Chef_menage.objects.filter(individu=True,commune=quartier,sexes="M").count()
                return JsonResponse(data)
            else:
                quartiers=QuartierSerializer(Quartier.objects.filter(commune=self.request.user.commune),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Chef_menage.objects.filter(individu=True,commune=self.request.user.commune,quartier=quartier,sexes="M").count()
                return JsonResponse(data)
        else:
            return JsonResponse({'message':'Personne'})

class Femme(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Chef_menage.objects.filter(individu=True,commune=quartier,sexes="F").count()
                return JsonResponse(data)
            else:
                quartiers=QuartierSerializer(Quartier.objects.filter(commune=self.request.user.commune),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Chef_menage.objects.filter(individu=True,commune=self.request.user.commune,quartier=quartier,sexes="F").count()
                return JsonResponse(data)
        else:
            return JsonResponse({'message':'Personne'})


class Enfantg(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Enfant_R.objects.filter(commune=quartier).count()
                return JsonResponse(data)
            else:
                quartiers=QuartierSerializer(Quartier.objects.filter(commune=self.request.user.commune),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Enfant_R.objects.filter(commune=self.request.user.commune,quartier=quartier).count()
                return JsonResponse(data)
        else:
            return JsonResponse({'message':'Personne'})


class Enfant_F(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Enfant_R.objects.filter(commune=quartier,sexes="F").count()
                return JsonResponse(data)
            else:
                quartiers=QuartierSerializer(Quartier.objects.filter(commune=self.request.user.commune),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Enfant_R.objects.filter(commune=self.request.user.commune,quartier=quartier,sexes="F").count()
                return JsonResponse(data)
        else:
            return JsonResponse({'message':'Personne'})


class Enfant_H(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Enfant_R.objects.filter(commune=quartier,sexes="M").count()
                return JsonResponse(data)
            else:
                quartiers=QuartierSerializer(Quartier.objects.filter(commune=self.request.user.commune),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Enfant_R.objects.filter(commune=self.request.user.commune,quartier=quartier,sexes="H").count()
                return JsonResponse(data)
        else:
            return JsonResponse({'message':'Personne'})



class StatcircleEn(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                data1={}
                data1["handicap"]=Enfant_R.objects.filter(handicap=True).count()
                data1["descolariser"]=Enfant_R.objects.filter(scolariser=True).count()
                data1["pered"]=Enfant_R.objects.filter(pere=True).count()
                data1["mered"]=Enfant_R.objects.filter(mere=True).count()
                data1["battue"]=Enfant_R.objects.filter(battue=True).count()
                data1['Total']=Enfant_R.objects.all().count()
                data={}
                data["enfantR"]=data1
                return JsonResponse(data)
            else:
                data1={}
                data1["handicap"]=Enfant_R.objects.filter(handicap=True,commune=request.user.commune).count()
                data1["descolariser"]=Enfant_R.objects.filter(scolariser=True,commune=request.user.commune).count()
                data1["pered"]=Enfant_R.objects.filter(pere=True,commune=request.user.commune).count()
                data1["mered"]=Enfant_R.objects.filter(mere=True,commune=request.user.commune).count()
                data1["battue"]=Enfant_R.objects.filter(battue=True).count()
                data1['Total']=Enfant_R.objects.filter(commune=request.user.commune).count()
                data={}
                data["enfantR"]=data1
                return JsonResponse(data)
        else:
            return JsonResponse({'message':'Personne'})


class StatbarEn(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                data1={}
                data2={}
                data3={}
                data4={}
                data5={}
                for quartier in quartierT:
                    data1["{}".format(quartier)]=Enfant_R.objects.filter(handicap=True,commune=quartier).count()
                    data2["{}".format(quartier)]=Enfant_R.objects.filter(scolariser=True,commune=quartier).count()
                    data3["{}".format(quartier)]=Enfant_R.objects.filter(pere=True,commune=quartier).count()
                    data4["{}".format(quartier)]=Enfant_R.objects.filter(mere=True,commune=quartier).count()
                    data5["{}".format(quartier)]=Enfant_R.objects.filter(battue=True,commune=quartier).count()
                    data["handicap"]=data1
                    data["descolariser"]=data2
                    data["pered"]=data3
                    data["mered"]=data4
                    data["battue"]=data5
                return JsonResponse({"menage":data})
            else:
                quartiers=QuartierSerializer(Quartier.objects.filter(commune=self.request.user.commune),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                data1={}
                data2={}
                data3={}
                data4={}
                data5={}
                for quartier in quartierT:
                    data1["{}".format(quartier)]=Enfant_R.objects.filter(handicap=True,commune=request.user.commune,quartier=quartier).count()
                    data2["{}".format(quartier)]=Enfant_R.objects.filter(scolariser=True,commune=request.user.commune,quartier=quartier).count()
                    data3["{}".format(quartier)]=Enfant_R.objects.filter(pere=True,commune=request.user.commune,quartier=quartier).count()
                    data4["{}".format(quartier)]=Enfant_R.objects.filter(mere=True,commune=request.user.commune,quartier=quartier).count()
                    data5["{}".format(quartier)]=Enfant_R.objects.filter(battue=True,commune=quartier).count()
                    data["handicap"]=data1
                    data["descolariser"]=data2
                    data["pered"]=data3
                    data["mered"]=data4
                    data["battue"]=data5
                return JsonResponse({"menage":data})
        else:
            return JsonResponse({'message':'Personne'})






    
    