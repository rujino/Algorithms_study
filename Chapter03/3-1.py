n = 5000
count = 0
total = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count = int(n / coin)
    n = n - count * coin
    total += count
    print(count)

print(total)
