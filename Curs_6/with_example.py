with open("test3.txt", "w") as f:
    f.write("Salut")
    raise ValueError()
    f.write("Nu mai ajunge in fisier")