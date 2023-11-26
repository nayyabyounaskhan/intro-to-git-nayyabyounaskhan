#code to check if the entered number is prime or not?

number=input( )
def is_prime(number):
    number=int(number)  #to convert str to int
    if number < 2:
        print('Number less than 2')
        return  #exit the function if number is less than 2
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f'{number} is not a prime number')
            return  #exit the function if number is not prime
        
    print(f'{number} is a prime number')
    
is_prime(number)
