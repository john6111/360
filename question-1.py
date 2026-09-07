n = int(input("Enter the number of time ranges: "))
ranges = []

for i in range(n):
    print("Enter range", i + 1, "(start and end separated by space):")
    parts = input().split()
    start = int(parts[0])
    end = int(parts[1])
    ranges.append([start, end])

ranges.sort()

merged = []
merged.append(ranges[0])

for i in range(1, n):
    current_start = ranges[i][0]
    current_end = ranges[i][1]
    
    last = merged[-1]
    
    if current_start <= last[1]:
        if current_end > last[1]:
            last[1] = current_end
    else:
        merged.append([current_start, current_end])

print()
print("Consolidated time ranges:")
for r in merged:
    print(r[0], r[1])