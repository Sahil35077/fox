
lim = int(input("limit of prime numbers : "))

for num in range(2, lim + 1):

    i = 2

    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;

    if(i != num):
        print(num, end=" ")
