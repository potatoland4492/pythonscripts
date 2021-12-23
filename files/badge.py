#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
  global label
  label = input("Label: ").replace("%", "%25").replace(" ", "%20").replace(":", "%3A").replace("/", "%2F").replace("?", "%3F").replace("#", "%23").replace("[", "%5B").replace("]", "%5D").replace("@", "%40").replace("!", "%21").replace("$", "%24").replace("&", "%26").replace("'", "%27").replace("(", "%28").replace(")", "%29").replace("*", "%2A").replace("+", "%2B").replace(",", "%2C").replace(";", "%3B").replace("=", "%3D")
  global message
  message = input("Message: ").replace("%", "%25").replace(" ", "%20").replace(":", "%3A").replace("/", "%2F").replace("?", "%3F").replace("#", "%23").replace("[", "%5B").replace("]", "%5D").replace("@", "%40").replace("!", "%21").replace("$", "%24").replace("&", "%26").replace("'", "%27").replace("(", "%28").replace(")", "%29").replace("*", "%2A").replace("+", "%2B").replace(",", "%2C").replace(";", "%3B").replace("=", "%3D")
  global color
  color = input("Color: ") # No replace because color is alphanumeric and `#`
  global logo
  logo = input("Logo (hit enter to skip): ") # No replace because logo is alphanumeric
  global url
  url = "https://img.shields.io/badge/" + label + "-" + message + "-" + color
  if logo != "":
    url = url + "?logo=" + logo
  sys.stdout.write(url + "\n")
  exit()

if len(sys.argv) < 4:
  sys.stdout.write("badge.py <label> <message> <color> [logo]\nbadge.py\n")
  exit()

label = sys.argv[1].replace("%", "%25").replace(" ", "%20").replace(":", "%3A").replace("/", "%2F").replace("?", "%3F").replace("#", "%23").replace("[", "%5B").replace("]", "%5D").replace("@", "%40").replace("!", "%21").replace("$", "%24").replace("&", "%26").replace("'", "%27").replace("(", "%28").replace(")", "%29").replace("*", "%2A").replace("+", "%2B").replace(",", "%2C").replace(";", "%3B").replace("=", "%3D")
message = sys.argv[2].replace("%", "%25").replace(" ", "%20").replace(":", "%3A").replace("/", "%2F").replace("?", "%3F").replace("#", "%23").replace("[", "%5B").replace("]", "%5D").replace("@", "%40").replace("!", "%21").replace("$", "%24").replace("&", "%26").replace("'", "%27").replace("(", "%28").replace(")", "%29").replace("*", "%2A").replace("+", "%2B").replace(",", "%2C").replace(";", "%3B").replace("=", "%3D")
color = sys.argv[3]
url = "https://img.shields.io/badge/" + label + "-" + message + "-" + color

if len(sys.argv) >= 5:
  logo = sys.argv[4]
  url = url + "?logo=" + logo

sys.stdout.write(url + "\n")