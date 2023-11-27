#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    if length == 0:
        print(fibonacci_list)
    elif length == 1:
        fibonacci_list.append(0)
        print(fibonacci_list)
    elif length == 2:
        fibonacci_list.append(0)
        fibonacci_list.append(1)
        print(fibonacci_list)
    elif length >= 3:
        fibonacci_list.append(0)
        fibonacci_list.append(1)
        for i in range(2, length):
            number = fibonacci_list[i-1] + fibonacci_list[i-2]
            fibonacci_list.append(number)
            i+=1
        print(fibonacci_list)
    
