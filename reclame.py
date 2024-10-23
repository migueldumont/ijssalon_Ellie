from algemene_functies import mijn_functie_2
def aanbieding_1(smaak,prijs,korting):
    korting_1=prijs*korting
    korting_2=prijs-korting_1
    uitvoer= f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting_2} euro."
    print(uitvoer)
print(aanbieding_1("aarbei",4,0.1))

def inkomsten_totaal(inkomsten,btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal*btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} waarover {btw_bedrag} euro nbtw betaald dient te worden."
    
    
week_inkomsten=[220, 430, 125, 160, 205, 90, 345]
resultaat=inkomsten_totaal(week_inkomsten,0.09)
print(resultaat)



def laag_en_hoog(mijn_lijst):
    hoogste=max(mijn_lijst)
    laagste=min(mijn_lijst)
    return [hoogste,laagste]

uitvoer_2=laag_en_hoog(week_inkomsten)
print(uitvoer_2)

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    gemiddeld = totaal / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddeld} euro."

uitvoer_3=gemiddelde(week_inkomsten)
print(uitvoer_3)

def meervoudig(invoer_lijst):
    
    
def combinatie(invoer_lijst_2):
korte_lijst = laag_en_hoog(invoer_lijst_2)
uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
return uitvoer