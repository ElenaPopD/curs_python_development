a = [10, 25, 38]
#a = (10, 25, 38)
#    0 1 2
primul = a[0]
al_doilea = a[1]
al_treilea = a[2]

print(primul, al_doilea, al_treilea)

primul, al_doilea, al_treilea = a

print(primul, al_doilea, al_treilea)

primul, *restul = a

print(primul, restul)

primul, al_doilea, *_ = a
*primele, ultimul = a

print(primele, ultimul)

primul, *ceva, ultimul = list(range(10))
print(primul, ceva, ultimul)

#*primele, undeva_la_mijloc, *restul = list(range(10))
#*primele, *undeva_la_mijloc, *restul = list(range(10))

