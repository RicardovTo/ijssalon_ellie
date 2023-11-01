mijn_dict = {'vis' : 10, 'vlees' : 25, 'overig' : 15 }
totaal = 50
def presenteer(dict, totaal):
    verdeler = (25 * "=")
    for k, v in dict.items():
        print(k, ":", v)
    print(verdeler)
    print(f'totaal : {totaal} euro')
