num = int(input())

for i in (1000, 100, 10, 1):
    digits, num = divmod(num, i)
    print(digits)
