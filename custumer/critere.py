from custumer.serializers1 import QuartierSerializer
from .serializersc import*
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from .models import *
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
from posts.permissions import*
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from posts.models import*
from posts.serializers import*
from rest_framework import status
from django.http import Http404

from rest_framework_simplejwt.tokens import RefreshToken

class CritereCh(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereChef
    serializer_class=MySerializerChef
    def get_queryset(self):
        return CritereChef.objects.all()

class CrudCh(generics.RetrieveUpdateDestroyAPIView):
    model=CritereChef
    permission_classes=[AllowAny]
    serializer_class=MySerializerChef
    def get_queryset(self):
        return CritereChef.objects.all()


class CritereCo(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereConj
    serializer_class=MySerializerConj
    def get_queryset(self):
        return CritereConj.objects.all()

class CrudCo(generics.RetrieveUpdateDestroyAPIView):
    model=CritereConj
    permission_classes=[AllowAny]
    serializer_class=MySerializerConj
    def get_queryset(self):
        return CritereConj.objects.all()

class CritereEn(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereEnfant
    serializer_class=MySerializerEnfant
    def get_queryset(self):
        return CritereEnfant.objects.all()

class CrudEn(generics.RetrieveUpdateDestroyAPIView):
    model=CritereEnfant
    permission_classes=[AllowAny]
    serializer_class=MySerializerEnfant
    def get_queryset(self):
        return CritereEnfant.objects.all()

class CritereCha(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereCharge
    serializer_class=MySerializerCharge
    def get_queryset(self):
        return CritereCharge.objects.all()

class CrudCha(generics.RetrieveUpdateDestroyAPIView):
    model=CritereCharge
    permission_classes=[AllowAny]
    serializer_class=MySerializerCharge
    def get_queryset(self):
        return CritereCharge.objects.all()

class CritereEq(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereEquipement
    serializer_class=MySerializerEquipement
    def get_queryset(self):
        return CritereEquipement.objects.all()

class CrudEq(generics.RetrieveUpdateDestroyAPIView):
    model=CritereEquipement
    permission_classes=[AllowAny]
    serializer_class=MySerializerEquipement
    def get_queryset(self):
        return CritereEquipement.objects.all()

class CritereCom(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereCommodite
    serializer_class=MySerializerCommodite
    def get_queryset(self):
        return CritereCommodite.objects.all()

class CrudCom(generics.RetrieveUpdateDestroyAPIView):
    model=CritereCharge
    permission_classes=[AllowAny]
    serializer_class=MySerializerCharge
    def get_queryset(self):
        return CritereCharge.objects.all()


class CritereDe(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereDeces
    serializer_class=MySerializerDeces
    def get_queryset(self):
        return CritereDeces.objects.all()

class CrudDe(generics.RetrieveUpdateDestroyAPIView):
    model=CritereDeces
    permission_classes=[AllowAny]
    serializer_class=MySerializerDeces
    def get_queryset(self):
        return CritereDeces.objects.all()


class CritereHa(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereHabitat
    serializer_class=MySerializerHabitat
    def get_queryset(self):
        return CritereHabitat.objects.all()

class CrudHa(generics.RetrieveUpdateDestroyAPIView):
    model=CritereHabitat
    permission_classes=[AllowAny]
    serializer_class=MySerializerHabitat
    def get_queryset(self):
        return CritereHabitat.objects.all()


class CritereGe(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereGeneral
    serializer_class=MySerializerGeneral
    def get_queryset(self):
        return CritereGeneral.objects.all()

class CrudGe(generics.RetrieveUpdateDestroyAPIView):
    model=CritereGeneral
    permission_classes=[AllowAny]
    serializer_class=MySerializerGeneral
    def get_queryset(self):
        return CritereGeneral.objects.all()


class CritereMe(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=CritereMenage
    serializer_class=MySerializerMenage
    def get_queryset(self):
        return CritereGeneral.objects.all()

class CrudMe(generics.RetrieveUpdateDestroyAPIView):
    model=CritereMenage
    permission_classes=[AllowAny]
    serializer_class=MySerializerMenage
    def get_queryset(self):
        return CritereMenage.objects.all()

class QuartierS(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    model=Quartier
    serializer_class=QuartierSerializer
    def get_queryset(self):
        return Quartier.objects.all()

class CrudCha(generics.RetrieveUpdateDestroyAPIView):
    model=CritereCharge
    permission_classes=[AllowAny]
    serializer_class=MySerializerCharge
    def get_queryset(self):
        return CritereCharge.objects.all()