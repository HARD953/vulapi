from django.urls import path,include
from .views import*
from rest_framework.urlpatterns import format_suffix_patterns
from .analyse import*
from .analysed.analysev import *
from .vulnera.vulnerablecond import*
from .vulnera.vulnerablephy import*
from .vulnera.vulnerableetude import*
from .vulnera.vulnerableoccu import*
from .recenserg.generale import*
from .recenserg.individu import*
from .analysed.informationg import*
from .critere.indicateurs import*
from .statistiquesr.statistique import*
from .statistiquesr.statistique3 import*
from .statistiquesr.statistique2 import*
from .analysed.analysecr import*

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
    path('enfantr/', EnfantRList.as_view(),name='lenfant'),
    path('denfantr/<int:pk>/', EnfantRDetail.as_view(),name='enfant-rue'),
    
    #Information traiter
    path('analyses2/',Information),
    path('analyses/',Information2),
    #Information simple
    path('vulnerablephys/',vulnerablep),
    path('vulnerablecon/',vulnerablec),
    path('vulnerableetud/',vulnerableet),
    path('vulnerableoccup/',vulnerableoc),
    path('menage/',vulnerableg),
    path('individus/',vulnerableI),
    #Information détailler
    path('information/<int:pk>/',info),
    path('informationd/<int:pk>/',ana),
    #Les statistiques pour le superadmin
    path('staticirclem/',StatcircleM.as_view()),
    path('staticirclei/',StatcircleI.as_view()),
    path('statibarm/',StatbarM.as_vieew()),
    path('statibari/',StatbarI.as_view()),

    path('statistiquegm/',statcircleMGeneral),
    path('statistiquegi/',statcircleIGeneral),

    path('homme/<str:slug>/',homme),
    path('individug/',individug),
    path('enfantru/<str:slug>/',enfant),
    path('enfantg/',enfantg),

]