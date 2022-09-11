from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from posts.permissions import *
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
# Create your views here.
from rest_framework import status


class WritePermission(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id==request.user

class ChefMenageList(generics.ListCreateAPIView):
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.filter(owner1=user)
    def perform_create(self, serializer):
        serializer.save(owner1=self.request.user)

class ChefMenageDetail(generics.RetrieveUpdateDestroyAPIView):
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.filter(owner1=user)
    def perform_create(self, serializer):
        serializer.save(owner1=self.request.user)

#Les Conjoint
class ConjointList(generics.ListCreateAPIView):
    model=Conjoint
    serializer_class=PostConjointSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Conjoint.objects.filter(owner2=user)
    def perform_create(self, serializer):
        serializer.save(owner2=self.request.user)
  
class ConjointDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    model=Conjoint
    serializer_class=PostConjointSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Conjoint.objects.filter(owner2=user)
    def perform_create(self, serializer):
        serializer.save(owner2=self.request.user)

#Les Recensés
class RecenserList(generics.ListCreateAPIView):
    model=Recenser
    serializer_class=RecensementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Recenser.objects.filter(owner3=user)
    def perform_create(self, serializer):
        serializer.save(owner3=self.request.user)
  
class RecenserDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    model=Recenser
    serializer_class=RecensementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Recenser.objects.filter(owner3=user)
    def perform_create(self, serializer):
        serializer.save(owner3=self.request.user)

#Les Enfants
class EnfantList(generics.ListCreateAPIView):
    model=Enfant
    serializer_class=EnfantS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Enfant.objects.filter(owner4=user)
    def perform_create(self, serializer):
        serializer.save(owner4=self.request.user)
  
class EnfantDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    model=Enfant
    serializer_class=EnfantS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Enfant.objects.filter(owner4=user)
    def perform_create(self, serializer):
        serializer.save(owner4=self.request.user)

#Les commodites
class CommoditeList(generics.ListCreateAPIView):
    model=Commodite
    serializer_class=CommoditeS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Commodite.objects.filter(owner5=user)
    def perform_create(self, serializer):
        serializer.save(owner5=self.request.user)
  
class CommoditeDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    model=Commodite
    serializer_class=CommoditeS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Commodite.objects.filter(owner5=user)
    def perform_create(self, serializer):
        serializer.save(owner5=self.request.user)

#Les equipements
class EquipementList(generics.ListCreateAPIView):
    model=Equipement
    serializer_class=EquipementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Equipement.objects.filter(owner6=user)
    def perform_create(self, serializer):
        serializer.save(owner6=self.request.user)
  
class EquipementDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    model=Equipement
    serializer_class=EquipementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Equipement.objects.filter(owner6=user)
    def perform_create(self, serializer):
        serializer.save(owner6=self.request.user)

#Les deces
class DecesList(generics.ListCreateAPIView):
    model=Deces
    serializer_class=DeceS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Deces.objects.filter(owner7=user)
    def perform_create(self, serializer):
        serializer.save(owner7=self.request.user)
  
class DecesDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    model=Deces
    serializer_class=DeceS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Deces.objects.filter(owner7=user)
    def perform_create(self, serializer):
        serializer.save(owner7=self.request.user)

#les charges
class ChargeList(generics.ListCreateAPIView):
    model=Charge
    serializer_class=PostChargeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Charge.objects.filter(owner8=user)
    def perform_create(self, serializer):
        serializer.save(owner8=self.request.user)

class EnfantRList(generics.ListCreateAPIView):
    model=Enfant_R
    serializer_class=PostEnfantRSerializer
    def get_queryset(self):
        user = self.request.user
        return Enfant_R.objects.filter(owner9=user)
    def perform_create(self, serializer):
        serializer.save(owner9=self.request.user)

class EnfantRDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    model=Enfant_R
    serializer_class=PostEnfantRSerializer
    def get_queryset(self):
        user = self.request.user
        return Enfant_R.objects.filter(owner9=user)
    def perform_create(self, serializer):
        serializer.save(owner9=self.request.user)
  
class ChargeDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    model=Charge
    serializer_class=PostChargeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Charge.objects.filter(owner8=user)
    def perform_create(self, serializer):
        serializer.save(owner8=self.request.user)

class ListRecenser(generics.ListAPIView):
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.filter(owner=user)


class RecensementView(APIView):        
    def post(self,request):
        data=request.data
        if data['Chef_menage']:
            for chef_menage in data['chef_menage']:
                serializerche = PostChefMSerializer(data=chef_menage)
                if serializerche.is_valid():
                    serializerche.save()
        if data['Conjoint']:
            for conjoint in data['Conjoint']:
                serializerco = PostConjointSerializer(data=conjoint)
                if serializerco.is_valid():
                    serializerco.save()
        if data['Recenser']:
            for recenser in data['Recenser']:
                serializerr = RecensementS(data=recenser)
                if serializerr.is_valid():
                    serializerr.save()
        if data['Enfant']:
            for enfant in data['Enfant']:
                serializere=EnfantS(data=enfant)
                if serializere.is_valid():
                    serializere.save()
        if data['Charge']:
            for charge in data['Charge']:
                serializerch=PostChargeSerializer(data=charge)
                if serializerch.is_valid():
                    serializerch.save()
        if data['Commodite']:
            for commodite in data['Commodite']:
                serializerc=CommoditeS(data=commodite)
                if serializerc.is_valid():
                    serializerc.save()
        if data['Equipement']:
            for equipement in data['Equipement']:
                serializereq=EquipementS(data=equipement)
                if serializereq.is_valid():
                    serializereq.save()
        return Response(status=status.HTTP_400_BAD_REQUEST)

class RecensementEnfent(APIView):
    def post(self,request):
        data=self.request.data
        serializer = PostEnfantRSerializer(data=data)
        message='Insertion Done'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Test1View(APIView):
    def post(self,request):
        data=self.request.data
        if data['test1']:
            serializer = Tes1Serializer(data=data['test1'])
            message='Insertion Done'
            if serializer.is_valid():
                serializer.save()
                print("reuissi1")
        if data['test2']:
            serializer1 = Tes2Serializer(data=data['test2'])
            print(data['test2'])
            message='Insertion Done'
            if serializer1.is_valid():
                serializer1.save()
                print("reuissi2")          
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Test2View(APIView):
    def post(self,request):
        data=self.request.data
        serializer = Tes2Serializer(data=data)
        message='Insertion Done'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            


    # def get(self,request,pk):
    #     try:
    #         affectations = Affecter.objects.get(pk=pk)
    #     except affectations.DoesNotExist:
    #         return HttpResponse(status=404)
    #     serializer = PostAffectationSerializer(affectations)
    #     return JsonResponse(serializer.data)

 