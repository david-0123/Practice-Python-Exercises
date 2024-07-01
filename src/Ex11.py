def prime(n):
    ans = [x for x in range(1,n+1) if n % x == 0]
    return len(ans) <= 2

num = int(input('Enter a number: '))
print(prime(num))