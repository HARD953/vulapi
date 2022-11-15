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

class StatcircleMGeneral(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Chef_menage.objects.filter(menage=True,commune=quartier).count()
                return JsonResponse(data)
            else:
                quartiers=QuartierSerializer(Quartier.objects.filter(commune=self.request.user.commune),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['quartier'] for i in dataf]
                data={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=Chef_menage.objects.filter(menage=True,commune=self.request.user.commune,quartier=quartier).count()
                return JsonResponse(data)
        else:
            return JsonResponse({"message":"error"})
            
class StatcircleIGeneral(APIView):
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
            return JsonResponse({"message":"error"})

class StatGeneral(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                data={}
                data["TotalG"]=Chef_menage.objects.all().count()
                return JsonResponse(data)
            else:
                data={}
                data["Total"]=Chef_menage.objects.filter(commune=self.request.user.commune).count()
                return JsonResponse(data)
        else:
            return JsonResponse({"message":"error"})




    
    