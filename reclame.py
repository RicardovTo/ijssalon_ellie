from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = (f"Vandaag in de aanbieding: 1 emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {prijs_na_korting} euro.")
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

def space():
    print()
    print()
space()
wekelijks = (220, 430, 125, 160, 205, 90, 345)

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
        btw_bedrag = totaal * btw
    uitvoer = (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro betaald dient te worden.")
    return uitvoer
print(inkomsten_totaal(wekelijks, 0.09))

space()

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer

print(laag_en_hoog(wekelijks))

space()

def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for element in mijn_lijst:
        totaal += element
        gemiddelde = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
print(gemiddelde(wekelijks))

space()

extra_lijst = 10, 5, 3, 2, 1, 2, 9

def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer = [tijdelijk[0],tijdelijk[1]]
    return uitvoer
print(meervoudig(extra_lijst))
space()

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie(extra_lijst))