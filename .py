r = int(input(""))
def product(x = []):
    a = 1
    for i in x:
        a *= i
    return a


def multiply(r):
   my_list = [i for i in range(1, r+1)]
   return product(my_list)


multiply(r)