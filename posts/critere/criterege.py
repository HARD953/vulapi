from datetime import date
from re import I
from custumer.models import*
from custumer.serializersc import*
from django.http import HttpResponseGone,JsonResponse
from rest_framework.response import Response

def critereGene(request,data):
    if request.method=="GET":
        critere=[]
        dics=[dict(i) for i in MySerializerGeneral(CritereGeneral.objects.all(),many=True).data]
        for i in dics:
            critere.append(i['conditionvie'])
            critere.append(i['conditionphy'])
            critere.append(i['conditionoccup'])
            critere.append(i['conditionnivee'])
        if data[0]=="conditionvie":
            if data[1]==2:
                return critere[0][0]
            elif data[1]==2:
                return critere[0][1]
            else:
                return critere[0][2]
        return JsonResponse({'data':dics})