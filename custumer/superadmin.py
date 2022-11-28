from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from posts.models import*
from .serializers1 import*
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from posts.permissions import *
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
# Create your views here.

class WritePermission(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id==request.user



class ChefMenageList(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    filterset_fields=['district','region','departement']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.all()

class ChefMenageListd(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.all()

#Les Conjoint
class ConjointList(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Conjoint
    serializer_class=PostConjointSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['occupation','niveau_etude']
    def get_queryset(self):
        user = self.request.user
        return Conjoint.objects.all()

class ConjointListd(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Conjoint
    serializer_class=PostConjointSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['occupation','niveau_etude']
    def get_queryset(self):
        user = self.request.user
        return Conjoint.objects.all()

#Les Recensés
class RecenserListd(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Recenser
    serializer_class=RecensementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parent']
    def get_queryset(self):
        user = self.request.user
        return Recenser.objects.all()

class RecenserList(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Recenser
    serializer_class=RecensementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parent']
    def get_queryset(self):
        user = self.request.user
        return Recenser.objects.all()
    
#Les Enfants
class EnfantListd(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Enfant
    serializer_class=EnfantS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['ecolier','niveau_etude']
    def get_queryset(self):
        user = self.request.user
        return Enfant.objects.all()

class EnfantList(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Enfant
    serializer_class=EnfantS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['ecolier','niveau_etude']
    def get_queryset(self):
        user = self.request.user
        return Enfant.objects.all()

#Les commodites
class CommoditeListd(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Commodite
    serializer_class=CommoditeS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentc']
    def get_queryset(self):
        user = self.request.user
        return Commodite.objects.all()

class CommoditeList(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Commodite
    serializer_class=CommoditeS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentc']
    def get_queryset(self):
        user = self.request.user
        return Commodite.objects.all()

#Les equipements
class EquipementListd(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Equipement
    serializer_class=EquipementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['moyen_deplacement','equipement_electr','equipement_audio','statut_occupation']
    def get_queryset(self):
        user = self.request.user
        return Equipement.objects.all()


class EquipementList(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Equipement
    serializer_class=EquipementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['moyen_deplacement','equipement_electr','equipement_audio','statut_occupation']
    def get_queryset(self):
        user = self.request.user
        return Equipement.objects.all()

#Les deces
class DecesList(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Deces
    serializer_class=DeceS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentd']
    def get_queryset(self):
        user = self.request.user
        return Deces.objects.all()

class DecesListd(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Deces
    serializer_class=DeceS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentd']
    def get_queryset(self):
        user = self.request.user
        return Deces.objects.all()

#les charges
class ChargeList(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Charge
    serializer_class=PostChargeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentg']
    def get_queryset(self):
        user = self.request.user
        return Charge.objects.all()

class ChargeListd(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Charge
    serializer_class=PostChargeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentg']
    def get_queryset(self):
        user = self.request.user
        return Charge.objects.all()
        
    # def get(self,request,pk):
    #     try:
    #         affectations = Affecter.objects.get(pk=pk)
    #     except affectations.DoesNotExist:
    #         return HttpResponse(status=404)
    #     serializer = PostAffectationSerializer(affectations)
    #     return JsonResponse(serializer.data)

 