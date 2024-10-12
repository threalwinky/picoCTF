f = open("flag.txt", "r").read()
f = f.split()
s = ""
for i in f:
    s += chr(int(i, 16))
print(s)
# print(chr(int(f, 16)))