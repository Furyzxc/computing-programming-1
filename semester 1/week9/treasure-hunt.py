#!/usr/bin/env python3

import os

file_name = "start.txt"
flag = True

while flag:
  file = open(file_name)
  content = file.readline().rstrip()

  if os.path.isdir(content):
    file_name = content + "/" + os.listdir(content)[0]
  elif os.path.isfile(content):
    file_name = content
  else:
    flag = False

  file.close()

print(content)
