#!/usr/bin/env python3

a = int(input())
p = int(input())
x1 = a // 1000
x2 = a % 1000 // 100
x3 = a % 1000 % 100 // 10
x4 = a % 1000 % 100 % 10


print(str(a)[::-1][p])
