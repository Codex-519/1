s = "a2b3c1"
result = ""

for i in range(0, len(s), 2):
    char = s[i]
    count = int(s[i + 1])

    result += char * count

print(result)