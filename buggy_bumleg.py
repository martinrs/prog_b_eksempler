import random

def checkForBUM(tal, bumtal):
    if tal % bumtal == 0 or bumtal in str(tal):
        return True
    else:
        return False

def rundeValg():
    ind = input('Hvor mange runder skal spillet vare?\n')
    if ind.isdigit():
        return int(ind)
    else:
        print('Forkert indtastning')
        return rundeValg()


def skabBumtal():
    bumtal = []
    indtastning = 'Intet indtastet'
    while indtastning != ' ' or not indtastning.isdigit():
        indtastning = input('Indtast et bumtal eller tryk ENTER for at spille ')
        if indtastning == '':
            if len(bumtal) == 0:
                bumtal.append(random.randint(1,10))
                print('Tilfældigt valgt bumtal er: {}'.format(bumtal[0]))
            return bumtal
        bumtal.append(int(indtastning))
        print(indtastning + ' tilføjet.\nBumtallene er: {}'.format(bumtal))
    return bumtal

def findVinder(fejlregnskab):
    if max(fejlregnskab.values()) == min(fejlregnskab.values()):
        print('Spillet ender uafgjort!')
    else:
        vinder = list(fejlregnskab.keys())[0]
        for spiller in fejlregnskab.keys():
            print('Spiller {}: {} fejl'.format(spiller, fejlregnskab[spiller]))
            if fejlregnskab[spiller] < fejlregnskab[vinder]:
                vinder = spiller
        print('Spiller {} vinder!'.format(vinder))


def run():
    maxtal = rundeValg()
    bumliste = skabBumtal()
    fejl = {1: 0, 2: 0}

    spiller = 1

    for i in range(1, maxtal+1):
        korrektsvar = ''
        for bum in bumliste:
            if checkForBUM(i, bum):
                korrektSvar = 'BUM'
                break
            else:
                korrektSvar = str(i)

        print('_________________')
        print('Din tur spiller {}'.format(spiller))
        svar = input('{} eller "BUM"?\n'.format(i))
        if svar.lower() == str(korrektSvar).lower():
            print('Korrekt')
        else:
            print('Forkert')
            # Opdater fejlregnskab
            fejl[spiller] += 1

        if spiller == 1:
            spiller = 2
        else:
            spiller = 1

    print('Spillet er slut!\n')

    findVinder(fejl)

if __name__ == '__main__':
    run()
