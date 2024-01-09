autori = {
    "Ion Creanga": ["Povesti din Copilarie", "Mai o carte"],
    "Mihai Eminescu": ["Luceafarul", "Somnoroase pasarele"]
}
# a = [1,2]
# a = [12]

print(autori["Ion Creanga"])
#print(autori["Camil Petrescu"])
autori["Camil Petrescu"] = ["Patul lui Procust"]
print(autori)
autori["Camil Petrescu"].append("Altceva")
autori["Camil Petrescu"] = ["Nimic"]
print(autori["Camil Petrescu"])
# Pop
print("*** POP")
print(autori)
autori.pop("Ion Creanga")
print("Dupa pop")
print(autori)
autori.popitem()
#autori.popitem()
print(autori)

# GET
print(autori.get("Ceva")) # autori["Ceva"]
# if "Ceva" in autori:
#   return autori["Ceva"]
# else
#   return None
dict1 = {
    1: {"key": "value"},
    2: {"key": "value"},
    "Mihai Eminescu": 3
}
autori.update(dict1)
print(autori)