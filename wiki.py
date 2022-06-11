# for
print(' ////// for ///// ')
print([i for i in range(1, 10, 3)])
print([i+2 for i in range(1, 10, 3)])
print([i*i for i in range(2, 10, 3)])
print([i if i%3 == 0 else i/2 for i in range(1, 10, 3)])

# 람다
print(' ////// lambda ///// ')
print(list(map(lambda x: x, list(range(1, 10, 2)))))
print(list(map(lambda x: x*x, list(range(1, 10, 2)))))
print(list(map(lambda x, y: x + y, list(range(1, 10, 2)), list(range(2, 10, 2)))))