from datetime import date
from re import I
from custumer.models import*
from custumer.serializersc import*
from django.http import HttpResponseGone,JsonResponse
from rest_framework.response import Response


def EquipementMenage(request,data):
    if request.method=="GET":
        critere=[]
        dics=[dict(i) for i in MySerializerEquipement(CritereEquipement.objects.all(),many=True).data]
        for i in dics:
            critere.append(i['moyend'])
            critere.append(i['moyend'])
            critere.append(i['moyend'])
    if len(data)<=1:
        return critere[0][0]
    elif len(data)<=4 and len(data)>1:
        return critere[0][1]
    else:
        return critere[0][2]

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
