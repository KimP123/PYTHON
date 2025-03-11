n=int(input("Enter the number: "))
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("It is not a prime number")
        else:
            print(f"{n} is a prime a prime number")
else:
    print("It's not a prime number")