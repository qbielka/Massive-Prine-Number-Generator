import csv
import functools
import operator
import math
import sympy

list_of_past_primes = []


def verify_all_primes_are_really_primes(start_num=0):
    print("Verify that all calculated Primes are really prime")
    read_file_of_primes()
    for i in range(len(list_of_past_primes)-start_num):
        if start_num % 10000 == 0:
             print("Calculating Index", start_num)
        if not sympy.isprime(list_of_past_primes[start_num]):
            print("Not a Prime: ", list_of_past_primes[start_num])
        start_num += 1


def is_prime(test_prime):
    for i in range(math.floor(test_prime/2)):
        if i <= 1:
            continue
        if test_prime % i == 0:
            return False
    return True


def nextPrime():
    if len(list_of_past_primes) == 0:
        list_of_past_primes.append(2)
        return 2
    prime = list_of_past_primes[len(list_of_past_primes) - 1]
    prime += 1
    while not is_prime_within_bounds(prime):
        prime += 1
    list_of_past_primes.append(prime)
    return prime


def is_prime_within_bounds(test_prime):
    square_root_of_test = math.sqrt(test_prime)
    for previous_prime in list_of_past_primes:
        if previous_prime > (square_root_of_test + 1):
            break
        if test_prime % previous_prime == 0:
            return False
    return True


def produce_massive_prime():
    read_file_of_primes()
    prime = functools.reduce(operator.mul, list_of_past_primes, 1) + 1

    print("Prime:", prime)
    print("Size 10^", math.log(prime, 10))
    return prime


def prime_generation():
    read_file_of_primes()

    size_next = 2500

    for j in range(100):
        print(len(list_of_past_primes))
        for i in range(size_next):
            nextPrime()
        with open('primes.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(list_of_past_primes[-size_next:])


def read_file_of_primes():
    with open('primes.csv') as primes_file:
        csv_reader = csv.reader(primes_file)
        for row in csv_reader:
            for prime_number in row:
                list_of_past_primes.append(int(prime_number))

# prime_generation()
# print(list_of_past_primes)
a = produce_massive_prime()
print(a)
print(math.log(a, 10))
verify_all_primes_are_really_primes()

# TO BEAT 10^(24,862,048)
