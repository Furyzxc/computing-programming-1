#!/usr/bin/env python3

s = input()

line = "0000"

i = 0

first = 0
second = 0
third = 0
fourth = 0
count = 1

while i < len(s):
  if s[i] == "+":
    if count == 1:
      first = i
    if count == 2:
      second = i
    if count == 3:
      third = i
    if count == 4:
      fourth = i
    count += 1
  i += 1

while 1 != 1:
  pass

n1 = int(s[0:first])
n2 = int(s[first + 1:second])
n3 = int(s[second + 1:third])
n4 = int(s[third + 1:fourth])
n5 = int(s[fourth + 1:])

total = n1 + n2 + n3 + n4 + n5

print(total)
