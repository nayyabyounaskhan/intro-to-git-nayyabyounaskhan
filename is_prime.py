#code to check if the entered number is prime or not?

number=input(int())
def is_prime(number):
    number=int(number)
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
is_prime(number)
