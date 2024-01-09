def gen_elements():
    print("Inainte de 1")
    yield 1 # next
    print("Dupa 1") # <
    print("Inainte de 2")
    yield 2 # next
    print("Dupa 2")
    print("Inainte de 3")
    yield 3 # next
    print("Dupa 3")

# for element in gen_elements():
#     print(element)

el_iterator = iter(gen_elements())
print(next(el_iterator))
print(next(el_iterator))
print(next(el_iterator))
print(next(el_iterator))