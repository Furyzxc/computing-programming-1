#!/usr/bin/env python3

a = int(input())

middle = a % 100000 % 10000 // 100

print(middle % 10 * 10 + middle // 10)
