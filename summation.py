def summation_while():
    i = 1
    total = 0
    n = int(input("Choose a number: "))
    while i <= n:
        total += i
        i += 1
    print(f"Here is the sum of all the numbers from 1 to {n}: {total} ")
    
summation_while()

def summation_for():
    i = 1
    total = 0
    n = int(input("Choose a number: "))
    for i in range (n+1):
        total += i
        i += 1
    print(f"Here is the sum of all the numbers from 1 to {n}: {total} ")

summation_for()
