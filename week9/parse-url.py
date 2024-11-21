#!/usr/bin/env python3

import sys

s = sys.argv[1]

scheme, host, port, path, query, frag = "", "", "", "", "", ""

after_2_slash = s.split("://")

scheme = after_2_slash[0]

after_slash = after_2_slash[1].split("/")

host_and_port = after_slash[0].split(":")
host = host_and_port[0]
if len(host_and_port) > 1:
  port = host_and_port[1]

path_query_frag = "/".join(after_slash[1:])
path_query = path_query_frag.split("?")
path = "/" + path_query[0]

hi = True
path_frag = path_query_frag.split("#")
if len(path_frag) > 1 and len(path_query) == 1:
  frag = path_frag[1]
  path = "/" + path_frag[0]
  hi = False

size = not len(path_query_frag) > 1 and hi
if len(path_query) == 1 and path_query[0] != "" and path[-1] != "/" and size:
  path += "/"

if len(path_query) > 1:
  query_frag = path_query[1].split("#")

  query = query_frag[0]
  if len(query_frag) > 1:
    frag = query_frag[1]

print("scheme:", scheme)
if host:
  print("host:", host)
if port:
  print("port:", port)
if path:
  print("path:", path)
if query:
  print("query-string:", query)
if frag:
  print("fragment-id:", frag)
