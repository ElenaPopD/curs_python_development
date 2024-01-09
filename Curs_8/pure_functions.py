def multiply_by_2(my_list):
    for index, element in enumerate(my_list):
        my_list[index] = element * 2
    return my_list

a = [1,2,3]
print(f"Inainte de apel {a}")
b = multiply_by_2(a)
print(f"Dupa apel {a}")
print(b)

# c = (1,2,3)
# d = multiply_by_2(c) # TypeError



def pure_multiply_by_2(my_list):
    return [element * 2 for element in my_list]

print("PUR")

a = [1,2,3]
print(f"Inainte de apel {a}")
b = pure_multiply_by_2(a)
print(f"Dupa apel {a}")
print(b)
c = (1,2,3)
d = pure_multiply_by_2(c)
