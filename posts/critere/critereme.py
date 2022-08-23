from datetime import date
from re import I
from custumer.models import*
from custumer.serializersc import*
from django.http import HttpResponseGone,JsonResponse
from rest_framework.response import Response

def critereMena(request,data):
    if request.method=="GET":
        critere=[]
        dics=[dict(i) for i in MySerializerMenage(CritereMenage.objects.all(),many=True).data]
        for i in dics:
            critere.append(i['moyenneage'])
            critere.append(i['niveauEtudeM'])
            critere.append(i['typeMenage'])
            critere.append(i['occupations'])

        if data[0]=="moyenneage":
            if data[1]==2:
                return critere[0][0]
            elif data[1]==2:
                return critere[0][1]
            else:
                return critere[0][2]
        if data[0]=="niveauEtudeM":
            if data[1]==2:
                return critere[0][0]
            elif data[1]==2:
                return critere[0][1]
            else:
                return critere[0][2]

        if data[0]=="typeMenage":
            if data[1]==2:
                return critere[0][0]
            elif data[1]==2:
                return critere[0][1]
            else:
                return critere[0][2]

        if data[0]=="occupations":
            if data[1]==2:
                return critere[0][0]
            elif data[1]==2:
                return critere[0][1]
            else:
                return critere[0][2]

        return JsonResponse({'data':dics})