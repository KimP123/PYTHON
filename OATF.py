def one(n):
    return n * (n + 1) / 2
print(one(4))

def two(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(two(4))

def three(n):
    sum = 0
    for i in range (1, n+1):
        for j in range(1,i+1):
            sum += 1
    return sum
print(three(4))