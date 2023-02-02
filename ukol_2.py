# Úkol - Obchod se součástkami
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
key = "BAV21"
value = 54
kod_soucastky = input("Zadejte kód součastky: ")
pocet_kusu = int(input("Zadejte počet kusů: "))

if kod_soucastky in sklad:
  if pocet_kusu > value:
    print("Na skladě není požadovaný počet kusů. Lze zakoupit pouze omezené mnnožství.")
    sklad.pop(kod_soucastky)
    # print(sklad) - pro kontrolu
  else:
      print("Požadovaný počet kusů skladem.")
      sklad[key] -= pocet_kusu
      # print(sklad) - pro kontrolu
else:
  print("Omlouváme se, součastka není skladem.")

