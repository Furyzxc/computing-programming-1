#!/usr/bin/env python3

s = input()

line = ""

while s != "end":
  line += " " + s
  s = input()

sents = " ".join(line.split()).split(".")

i = 0

while i < len(sents) - 1:
  if i < len(sents) - 1:
    print(" ".join(sents[i].split()) + ".")
  i += 1
