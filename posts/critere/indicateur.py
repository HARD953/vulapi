from datetime import date
from re import I
from custumer.models import*

def calculate_age(born):
    today = date.today()
    return int(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

def sexesChef(sexe):
    if sexe=="Homme":
        return 0
    else:
        return 1

def nationalite(nat):
    if nat=="Ivoirienne":
        return 0
    else:
        return 1

def immigre(imi):
    if imi==False:
        return 0
    else:
        return 1

def niveau(niv):
    age=0
    anneP=0
    anneP=annePossible(abs(int(niv)))+anneP
    age=age+anneeEtude(niv)
    coef=float(age)/float(anneP)
    return educationM(coef)

def situation_matr(situa):
    if situa=="Marie":
        return 1
    else:
        return 0

def maladies(mal):
    if mal=="palu":
        return 1
    else:
        return 0

def occupations(occupation):
    if occupation=="Informaticien":
        return 0
    else:
        return 1

def amanegement(ville):
    if ville=="ABIDJAN":
        return 0
    else:
        return 1

def ageMenage(age):
    if int(age)<=14 and int(age)>=0:
        return 3
    elif int(age)<=24 and int(age)>=15:
        return 2
    elif int(age)<=64 and int(age)>=25:
        return 1
    else:
        return 0

def moyenneage(ages):
    age=0
    for i in ages:
        age=age+int(i)
    if len(ages)!=0:
        moyennea=age/len(ages)
    else:
        moyennea=0
    return moyennea
    
def moyennecondition(cond):
    con=0
    for i in cond:
        con=cond+i
    return con

def annePossible(age):
    return abs(age)-5

def anneeEtude(niveau):
    age=0
    if niveau=="CEPE":
        age=age+6
    elif niveau=="BEPC":
        age=age+10
    elif niveau=="BAC":
        age=age+13
    elif niveau=="BTS":
        age=age+15
    elif niveau=="DUT":
        age=age+16
    elif niveau=="LICENCE":
        age=age+16
    elif niveau=="MASTER":
        age=age+18
    elif niveau=="DOCTARAT":
        age=age+21
    elif niveau=="PROFESSEUR":
        age=age+30
    else:
        age=0
    return age

def educationM(coef):
    if abs(coef)<0.2:
        return 2
    elif abs(coef)>=0.2 and abs(coef)<0.5:
        return 1
    elif abs(coef)>=0.5 and abs(coef)<2:
        return 0
    else:
        return 46

def EducationMenage(data):
    age=0
    anneP=0
    for x in data[0]:
        anneP=annePossible(abs(int(x)))+anneP
    for z in data[1]:
        age=age+anneeEtude(z)
    coef=float(age)/float(anneP)
    return educationM(coef)

def handicap(hand):
    if hand=="Handicap_Mental":
        return 4
    elif hand=="Non_voyant":
        return 3
    elif hand in ['Handicap_membre_superieurs','Handicap_membre_inferieurs']:
        return 2
    elif hand in ['Sourd','Muet','Begue']:
        return 1
    else:
        return 0


def moyenneHand(data):
    moy=0
    for i in data:
        moy=moy+handicap(i)
    return moy

def moyenneOccup(data):
    moy=0
    for i in data:
        moy=moy+occupations(i)
    return moy    

def niveau(niv):
    age=0
    if niv=="CEPE":
        return 2
    elif niv=="BEPC":
        return 2
    elif niv=="BAC":
        return 1
    elif niv=="BTS":
        return 1
    elif niv=="DUT":
        return 0
    elif niv=="LICENCE":
        return 0
    elif niv=="MASTER":
        return 0
    elif niv=="DOCTARAT":
        return 0
    else:
        return 0
    
def moyenneNiveau(data):
    moy=0
    for i in data:
        moy=moy+niveau(i)
    return moy  

def typeMenage(type):
    if type=="Menage_non_familial":
        return 2
    elif type=="Menage_biparental_nucléaire":
        return 2
    elif type=="Ménage_Biparental_élargi":
        return 2
    elif type=="Ménage_isolé":
        return 2
    elif type=="Ménage_monoparental":
        return 2
    elif type=="Ménage_monoparental_elargi":
        return 2
    else:
        return 0


def ville(ville):
    if ville=="ABIDJAN":
        return 0
    else:
        return 1

def proprietaire(prop):
    if prop==False:
        return 0
    else:
        return 1

def accessibilite(localisation):
    pass

def EquipementMenage(data):
    if len(data)<=1:
        return 2
    elif len(data)<=4 and len(data)>1:
        return 1
    else:
        return 0

def logement1(log):
    if int(log)>3:
        return 0
    elif int(log)<3 and int(log)>1:
        return 1
    else:
        return 2

def logement2(log2):
    if log2=="BANCO":
        return 2
    elif log2=="COUR_COMMUNE":
        return 1
    else:
        return 0

def eaux(eau):
    if eau=="RIVIERE" or eau=="POMPE":
        return 2
    elif eau=="ROBINET_COMMUN":
        return 1
    else:
        return 0

def eclairages(ecl):
    if ecl=="RACCORDE":
        return 2
    elif ecl=="COMPTEUR":
        return 1
    else:
        return 0

def aisance(aise):
    if aise=="NWC":
        return 2
    elif aise=="FOSSE":
        return 1
    else:
        return 0

def combustible(comb):
    if comb=="feu_bois":
        return 2
    elif comb=="CHARBON":
        return 1
    elif comb=="gaz" or comb=="ELECTRICITE":
        return 0
        
def MoyenneEquipement(data):
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