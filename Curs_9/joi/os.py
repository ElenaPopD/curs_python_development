import os
import os.path

# os.remove('test.txt')

# print(os.environ)

print(os.path.expanduser('~'))

home = os.path.expanduser('~')

doc = os.path.join(home, 'Documents')

print(doc)


lista_dir = os.getcwd().split(os.sep)[:-1]

print(lista_dir)

dir_final = os.path.join(*lista_dir)
print(dir_final)
