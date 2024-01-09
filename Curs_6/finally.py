f = open("test1.txt", "w")
try:
    f.write("Ceva")
    raise ValueError()
    f.write("altceva")
finally:
    f.write("\nLinia de final")
    f.close()