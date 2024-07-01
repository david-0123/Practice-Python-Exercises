num = int(input("Enter a number: "))

ans = [x for x in range(1,num+1) if num % x == 0]
print(ans)