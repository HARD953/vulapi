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
# Create your views here.

class CreateAgent(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        message='Merci pour votre contribution:\n nous vous contacterons dans peut'
        data=request.data
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
        serializer = UserSerializer(data=data)
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.error})


# class CreateAgent(APIView):
#     queryset=NewUser.objects.all()
#     permission_classes=[AllowAny]
#     serializer_class=UserSerializer

class CreateAdmin(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        message='Merci pour votre contribution:\n nous vous contacterons dans peut'
        data=request.data
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
        serializer = AdminSerializer(data=data)
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.error})

class CreateSuperAdmin(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        message='Merci pour votre contribution:\n nous vous contacterons dans peut'
        data=request.data
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
        serializer = SuperAdminSerializer(data=data)
        message='Merci pour votre contribution:\n nous vous contacterons dans peu'
        if serializer.is_valid():
            serializer.save()
            return Response({'message':message,'data':serializer.data})            
        return Response({'message':serializer.error})

# class FilterRecensement(filters.FilterSet):
#     agent=filters.CharFilter(lookup_expr='icontains')
#     class Meta:
#         model:NewUser
#         fields=("agent","commune")


class ListAgent(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=NewUser
    serializer_class=UserSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["user_name","commune","first_name","start_date","adresse"]
    def get_queryset(self):
        user = self.request.user
        return NewUser.objects.filter(commune=user.commune,is_agent=True)

class ListAllAgent(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=NewUser
    serializer_class=UserSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["user_name","commune","first_name","start_date","adresse"]
    def get_queryset(self):
        user = self.request.user
        return NewUser.objects.filter(is_agent=True)

class ListAdmin(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=NewUser
    serializer_class=AdminSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["user_name","commune","first_name","start_date","adresse"]
    def get_queryset(self):
        user = self.request.user
        return NewUser.objects.filter(is_user=True)

class ListSuperAdmin(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=NewUser
    serializer_class=AdminSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["user_name","commune","first_name","start_date","adresse"]
    def get_queryset(self):
        user = self.request.user
        return NewUser.objects.filter(is_superuser=True)

class ListRecenser(generics.ListAPIView):
    permission_classes=[AllowAny]
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.all()

class DetailAgent(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["user_name","commune","first_name","start_date","adresse"]
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.all()

class DetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    model=NewUser
    serializer_class=AdminSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=["user_name","commune","first_name","start_date","adresse"]
    def get_queryset(self):
        user = self.request.user
        return NewUser.objects.filter(is_user=True)

# class DetailAgent(generics.RetrieveUpdateDestroyAPIView):
#     queryset=NewUser.objects.all()
#     permission_classes=[IsAdminAuthenticated]
#     serializer_class=UserSerializer

class DetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset=NewUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=AdminSerializer

#How make to connect when we use token jwt
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_name'] = user.user_name
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# def get1(request):
#     if request.method=="GET":
#         recenser=NewUser.objects.all()
#         serializer = UserSerializer(recenser, many=True)
#         return JsonResponse(serializer.data, safe=False)

# Select All information for user who as connected
# class RecensementView(APIView):
#     permission_classes=[AdminAuthenticated]
#     def get(self,request):
#         user=NewUser.objects.get(user_name=request.user)
#         serializer_context = {'request': request}
#         user_data=UserSerializer(user,context=serializer_context).data
#         return Response(user_data)
        




class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        user=NewUser.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'iat':datetime.datetime.utcnow()
            }
        token =jwt.encode(payload, 'secret',algorithm='HS256')
        response =Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data ={
            'jwt':token
        }
        return response

# class LogoutView(APIView):
#     def post(self, request):
#         response=Response()
#         response.delete_cookie('jwt')
#         response.data ={
#             'message':'success'
#         }
#         return response


# class DetailAdmin(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes=[IsAdminAuthenticated]
#     def list(self, request):
#         queryset = NewUser.objects.filter(is_agent=True,localite=request.POST['commue'])
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

# class DetailSuperAdmin(generics.RetrieveUpdateDestroyAPIView):
#     queryset=NewUser.objects.all()
#     permission_classes=[AllowAny]
#     serializer_class=SuperAdminSerializer

#Select All information for user who as connected
# class RecensementView(APIView):
#     permission_classes=[IsAdminAuthenticated]
#     def get(self,request):
#         user=NewUser.objects.get(pk=pk,is_agent=True,localite=request.POST['commue'])
#         serializer_context = {'request': request}
#         user_data=UserSerializer(user,context=serializer_context).data
#         return Response(user_data)