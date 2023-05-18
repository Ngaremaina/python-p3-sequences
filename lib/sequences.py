def print_fibonacci(length):
    mylist = []
 
    a, b = 0, 1
    while len(mylist) < length:
        mylist.append(a)
        a, b = b, a + b
    print(mylist)