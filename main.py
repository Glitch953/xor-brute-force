data = []
with open("data.txt", "r") as f:
    for line in f:
        data.append(int(line))
print(data)
for key in range(256):
    result = ""
    for b in data:
        result = result + chr(b ^key)
    if result.isprintable() and result.isascii():
        print(key , result)
