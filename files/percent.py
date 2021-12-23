#!/usr/bin/python3

import sys

if len(sys.argv) <= 2:
  sys.stdout.write("Specify '-p' or '--percent' to encode with percent-encoding, or '-t' or '--text' to decode percent-encoding into plaintext. After the option, add string to be converted.\n")
  exit(1)

mode = sys.argv[1]
text = sys.argv[2]

if mode == "-p" or mode == "--percent":
  out = text.replace("%", "%25").replace(" ", "%20").replace(":", "%3A").replace("/", "%2F").replace("?", "%3F").replace("#", "%23").replace("[", "%5B").replace("]", "%5D").replace("@", "%40").replace("!", "%21").replace("$", "%24").replace("&", "%26").replace("'", "%27").replace("(", "%28").replace(")", "%29").replace("*", "%2A").replace("+", "%2B").replace(",", "%2C").replace(";", "%3B").replace("=", "%3D")
  sys.stdout.write(out + "\n")
elif mode == "-t" or mode == "--text":
  out = text.replace("%3D", "=").replace("%2C", ",").replace("%2B", "+").replace("%2A", "*").replace("%29", ")").replace("%28", "(").replace("%27", "'").replace("%26", "&").replace("%24", "$").replace("%21", "!").replace("%40", "@").replace("%5D", "]").replace("%5B", "[").replace("%23", "#").replace("%3F", "?").replace("%2F", "/").replace("%3A", ":").replace("%20", " ").replace("%25", "%")
  sys.stdout.write(out + "\n")