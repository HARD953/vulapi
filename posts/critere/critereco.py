from datetime import date
from re import I
from custumer.models import*
from custumer.serializersc import*
from django.http import HttpResponseGone,JsonResponse
from rest_framework.response import Response

def critereco(request,data):
    if request.method=="GET":
        critere=[]
        dics=[dict(i) for i in MySerializerCommodite(CritereCommodite.objects.all(),many=True).data]
        for i in dics:
            critere.append(i['eclairage'])
            critere.append(i['cuisson'])
            critere.append(i['aeaux'])
            critere.append(i['ordure'])
            critere.append(i['nombrep'])
            critere.append(i['aisance'])
            critere.append(i['typelogement'])
            critere.append(i['loyer'])
            
        if data[0]=="eclairage":
            if data[1]=="RACCORDE":
                return critere[0][0]
            elif data[1]=="COMPTEUR":
                return critere[0][1]
            else:
                return critere[0][2]
                
        elif data[0]=="aisance":
            if data[1]=="NWC":
                return critere[1][0]
            elif data[1]=="FOSSE":
                return critere[1][1]
            else:
                return critere[1][2]

        elif data[0]=="combustible":
            if data[1]=="feu_bois":
                return critere[2][0]
            elif data[1]=="CHARBON":
                return critere[2][1]
            elif data[1]=="gaz" or data[1]=="ELECTRICITE":
                return critere[2][2]

        elif data[0]=="ordure":
            if data[1]=="feu_bois":
                return critere[3][0]
            elif data[1]=="CHARBON":
                return critere[3][1]
            elif data[1]=="gaz" or data[1]=="ELECTRICITE":
                return critere[3][2]

        elif data[0]=="eaux":
            if data[1]=="RIVIERE" or data[1]=="POMPE":
                return critere[4][0]
            elif data[1]=="ROBINET_COMMUN":
                return critere[4][1]
            else:
                return critere[4][2]

        elif data[0]=="logement1":
            if int(data[1])>3:
                return critere[5][0]
            elif int(data[1])<3 and int(data[1])>1:
                return critere[5][1]
            else:
                return critere[5][2]

        elif data[0]=="logement2":
            if data[1]=="BANCO":
                return critere[6][0]
            elif data[1]=="COUR_COMMUNE":
                return critere[6][1]
            else:
                return critere[6][2]

        elif data[0]=="loyer":
            if data[1]==True:
                return critere[7][0]
            else:
                return critere[7][2]
        return JsonResponse({'data':dics})
