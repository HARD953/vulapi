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

def vulnerableI(request):
    if request.method=="GET":
        chef=Chef_menage.objects.filter(individu=True)
        chefs=PostChefMSerializer(chef,context={'request': request},many=True)
        return JsonResponse({'data':chefs.data,'status':status.HTTP_200_OK})
    #     dataf=[dict(i) for i in chefs.data]
    #     idf=[i['id'] for i in dataf]
    #     data1={}
    #     for i in idf:
    #         data={}
    #         data['chefmenage']=[dict(s) for s in PostChefMSerializer(Chef_menage.objects.filter(id=i),context={'request': request},many=True).data]
    #         data['enfant']=[dict(s) for s in EnfantS(Enfant.objects.filter(parentf=i),context={'request': request},many=True).data]
    #         data['charge']=[dict(s) for s in PostChargeSerializer(Charge.objects.filter(parentg=i),context={'request': request},many=True).data]
    #         data['conjoint']=[dict(s) for s in PostConjointSerializer(Conjoint.objects.filter(idc=i),context={'request': request},many=True).data]
    #         data['recenser']=[dict(s) for s in RecensementS(Recenser.objects.filter(parent=i),context={'request': request},many=True).data]
    #         data['equipement']=[dict(s) for s in EquipementS(Equipement.objects.filter(parente=i),context={'request': request},many=True).data]
    #         data['commodite']=[dict(s) for s in CommoditeS(Commodite.objects.filter(parentc=i),context={'request': request},many=True).data]
    #         data['deces']=[dict(s) for s in DeceS(Deces.objects.filter(parentd=i),context={'request': request},many=True).data]
    #         data1["{}".format(i)]=data
    #     return JsonResponse({"data":data, "status":status.HTTP_200_OK,"message":"liste des récensers"})
    # else:
    #     return Response({'message':'Personne'})



    
    