#!/usr/bin/env python3

if __name__ == "__main__":
  a = []
  s = input()
  while s != "end":
    a.append(int(s))
    s = input()
  b = []
  s = input()
  while s != "end":
    b.append(int(s))
    s = input()

i = 0
j = 0
while i < len(a) and j < len(b):
  if a[i] > b[j]:
    print(b[j])
    j += 1
  else:
    print(a[i])
    i += 1

while i < len(a):
  print(a[i])
  i += 1

while j < len(b):
  print(b[j])
  j += 1
