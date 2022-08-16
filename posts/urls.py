from django.urls import path,include
from .views import*
from rest_framework.urlpatterns import format_suffix_patterns
from .analyse import*
from .dat import *
from .vulnerablecond import*
from .vulnerablephy import*
from .vulnerableetude import*
from .vulnerableoccu import*
from .generale import*
from .individu import*


urlpatterns=[
    path('chefmenage/', ChefMenageList.as_view(),name='chef_menage-list'),
    path('dchefmenage/<int:pk>/', ChefMenageDetail.as_view(),name='chef_menage-detail'),
    path('conjoint/', ConjointList.as_view(),name='conjoint'),
    path('dconjoint/<int:pk>/', ConjointDetail.as_view(),name='conjoint-detail'),
    path('recensement/', RecenserList.as_view(),name='recenser-list'),
    path('drecensement/<int:pk>/', RecenserDetail.as_view(),name='recenser-detail'),
    path('enfant/', EnfantList.as_view(),name='enfant'),
    path('denfant/<int:pk>/', EnfantDetail.as_view(),name='enfant-detail'),
    path('commodite/', CommoditeList.as_view(),name='commodite'),
    path('dcommodite/<int:pk>/', CommoditeDetail.as_view(),name='commodite-detail'),
    path('equipement/', EquipementList.as_view(),name='equipement'),
    path('dequipement/<int:pk>/', EquipementDetail.as_view(),name='equipement-detail'),
    path('deces/', DecesList.as_view(),name='deces'),
    path('ddeces/<int:pk>/', DecesDetail.as_view(),name='deces-detail'),
    path('charge/', ChargeList.as_view(),name='charge'),
    path('dcharge/<int:pk>/', ChargeDetail.as_view(),name='charge-detail'),
    path('recenser/', RecensementView.as_view(),name='charge'),

    #Information traiter
    path('analyses2/',Information),
    path('analyses/',Information2),
    #Information simple
    path('vulnerablephys/',vulnerablep),
    path('vulnerablecon/',vulnerablec),
    path('vulnerableetud/',vulnerableet),
    path('vulnerableoccup/',vulnerableoc),
    path('vulnerablegs/',vulnerableg),
    path('individus/',vulnerableI)
]