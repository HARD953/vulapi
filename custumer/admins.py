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

class ChefMenageLista(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.filter(commune=user.commune)

class ChefMenageListad(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.filter(commune=user.commune)

#Les Conjoint
class ConjointLista(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Conjoint
    serializer_class=PostConjointSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['occupation','niveau_etude']
    def get_queryset(self):
        user = self.request.user
        return Conjoint.objects.filter(commune=user.commune)

class ConjointListad(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Conjoint
    serializer_class=PostConjointSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['occupation','niveau_etude']
    def get_queryset(self):
        user = self.request.user
        return Conjoint.objects.filter(commune=user.commune)

#Les Recensés
class RecenserListad(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Recenser
    serializer_class=RecensementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parent']
    def get_queryset(self):
        user = self.request.user
        return Recenser.objects.all()

class RecenserLista(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Recenser
    serializer_class=RecensementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parent']
    def get_queryset(self):
        user = self.request.user
        return Recenser.objects.all()
    
#Les Enfants
class EnfantListad(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Enfant
    serializer_class=EnfantS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['ecolier','niveau_etude']
    def get_queryset(self):
        user = self.request.user
        return Enfant.objects.filter(commune=user.commune)

class EnfantLista(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Enfant
    serializer_class=EnfantS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['ecolier','niveau_etude']
    def get_queryset(self):
        user = self.request.user
        return Enfant.objects.filter(commune=user.commune)

#Les commodites
class CommoditeListad(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Commodite
    serializer_class=CommoditeS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parent']
    def get_queryset(self):
        user = self.request.user
        return Commodite.objects.all()

class CommoditeLista(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Commodite
    serializer_class=CommoditeS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parent']
    def get_queryset(self):
        user = self.request.user
        return Commodite.objects.all()

#Les equipements
class EquipementListad(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Equipement
    serializer_class=EquipementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['moyen_deplacement','equipement_electr','equipement_audio','statut_occupation']
    def get_queryset(self):
        user = self.request.user
        return Equipement.objects.all()


class EquipementLista(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Equipement
    serializer_class=EquipementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['moyen_deplacement','equipement_electr','equipement_audio','statut_occupation']
    def get_queryset(self):
        user = self.request.user
        return Equipement.objects.all()

#Les deces
class DecesLista(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Deces
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentd']
    def get_queryset(self):
        user = self.request.user
        return Deces.objects.all()

class DecesListad(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Deces
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentd']
    def get_queryset(self):
        user = self.request.user
        return Deces.objects.all()

#les charges
class ChargeLista(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Charge
    serializer_class=PostChargeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentg']
    def get_queryset(self):
        user = self.request.user
        return Charge.objects.filter(commune=user.commune)

class ChargeListad(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Charge
    serializer_class=PostChargeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['parentg']
    def get_queryset(self):
        user = self.request.user
        return Charge.objects.filter(commune=user.commune)

class Affecter(APIView):
    def post(self,request):
        message='Merci pour votre contribution:\n nous vous contacterons dans peut'
        data=request.data
        serializer = AffectaSerializer(data=data)
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.errors})




    # def get(self,request,pk):
    #     try:
    #         affectations = Affecter.objects.get(pk=pk)
    #     except affectations.DoesNotExist:
    #         return HttpResponse(status=404)
    #     serializer = PostAffectationSerializer(affectations)
    #     return JsonResponse(serializer.data)

 