#!/usr/bin/env python3

message = "Hello world.\n"
file_name = "hello.txt"

with open(file_name, "w") as f:
   # f is a file object opened for writing
   f.write(message)
