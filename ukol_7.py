class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne=True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def pujc_auto(self):
        if self.dostupne == False:
            return f"Vozidlo není k dispozici."
        else:
            return f"Potvrzuji zapůjčení vozidla"
               
    def get_info(self):
        return f"{self.registracni_znacka}, {self.typ_vozidla}"
    
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
peugeot.pujc_auto()
print(peugeot)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)
print(skoda)

znacka = input("Zadejte značku auta, které chcete si chcete půjčit: ")