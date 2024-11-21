#!/usr/bin/env python3

a = int(input())
print(a % 4 == 0 and a % 100 != 0 or a % 400 == 0)
