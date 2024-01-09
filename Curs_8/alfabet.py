def gen_alfabet():
    current = 65
    while current < 91:
        yield chr(current)
        current += 1
    
  

# for litera in gen_alfabet():
#     print(litera)
    
a = gen_alfabet()
for litera in a:
    print(litera)

print ("Dupa primul for")
for litera in a:
    print(litera)
print ("\nDupa al 2 lea  for")