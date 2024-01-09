def fizzbuzz(nr):
    if nr % 15 == 0:
        return "FizzBuzz"
    elif nr % 5 == 0:
        return "Buzz"
    elif nr % 3 == 0:
        return "Fizz"
    return nr
