import requests

def decoupage():
    payload={"Region":"","Chef_Lieu":"","Departement":"","Sous_Prefecture":"","Commune":""}
    commune1=requests.get('https://data.gouv.ci/data-fair/api/v1/datasets/liste-des-circonscriptions-administratives-et-des-communes/lines?size=252&highlight=REGION%2CCHEF-LIEU%2CDEPARTEMENT%2CSOUS-PREFECTURE%2CCOMMUNE')
    commune2=requests.get("https://data.gouv.ci/data-fair/api/v1/datasets/liste-des-circonscriptions-administratives-et-des-communes/lines?size=252&select=COMMUNE")
    communeparc=requests.get("https://data.gouv.ci/data-fair/api/v1/datasets/liste-des-circonscriptions-administratives-et-des-communes/lines?size=252&select=COMMUNE&qs=ABIDJAN")
    region=requests.get("")
    print(commune.content)
decoupage()