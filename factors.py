def factors(n):
    print(f"The Factors of {n} are:")
    for i in range(1,n+1):
        if(n%i==0):
            print(i, end=" ")


number = int(input("Enter the number you wnat to find the factors of:"))

factors(number)


