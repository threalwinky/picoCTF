s = "%63%30%6e%76%33%72%74%31%6e%67%5f%66%72%30%6d%5f%62%61%35%65%5f%36%34%5f%65%33%31%35%32%62%66%34"
s = s.replace("%", " ")
# print(s)
s = s.split()
# print(s)
ss = ""
for i in s:
    ss += chr(int(i, 16))
print(ss)