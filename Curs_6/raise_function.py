def scrie_ceva(fisier):
    raise ValueError()
    fisier.write("\ndin functie\n")

f = open("test2.txt", "w")
try:
    f.write("Ceva")
    scrie_ceva(f)
finally:
    f.write("\nLinia de final")
    f.close()