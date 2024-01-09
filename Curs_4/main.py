f = open("studenti.csv")
filtrat = []
for line in f:
    # print(line.split(','))
    a = line.split(',')[-1].strip()
    if int(a) < 4:
        filtrat.append(line)
    # filtrat.append(line.split(','))
print(filtrat)
f.close()
f = open('filtrati.csv', mode='w')
for line in filtrat:
    f.write(line)

f.close()
