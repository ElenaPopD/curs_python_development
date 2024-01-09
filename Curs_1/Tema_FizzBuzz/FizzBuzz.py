nr_intreg = int (input ("Introudeti un numar intreg:"))
if nr_intreg % 3 == 0 and nr_intreg % 5 == 0:
    print("FizzBuzz")
elif nr_intreg % 3 == 0:
    print("Fizz")
elif nr_intreg % 5 == 0:
    print("Buzz")
else:
    print(nr_intreg)      