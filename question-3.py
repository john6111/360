s = input("enter string:")

last_seen = [-1] * 26
start = 0
max_len = 0

for end in range(len(s)):
    ch = ord(s[end]) - ord('a')
    
    if last_seen[ch] >= start:
        start = last_seen[ch] + 1
    
    last_seen[ch] = end
    
    current_len = end - start + 1
    if current_len > max_len:
        max_len = current_len

print(max_len)
