import json
with open('body.json', encoding='utf-8') as soubor:
    body = json.load(soubor)
print(body)

for key, value in body.items():
    if value < 60:
        print(key + ": Fail")
        body[key] = "Fail"
    else:
        print(key + ": Pass")
        body[key] = "Pass"


with open("prospech.json", mode="w", encoding="utf-8") as file:
    json.dump(body, file)