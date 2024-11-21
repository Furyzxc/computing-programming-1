#!/usr/bin/env python3

with open("irish-dobs.txt") as f:
  f2 = open("american-dobs.txt", "w")
  line = f.readline()
  while line != "":
    arr = line.split("/")
    arr[0], arr[1] = arr[1], arr[0]
    f2.write("/".join(arr))
    line = f.readline()
