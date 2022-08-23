from datetime import date
from re import I
from custumer.models import*
from custumer.serializersc import*
from django.http import HttpResponseGone,JsonResponse
from rest_framework.response import Response


def criteredes(request,data):
    if request.method=="GET":
        critere=[]
        dics=[dict(i) for i in MySerializerDeces(CritereDeces.objects.all(),many=True).data]
        for i in dics:
            critere.append(i['agec'])
        return JsonResponse({'data':dics})
