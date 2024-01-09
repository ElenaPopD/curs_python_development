autori = {
    "Ion Creanga": ["Povesti din Copilarie", "Mai o carte", "Scrisoarea a 3-a"],
    "Mihai Eminescu": ["Luceafarul", "Somnoroase pasarele"],
    "Steve Jobs": [1,2,3,45,6,6,6]
}
max_lucrari = 0
castigator = ""
for autor, lista_lucrari in autori.items():
    if len(lista_lucrari) > max_lucrari:
        max_lucrari = len(lista_lucrari)
        castigator = autor

print(f"{castigator} are {max_lucrari} lucrari publicate")

opere = [["Povesti din Copilarie", "Mai o carte", "Scrisoarea a 3-a"], ["Luceafarul", "Somnoroase pasarele"], [1,2,3,45,6,6,6] ]
autori = ["Ion Creanga", "Mihai Eminescu", "Steve Jobs" ]
