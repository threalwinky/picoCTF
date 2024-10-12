
import sys
def getRandomNumber():
  print(4)  
def exit():
  sys.exit(0)
def esoteric1():
  esoteric = \
  print(esoteric)
def win():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)
def esoteric2():
  esoteric = \
  print(esoteric)

def filter(user_input):
  if 'win' in user_input:
    return False
  return True

while(True):
  try:
    user_input = input('==> ')
    if( filter(user_input) ):
      eval(user_input + '()')
    else:
      print('Illegal input')
  except Exception as e:
    print(e)
    break
