def times_table():
    print("== {0} Times ==".format(int(a)))
    for i in range(1, 10):
        print("{0} * {1} = {2}".format(int(a), i, int(a) * i))
    print("== {0} Times ==".format(int(b)))
    for i in range(1, 10):
        print("{0} * {1} = {2}".format(int(b), i, int(b) * i))
a, b = input().split(' ')
times_table()