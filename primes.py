def is_prime(num):
    foundPrimes = range(2, int(num**0.5)+1)
    for factor in foundPrimes:
        if num % factor == 0:
            return False
        
    return True 

def list_primes(num_max):
    my_list = []
    for num in range(2, num_max):
        if is_prime(num):
            my_list.append(num)
            
    return my_list 