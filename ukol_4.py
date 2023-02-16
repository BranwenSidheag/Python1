# program na zasílání SMS zpráv
tel_cislo = input("Zadejte číslo příjemce: ")
pocet_znaku = len(tel_cislo)

def overeni_cisla(pocet_znaku):
    if pocet_znaku == 9 or pocet_znaku == 13:
        print(True)
    else:
        print(False)
        return exit()

overeni_cisla(pocet_znaku)

text_zpravy = input("Zadejte text zprávy: ")
delka_zpravy = len(text_zpravy)

def cena_zpravy(delka_zpravy, sms=3):
    pocet_sms = delka_zpravy // 180

