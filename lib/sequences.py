# !/usr/bin/env python3

def print_fibonacci(length):
    # fib = []
    # prev = 0
    # for i in range(length):
    #     fib.append(prev + i)
    #     prev = fib[-1]
    #     # print(i, latest, f"| sum: {i+latest}")
        
    # print(fib)
    fib = []
    prev = 0
    current = 1
    
    if length == 1:
        print([prev])
        return
    if length == 0:
        print([])
        return
    
    fib.append(prev)
    fib.append(current)
    for i in range(length):
        c = prev + current
        fib.append(c)
        prev = current
        current = c
    
    print(fib[:length])
    # print(fib)
print_fibonacci(2)
