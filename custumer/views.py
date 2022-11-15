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
from .serializers1 import *
import requests
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class CreateAgent(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                dons=NewUser.objects.filter(is_agent=True)
                serializer=GeneraleSerialiser(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
            else:
                dons=NewUser.objects.filter(commune=self.request.user.commune,is_agent=True)
                serializer=GeneraleSerialiser(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})
            
    def post(self,request):
        message='Enregistrement reussi'
        data=self.request.data
        if data['is_staff']=="is_staff":
            data['is_staff']=True
        else:
            data['is_staff']=False

        if data['is_active']=="is_active":
            data['is_active']=True
        else:
            data['is_active']=False
    
        if data['is_agent']=="is_agent":
            data['is_agent']=True
        else:
            data['is_agent']=False

        data['responsable']=self.request.user.user_name
        
        serializer = UserSerializer(data=data)
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.errors})

class CrudAgent(APIView):
    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GeneraleSerialiser(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GeneraleSerialiser(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CreateAdmin(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                dons=NewUser.objects.filter(is_user=True)
                serializer=GeneraleSerialiser(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
            else:
                dons=NewUser.objects.filter(is_user=True,commune=self.request.user.commune)
                serializer=GeneraleSerialiser(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

    def post(self,request):
        message='Enregistrement reussi'
        data=self.request.data
        if data['is_staff']=="is_staff":
            data['is_staff']=True
        else:
            data['is_staff']=True

        if data['is_active']=="is_active":
            data['is_active']=True
        else:
            data['is_active']=True
    
        if data['is_user']=="is_user":
            data['is_user']=True
        else:
            data['is_user']=True

        data['responsable']=self.request.user.user_name

        serializer = AdminSerializer(data=data)
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.errors})

class CrudAdmin(APIView):
    permission_classes=[IsSuperAdminAuthenticated]
    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GeneraleSerialiser(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GeneraleSerialiser(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateSuperAdmin(APIView):
    permission_classes=[IsSuperAdminAuthenticated]
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                dons=NewUser.objects.filter(is_superuser=True)
                serializer=GeneraleSerialiser(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
            else:
                dons=NewUser.objects.filter(is_superuser=True,commune=self.request.user.commune)
                serializer=GeneraleSerialiser(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})
    
    def post(self,request):
        message='Enregistrement reussi'
        data=self.request.data
        if data['is_staff']=="is_staff":
            data['is_staff']=True
        else:
            data['is_staff']=False

        if data['is_active']=="is_active":
            data['is_active']=True
        else:
            data['is_active']=False
    
        if data['is_superuser']=="is_superuser":
            data['is_superuser']=True
        else:
            data['is_superuser']=False

        data['responsable']=self.request.user.user_name

        serializer = SuperAdminSerializer(data=data)
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.errors})


class CrudSuperadmin(APIView):
    permission_classes=[IsSuperAdminAuthenticated]
    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GeneraleSerialiser(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GeneraleSerialiser(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#How make to connect when we use token jwt

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DetailConecter(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        if self.request.user.is_authenticated:
            dons=NewUser.objects.filter(user_name=self.request.user.user_name)
            serializer=GeneraleSerialiser(dons, many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST})

class DetaSuperadmin(APIView):
    permission_classes=[AllowAny]
    def get(self,request,slug):
        chef=NewUser.objects.filter(email=slug,is_superuser=True)
        chefs=[dict(i) for i in GeneraleSerialiser(chef,context={'request': request},many=True).data]
        data={}
        data['superadmin']=[dict(i) for i in GeneraleSerialiser(chef,context={'request': request},many=True).data]
        data['adminagent']=NewUser.objects.filter(responsable=chefs[0]["user_name"]).count()
        return JsonResponse({'chefs':data})

class DetaAdmin(APIView):
    permission_classes=[AllowAny]
    def get(self,request,slug):
        chef=NewUser.objects.filter(email=slug,is_user=True)
        chefs=[dict(i) for i in GeneraleSerialiser(chef,context={'request': request},many=True).data]
        data={}
        data['admin']=[dict(i) for i in GeneraleSerialiser(chef,context={'request': request},many=True).data]
        data['agentcree']=NewUser.objects.filter(is_agent=True,responsable=chefs[0]["user_name"]).count()
        return JsonResponse({'chefs':data})

class DetaAgent(APIView):
    permission_classes=[AllowAny]
    def get(self,request,slug):
        chef=NewUser.objects.filter(email=slug,is_agent=True)
        chefs=[dict(i) for i in GeneraleSerialiser(chef,context={'request': request},many=True).data]
        dataf=[dict(i) for i in chefs]
        idf=[i['id'] for i in dataf]
        data={}
        data['agent']=[dict(i) for i in GeneraleSerialiser(chef,context={'request': request},many=True).data]
        data['personneR']=(Chef_menage.objects.filter(owner1=idf[0])).count()
        data['enfantR']=(Enfant_R.objects.filter(owner1=idf[0])).count()
        data['individu']=(Chef_menage.objects.filter(owner1=idf[0],individu=True)).count()
        data['menage']=(Chef_menage.objects.filter(owner1=idf[0],menage=True)).count()
        data['vulnerable_physique']=(Chef_menage.objects.filter(owner1=idf[0],vulnerablePhy=True)).count()
        data['vulnerable_conditionv']=(Chef_menage.objects.filter(owner1=idf[0],vulnerableCondi=True)).count()
        data['vulnerable_etude']=(Chef_menage.objects.filter(owner1=idf[0],vulnerableEtude=True)).count()
        data['vulnerable_sansE']=(Chef_menage.objects.filter(owner1=idf[0],vulnerableOccup=True)).count()
        return JsonResponse({'data':data})

class Affecter(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                dons=Affectation.objects.all()
                serializer=AffectaSerializer(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
            elif self.request.user.is_user:
                dons=Affectation.objects.filter(commune=self.request.user.commune)
                serializer=AffectaSerializer(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
            else:
                dons=Affectation.objects.filter(agent=self.request.user.user_name,status=False)
                serializer=AffectaSerializer(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        return Response({'status':status.HTTP_400_BAD_REQUEST})

    def post(self,request):
        message='Merci pour votre contribution'
        data=self.request.data
        data['owner']=self.request.user.user_name
        serializer = AffectaSerializer(data=data)
        message='Merci pour votre contribution'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.errors})

class CrudAffectation(APIView):
    def get_object(self, pk):
        try:
            return Affecter.objects.get(pk=pk)
        except Affecter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AffectaSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AffectaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Zonez(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                dons=Zone.objects.all()
                serializer=ZoneSerializer(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
            else:
                dons=Zone.objects.filter(commune=self.request.user.commune)
                serializer=ZoneSerializer(dons, many=True)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        return Response({'status':status.HTTP_400_BAD_REQUEST})

    def post(self,request):
        message='Merci pour votre contribution'
        data=self.request.data
        data['commune']=self.request.user.commune
        serializer = ZoneSerializer(data=data)
        message='Merci pour votre contribution'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.errors})

class CrudZone(APIView):
    def get_object(self, pk):
        try:
            return Zone.objects.get(pk=pk)
        except Zone.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ZoneSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ZoneSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Quartierl(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser or self.request.user.is_agent:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                dataf=[dict(i) for i in quartiers]
                quartierT=[i['commune'] for i in dataf]
                data={}
                data2={}
                for quartier in quartierT:
                    data["{}".format(quartier)]=[dict(s) for s in QuartierSerializer(Quartier.objects.filter(commune=quartier),context={'request': request},many=True).data]
                for s in data.keys():
                    data2["{}".format(s)]=[q["quartier"] for q in data[s]]
                return Response(data2,status=status.HTTP_200_OK)
            else:
                data={}
                data2={}
                data["quartier"]=[dict(s) for s in QuartierSerializer(Quartier.objects.filter(commune=self.request.user.commune),context={'request': request},many=True).data]
                for s in data.keys():
                    data2["{}".format(s)]=[q["quartier"] for q in data[s]]
                return Response(data2,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        data=self.request.data
        liste=[]
        for i in data["quartier"]:
            dico={}
            dico["commune"]=data["commune"]
            dico["quartier"]=i
            print(dico)
            liste.append(dico)
        serializer = QuartierSerializer(data=liste, many=True)
        message='Insertion Done'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class CrudQuartier(APIView):
    def get_object(self, pk):
        try:
            return Quartier.objects.get(pk=pk)
        except Quartier.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = QuartierSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = QuartierSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InfoAffecter(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        chef=AffectaSerializer(Affectation.objects.filter(agent=self.request.user.user_name),context={'request': request},many=True).data
        zone=[i["quartier"] for i in chef]
        quartier={}
        quartiers={}
        x=[]
        for q in zone:
            quartier["{}".format(q)]=[dict(i) for i in ZoneSerializer(Zone.objects.filter(nomz=q),context={'request': request},many=True).data]
        for s in quartier.values():
            x=list(s[0].values())
        quartiers["{}".format(x[0])]=x[2:]
        return JsonResponse(quartiers)



class QuartierT(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser or self.request.user.is_agent:
                quartiers=QuartierSerializer(Quartier.objects.all(),context={'request': request},many=True).data
                x=[]
                for i in quartiers:
                    x.append(i['quartier'])
                data={}
                data["quartier"]=x
                return Response(data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)






