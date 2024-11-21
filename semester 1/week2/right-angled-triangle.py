#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

t = a * a == (b * b + c * c)

print(t or b * b == (a * a + c * c) or c * c == (a * a + b * b))
