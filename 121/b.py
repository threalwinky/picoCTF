import hashlib
a = hashlib.sha256(b'FRASER').hexdigest()
s = ""
s += a[4]
s += a[5]
s += a[3]
s += a[6]
s += a[2]
s += a[7]
s += a[1]
s += a[8]
print(s)
# print(a[4])