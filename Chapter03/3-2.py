# 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 더하여 가장 큰 수 를 만드는 것이다.
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 k번 초과하여 더해 질 수 없다.

# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번째로 큰 수

print(first, second)

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

