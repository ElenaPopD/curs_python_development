def maxim(lista):
    element_maxim = lista[0]
    for element in lista:
        if element > element_maxim:
            element_maxim = element
            print("Am un maxim nou ", element_maxim)
    # return None
    # return
    # 

x = maxim([4,1,2,3,5])
print(x)
x = maxim(["Ana", "are", "mere", "MERE"])
print(x)

