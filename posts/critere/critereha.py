from datetime import date
from re import I
from custumer.models import*
from custumer.serializersc import*
from django.http import HttpResponseGone,JsonResponse
from rest_framework.response import Response




def critereHabi(request,data):
    if request.method=="GET":
        critere=[]
        dics=[dict(i) for i in MySerializerHabitat(CritereHabitat.objects.all(),many=True).data]
        for i in dics:
            critere.append(i['ville'])
            critere.append(i['quartier'])
        if data[0]=="ville":
            if data[1]==2:
                return critere[0][0]
            elif data[1]==2:
                return critere[0][1]
            else:
                return critere[0][2]

        if data[0]=="quartier":
            if data[1]==2:
                return critere[1][0]
            elif data[1]==2:
                return critere[1][1]
            else:
                return critere[1][2]
        return JsonResponse({'data':dics})


