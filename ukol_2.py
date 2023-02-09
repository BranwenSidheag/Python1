# Úkol - Obchod se součástkami
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod_soucastky = input("Zadejte kód součastky: ")
pocet_kusu = int(input("Zadejte počet kusů: "))

if kod_soucastky in sklad:
  if sklad[kod_soucastky] < pocet_kusu:
    print("Na skladě není požadovaný počet kusů. Lze zakoupit pouze omezené mnnožství.")
    sklad.pop(kod_soucastky)
  else:
      print("Požadovaný počet kusů skladem.")
      sklad[kod_soucastky] -= pocet_kusu
else:
  print("Omlouváme se, součastka není skladem.")

  # print(sklad) - pro kontrolu