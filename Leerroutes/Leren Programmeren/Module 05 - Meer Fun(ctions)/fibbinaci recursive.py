def fib(getal):
    if getal <= 2:
        return 1
    return fib(getal - 1) + fib(getal - 2)

aantal_fib = int(input("voor een nummer in voor de reeks "))
print(fib(aantal_fib))
