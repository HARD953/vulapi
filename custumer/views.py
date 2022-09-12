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
from .serializers1 import AffectaSerializer

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
        print(snippet)
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
            data['is_staff']=False

        if data['is_active']=="is_active":
            data['is_active']=True
        else:
            data['is_active']=False
    
        if data['is_user']=="is_user":
            data['is_user']=True
        else:
            data['is_user']=False

        data['responsable']=self.request.user.user_name

        serializer = AdminSerializer(data=data)
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.errors})

class CrudAdmin(APIView):
    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print(snippet)
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
    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print(snippet)
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
        data['admin/agent']=NewUser.objects.filter(responsable=chefs[0]["user_name"]).count()
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
        data['individu']=(Chef_menage.objects.filter(owner1=idf[0],individu=True)).count()
        data['menage']=(Chef_menage.objects.filter(owner1=idf[0],menage=True)).count()
        data['vulnerable_physique']=(Chef_menage.objects.filter(owner1=idf[0],vulnerablePhy=True)).count()
        data['vulnerable_conditionv']=(Chef_menage.objects.filter(owner1=idf[0],vulnerableCondi=True)).count()
        data['vulnerable_etude']=(Chef_menage.objects.filter(owner1=idf[0],vulnerableEtude=True)).count()
        data['vulnerable_sansE']=(Chef_menage.objects.filter(owner1=idf[0],vulnerableOccup=True)).count()
        return JsonResponse({'data':data})


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