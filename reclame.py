from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    totaal1 =  prijs * korting
    totaal = prijs - totaal1
    print(f"Vandaag in de aanbieding: 1 emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {totaal} euro.")

aanbieding_1("aardbei", 4, 0.1)
print()
print()

wekelijks = [220, 430, 125, 160, 205, 90, 345]

def inkomsten_totaal(inkomsten):

    totaal = (sum(inkomsten))
    btw = totaal * 0.09
    
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden.")
inkomsten_totaal(wekelijks)
print()
print()
def laag_en_hoog(mijn_lijst):
    print(max(mijn_lijst))
    print(min(mijn_lijst))
    return mijn_lijst
laag_en_hoog(wekelijks)
print()
print()
def gemiddelde(mijn_lijst):
    lengte = len(mijn_lijst)
    som = sum(mijn_lijst)
    gemiddelde = som / lengte
    print(f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro.")
gemiddelde(wekelijks)

print()
print()
extra_lijst = [10, 5, 3, 2, 1, 2, 9]

def meervoudig(invoer_lijst):
    laag_en_hoog(invoer_lijst)
    return invoer_lijst
meervoudig(extra_lijst)

print()
print()

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
combinatie(extra_lijst)