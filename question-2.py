n = int(input("enter n:"))
readings = [int(x) for x in input().split()]
k = int(input("enter k:"))
current_sum = sum(readings[:k])
max_sum = current_sum
for i in range(k, n):
    current_sum = current_sum + readings[i] - readings[i - k]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)


