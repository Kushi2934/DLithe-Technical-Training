def is_disarium(n): return n == sum(int(d)**(i+1) for i,d in enumerate(str(n)))

n = int(input("How many Disarium numbers: "))
num = found = 0
while found < n:
    if is_disarium(num):
        print(num, end=' ')
        found += 1
    num += 1

print()
a, b = map(int, input("Enter range (a b): ").split())
print(*[i for i in range(a, b+1) if is_disarium(i)])