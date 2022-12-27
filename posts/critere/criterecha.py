from datetime import date
from re import I
from custumer.models import*
from custumer.serializersc import*
from django.http import HttpResponseGone,JsonResponse
from rest_framework.response import Response


def criterecha(request,data):
    if request.method=="GET":
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
                return critere[0][1]
            elif data[1]<=64 and data[1]>=25:
                return critere[0][0]
            else:
                return critere[0][0]

        elif data[0]=="niveau":
            if data[1]=="CEPE":
                return critere[1][0]
            elif data[1]=="BEPC":
                return critere[1][0]
            elif data[1]=="BAC":
                return critere[1][1]
            elif data[1]=="BTS":
                return critere[1][1]
            elif data[1]=="DUT":
                return critere[1][1]
            elif data[1]=="LICENCE":
                return critere[1][2]
            elif data[1]=="MASTER":
                return critere[1][2]
            elif data[1]=="DOCTARAT":
                return critere[1][2]
            else:
                return critere[1][2]

        elif data[0]=="maladie":
            if data[1]=="CANCER":
                return critere[2][1]

        elif data[0]=="handicap":
            if data[1]=="Handicap_Mental":
                return critere[3][1]
            elif data[1]=="Non_voyant":
                return critere[3][1]
            elif data[1] in ['Handicap_membre_superieurs','Handicap_membre_inferieurs']:
                return critere[3][1]
            elif data[1] in ['Sourd','Muet','Begue']:
                return critere[3][1]
            else:
                return critere[3][1]
                
        elif data[0]=="occupation":
            if data[1]=="Informaticien":
                return critere[4][2]

        return JsonResponse({'data':dics})