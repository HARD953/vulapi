from datetime import date
from re import I
from custumer.models import*
from custumer.serializersc import*
from django.http import HttpResponseGone,JsonResponse
from rest_framework.response import Response

def calculate_age(born):
    today = date.today()
    return int(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

def criterechef(request,data):
    if request.method=="GET":
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
            if data[1]<=24 and data[1]>=15:
                return critere[1][2]
            elif data[1]<=64 and data[1]>=25:
                return critere[1][1]
            else:
                return critere[1][0]

        elif data[0]=="nationalite":
            if data[1]=="Ivoirienne":
                return critere[2][2]
            elif data[1=="Occident"]:
                return critere[2][1]
            else:
                return critere[2][0]

        elif data[0]=="niveau":
            if data[1]=="CEPE":
                return critere[3][0]
            elif data[1]=="BEPC":
                return critere[3][0]
            elif data[1]=="BAC":
                return critere[3][1]
            elif data[1]=="BTS":
                return critere[3][1]
            elif data[1]=="DUT":
                return critere[3][1]
            elif data[1]=="LICENCE":
                return critere[3][2]
            elif data[1]=="MASTER":
                return critere[3][2]
            elif data[1]=="DOCTARAT":
                return critere[3][2]
            else:
                return critere[3][2]

        elif data[0]=="maladie":
            return critere[4][0]

        elif data[0]=="handicap":
            if data[1]=="Handicap_Mental":
                return critere[5][1]
            elif data[1]=="Non_voyant":
                return critere[5][1]
            elif data[1] in ['Handicap_membre_superieurs','Handicap_membre_inferieurs']:
                return critere[5][1]
            elif data[1] in ['Sourd','Muet','Begue']:
                return critere[5][1]
            else:
                return critere[5][1]

        elif data[0]=="occupation":
            if data[1]=="Informaticien":
                return critere[6][2]
        return JsonResponse({'data':dics})