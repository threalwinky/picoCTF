# global a
# var_name = "a"
# value="a"
def win():
    print(123)
exec('global '+"a"+'; '+"a"+' = '+"123 win()")