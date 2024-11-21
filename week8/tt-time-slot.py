#!/usr/bin/env python3

s = input()
count = 0

while s != "end":
  arr = s.split()
  start = int(arr[1])
  duration = int(arr[2])
  end = str(start + duration - 1) + ":50"
  start_time = str(start) + ":00 "
  print(arr[0] + " " + start_time + end + " " + " ".join(arr[3:]))
  s = input()
