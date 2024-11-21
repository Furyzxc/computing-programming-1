#!/usr/bin/env python3

import sys

snaps = sys.stdin.read().split()

dict = {}

i = 0

while i < len(snaps):
  if snaps[i] not in dict:
    dict[snaps[i]] = 0
  else:
    print("snap:", snaps[i])
    i = len(snaps)
  i += 1
