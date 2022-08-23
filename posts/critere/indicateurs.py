from datetime import date
from re import I
from custumer.models import*
from custumer.serializersc import*
from django.http import HttpResponseGone,JsonResponse
from rest_framework.response import Response

def calculate_age(born):
    today = date.today()
    return int(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

def criterechef(data):
    critere=[]
    dics=[dict(i) for i in MySerializerChef(CritereChef.objects.all(),many=True).data]
    for i in dics:
        critere.append(i['sexeChef'])
        critere.append(i['agechef'])
        critere.append(i['nationalite'])
        critere.append(i['niveauEtude'])
        critere.append(i['maladie'])
        critere.append(i['handicap'])
        critere.append(i['occupations'])
    if data[0]=="sexe":
        if data[1]=="Homme":
            return critere[0][0]
        else:
            return critere[0][1]

    elif data[0]=="age":
        if data[1]<=14 and data[1]>=0:
            return critere[0][0]
        elif data[1]<=24 and data[1]>=15:
            return critere[0][0]
        elif data[1]<=64 and data[1]>=25:
            return critere[0][0]
        else:
            return critere[0][0]

    elif data[0]=="nationalite":
        if data[1]=="Ivoirienne":
            return critere[0][0]
        else:
            return critere[0][0]

    elif data[0]=="niveau":
        if data[1]=="CEPE":
            return critere[0][0]
        elif data[1]=="BEPC":
            return critere[0][0]
        elif data[1]=="BAC":
            return critere[0][0]
        elif data[1]=="BTS":
            return critere[0][0]
        elif data[1]=="DUT":
            return critere[0][0]
        elif data[1]=="LICENCE":
            return critere[0][0]
        elif data[1]=="MASTER":
            return critere[0][0]
        elif data[1]=="DOCTARAT":
            return critere[0][0]
        else:
            return critere[0][0]

    elif data[0]=="maladie":
        if data[1]=="CANCER":
            return critere[0][1]

    elif data[0]=="handicap":
        if data[1]=="Handicap_Mental":
            return critere[0][1]
        elif data[1]=="Non_voyant":
            return critere[0][1]
        elif data[1] in ['Handicap_membre_superieurs','Handicap_membre_inferieurs']:
            return critere[0][1]
        elif data[1] in ['Sourd','Muet','Begue']:
            return critere[0][1]
        else:
            return critere[0][1]

    elif data[0]=="occupation":
        if data[1]=="Informaticien":
            return critere[0][0]
    return JsonResponse({'data':dics})

def critereconj(data):
    critere=[]
    dics=[dict(i) for i in MySerializerConj(CritereConj.objects.all(),many=True).data]
    for i in dics:
        critere.append(i['agec'])
        critere.append(i['niveauEtude'])
        critere.append(i['maladie'])
        critere.append(i['handicap'])
        critere.append(i['occupations'])
    if data[0]=="age":
        if data[1]<=14 and data[1]>=0:
            return critere[0][0]
        elif data[1]<=24 and data[1]>=15:
            return critere[0][0]
        elif data[1]<=64 and data[1]>=25:
            return critere[0][0]
        else:
            return critere[0][0]
    elif data[0]=="niveau":
        if data[1]=="CEPE":
            return critere[0][0]
        elif data[1]=="BEPC":
            return critere[0][0]
        elif data[1]=="BAC":
            return critere[0][0]
        elif data[1]=="BTS":
            return critere[0][0]
        elif data[1]=="DUT":
            return critere[0][0]
        elif data[1]=="LICENCE":
            return critere[0][0]
        elif data[1]=="MASTER":
            return critere[0][0]
        elif data[1]=="DOCTARAT":
            return critere[0][0]
        else:
            return critere[0][0]
    elif data[0]=="maladie":
        if data[1]=="CANCER":
            return critere[0][1]
    elif data[0]=="handicap":
        if data[1]=="Handicap_Mental":
            return critere[0][1]
        elif data[1]=="Non_voyant":
            return critere[0][1]
        elif data[1] in ['Handicap_membre_superieurs','Handicap_membre_inferieurs']:
            return critere[0][1]
        elif data[1] in ['Sourd','Muet','Begue']:
            return critere[0][1]
        else:
            return critere[0][1]

    elif data[0]=="occupation":
        if data[1]=="Informaticien":
            return critere[0][0]

    return JsonResponse({'data':dics})

def critereenf(data):
    critere=[]
    dics=[dict(i) for i in MySerializerEnfant(CritereEnfant.objects.all(),many=True).data]
    for i in dics:
        critere.append(i['agec'])
        critere.append(i['niveauEtude'])
        critere.append(i['maladie'])
        critere.append(i['handicap'])
    if data[0]=="age":
        if data[1]<=14 and data[1]>=0:
            return critere[0][0]
        elif data[1]<=24 and data[1]>=15:
            return critere[0][0]
        elif data[1]<=64 and data[1]>=25:
            return critere[0][0]
        else:
            return critere[0][0]
    elif data[0]=="niveau":
        if data[1]=="CEPE":
            return critere[0][0]
        elif data[1]=="BEPC":
            return critere[0][0]
        elif data[1]=="BAC":
            return critere[0][0]
        elif data[1]=="BTS":
            return critere[0][0]
        elif data[1]=="DUT":
            return critere[0][0]
        elif data[1]=="LICENCE":
            return critere[0][0]
        elif data[1]=="MASTER":
            return critere[0][0]
        elif data[1]=="DOCTARAT":
            return critere[0][0]
        else:
            return critere[0][0]
    elif data[0]=="maladie":
        if data[1]=="CANCER":
            return critere[0][1]
    elif data[0]=="handicap":
        if data[1]=="Handicap_Mental":
            return critere[0][1]
        elif data[1]=="Non_voyant":
            return critere[0][1]
        elif data[1] in ['Handicap_membre_superieurs','Handicap_membre_inferieurs']:
            return critere[0][1]
        elif data[1] in ['Sourd','Muet','Begue']:
            return critere[0][1]
        else:
            return critere[0][1]

    return JsonResponse({'data':dics})

def criterecha(data):

    critere=[]
    dics=[dict(i) for i in MySerializerCharge(CritereCharge.objects.all(),many=True).data]
    for i in dics:
        i['agec']
        i['niveauEtude']
        i['maladie']
        i['handicap']
        i['occupations']

    if data[0]=="age":
        if data[1]<=14 and data[1]>=0:
            return critere[0][0]
        elif data[1]<=24 and data[1]>=15:
            return critere[0][0]
        elif data[1]<=64 and data[1]>=25:
            return critere[0][0]
        else:
            return critere[0][0]
    elif data[0]=="niveau":
        if data[1]=="CEPE":
            return critere[0][0]
        elif data[1]=="BEPC":
            return critere[0][0]
        elif data[1]=="BAC":
            return critere[0][0]
        elif data[1]=="BTS":
            return critere[0][0]
        elif data[1]=="DUT":
            return critere[0][0]
        elif data[1]=="LICENCE":
            return critere[0][0]
        elif data[1]=="MASTER":
            return critere[0][0]
        elif data[1]=="DOCTARAT":
            return critere[0][0]
        else:
            return critere[0][0]
    elif data[0]=="maladie":
        if data[1]=="CANCER":
            return critere[0][1]
    elif data[0]=="handicap":
        if data[1]=="Handicap_Mental":
            return critere[0][1]
        elif data[1]=="Non_voyant":
            return critere[0][1]
        elif data[1] in ['Handicap_membre_superieurs','Handicap_membre_inferieurs']:
            return critere[0][1]
        elif data[1] in ['Sourd','Muet','Begue']:
            return critere[0][1]
        else:
            return critere[0][1]

    elif data[0]=="occupation":
        if data[1]=="Informaticien":
            return critere[0][0]

    return JsonResponse({'data':dics})

def critereco(data):

    critere=[]
    dics=[dict(i) for i in MySerializerCommodite(CritereCommodite.objects.all(),many=True).data]
    for i in dics:
        critere.append(i['eclairage'])
        critere.append(i['cuisson'])
        critere.append(i['aeaux'])
        critere.append(i['ordure'])
        critere.append(i['nombrep'])
        critere.append(i['aisance'])
        critere.append(i['loyer'])
        critere.append(i['typelogement'])
    if data[0]=="eclairage":
        if data[1]=="RACCORDE":
            return 2
        elif data[1]=="COMPTEUR":
            return 1
        else:
            return 0
    elif data[0]=="aisance":
        if data[1]=="NWC":
            return 2
        elif data[1]=="FOSSE":
            return 1
        else:
            return 0
    elif data[0]=="combustible":
        if data[1]=="feu_bois":
            return 2
        elif data[1]=="CHARBON":
            return 1
        elif data[1]=="gaz" or data[1]=="ELECTRICITE":
            return 0
    elif data[0]=="eaux":
        if data[1]=="RIVIERE" or data[1]=="POMPE":
            return 2
        elif data[1]=="ROBINET_COMMUN":
            return 1
        else:
            return 0

    elif data[0]=="logement1":
        if int(data[1])>3:
            return 0
        elif int(data[1])<3 and int(data[1])>1:
            return 1
        else:
            return 2

    elif data[0]=="logement2":
        if data[1]=="BANCO":
            return 2
        elif data[1]=="COUR_COMMUNE":
            return 1
        else:
            return 0
    return JsonResponse({'data':dics})

def criteredes(data):
    critere=[]
    dics=[dict(i) for i in MySerializerDeces(CritereDeces.objects.all(),many=True).data]
    for i in dics:
        critere.append(i['agec'])
    return JsonResponse({'data':dics})

def EquipementMenage(data):
    critere=[]
    dics=[dict(i) for i in MySerializerEquipement(CritereEquipement.objects.all(),many=True).data]
    for i in dics:
        critere.append(i['moyend'])
        critere.append(i['moyend'])
        critere.append(i['moyend'])
    if len(data)<=1:
        return critere[0]
    elif len(data)<=4 and len(data)>1:
        return critere[0]
    else:
        return critere[0]

def critereequ(data):
    for i in data[0]:
        if len(i)!=0:
            print(i)
            moyend=int(EquipementMenage(i))
        else:
            moyend=0
    for q in data[1]:
        if len(q)!=0:
            moyene=int(EquipementMenage(q))
        else:
            moyene=0
    for w in data[2]:
        if len(w)!=0:
            moyena=int(EquipementMenage(w))
        else:
            moyena=0
    equi=moyend+moyene+moyena
    return equi


def critereMena(request):
    dics=[dict(i) for i in MySerializerMenage(CritereMenage.objects.all(),many=True).data]
    for i in dics:
        i['moyenneage']
        i['niveauEtudeM']
        i['typeMenage']
        i['occupations']
    return JsonResponse({'data':dics})


def critereHabi(request):
    dics=[dict(i) for i in MySerializerHabitat(CritereHabitat.objects.all(),many=True).data]
    for i in dics:
        i['ville']
        i['quartier']
    return JsonResponse({'data':dics})

def critereGene(request):
    dics=[dict(i) for i in MySerializerGeneral(CritereGeneral.objects.all(),many=True).data]
    for i in dics:
        i['conditionvie']
        i['conditionphy']
        i['conditionoccup']
        i['conditionnivee']
    return JsonResponse({'data':dics})

