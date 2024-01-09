def in_lista(element, lista):
    if element in lista:
        return True
        print("True")
    else:
        return False
        print("False")

print(in_lista(5, [1,2,3]))
print(in_lista(5, [1,2,3,5]))
