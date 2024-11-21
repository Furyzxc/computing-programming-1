#!/usr/bin/env python3

s = input()

i = 0
res = ""

index = 0

while index < len(s) - 1 and s[index] == "0":
  index += 1

s = s[index::]

while i < len(s):
  num = s[i]
  if num == "a":
    num = "10"
  elif num == "b":
    num = "11"
  elif num == "c":
    num = "12"
  elif num == "d":
    num = "13"
  elif num == "e":
    num = "14"
  elif num == "f":
    num = "15"

  d = 0

  while str(d) != num:
    d += 1

  j = 3
  while j >= 0:
    bina = d // (2 ** j)
    d -= bina * (2 ** j)

    res += str(bina)
    j -= 1

  i += 1

k = 0

while k < len(res) and res[k] != "1" and k < 3:
  k += 1

res = res[k::]

print(res)
