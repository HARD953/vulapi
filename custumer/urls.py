from django.urls import path,include
from .views import*
from .superadmin import*
from .admins import*
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns=format_suffix_patterns([
    path('superadmin/', CreateSuperAdmin.as_view(),name='registers-sadmin'),
    path('admins/', CreateAdmin.as_view(),name='registers-admin'),
    path('agent/', CreateAgent.as_view(),name='registers-agent'),
    path('effecter/', Affecter.as_view(),name='affecter-agent'),


    path('aladmin/', ListAdmin.as_view(),name='registers-sadmin-detail'),
    path('alagent/', ListAgent.as_view(),name='registers-admin-detail'),
    path('allagent/', ListAllAgent.as_view(),name='registers-admin-detail'),

    path('admin/<int:pk>', DetailAdmin.as_view(),name='registers-sadmin-detail'),
    path('agent/<int:pk>', DetailAgent.as_view(),name='registers-admin-detail'),

#Superadmin
    path('chefmenages/', ChefMenageList.as_view(),name='chef_menage-list'),
    path('conjoints/', ConjointList.as_view(),name='conjoint'),
    path('recensements/', RecenserList.as_view(),name='recenser-list'),
    path('enfants/', EnfantList.as_view(),name='enfant'),
    path('commodites/', CommoditeList.as_view(),name='commodite'),
    path('equipements/', EquipementList.as_view(),name='equipement'),
    path('decess/', DecesList.as_view(),name='deces'),
    path('charges/', ChargeList.as_view(),name='charge'),

    path('chefmenagesd/<int:pk>/', ChefMenageListd.as_view(),name='chef_menage-listd'),
    path('conjointsd/<int:pk>/', ConjointListd.as_view(),name='conjointd'),
    path('recensementsd/<int:pk>/', RecenserListd.as_view(),name='recenser-listd'),
    path('enfantsd/<int:pk>/', EnfantListd.as_view(),name='enfantd'),
    path('commoditesd/<int:pk>/', CommoditeListd.as_view(),name='commodited'),
    path('equipementsd/<int:pk>/', EquipementListd.as_view(),name='commodited'),
    path('decessd/<int:pk>/', DecesListd.as_view(),name='commodited'),
    path('chargesd/<int:pk>/', ChargeListd.as_view(),name='commodited'),

#Admin par district
    path('chefmenagea/', ChefMenageLista.as_view()),
    path('conjointa/', ConjointLista.as_view()),
    path('recensementa/', RecenserLista.as_view()),
    path('enfanta/', EnfantLista.as_view()),
    path('commoditea/', CommoditeLista.as_view()),
    path('equipementa/', EquipementLista.as_view()),
    path('decesa/', DecesLista.as_view()),
    path('chargea/', ChargeLista.as_view()),

    path('chefmenagead/<int:pk>/', ChefMenageListad.as_view()),
    path('conjointad/<int:pk>/', ConjointListad.as_view()),
    path('recensementad/<int:pk>/', RecenserListad.as_view()),
    path('enfantad/<int:pk>/', EnfantListad.as_view()),
    path('commoditead/<int:pk>/', CommoditeListad.as_view()),
    path('equipementad/<int:pk>/', EquipementListad.as_view()),
    path('decesad/<int:pk>/', DecesListad.as_view()),
    path('chargead/<int:pk>/', ChargeListad.as_view()),


    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
])