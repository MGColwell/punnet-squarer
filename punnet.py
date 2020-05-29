#!/usr/bin/env python3
import sys

def main(argv):
  #print (argv) #comment/uncomment for debug

  if (len(sys.argv) < 2):
    print("Needs at least 1 arg, try help")
    exit()

  if (sys.argv[1] == "help"):
    print("Create a punnet square given two text strings")
    print("Usage: ./punnet.py <firststring> <secondstring>")
    print("Example: ./punnet.py AaBB AAbB")
    exit()

  if (len(sys.argv) != 3):
    print("Invalid number of arguments. Try help.")
    exit()

  if (len(sys.argv[1]) != len(sys.argv[2])):
    print("You cannot make a punnet square out of an unequal number of genes")
    exit()

  #prints first line
  print("   ", end = "")
  for char in sys.argv[1]:
    print("  | ", end = "")
    print(char, end = "")
  print(" ")

  #prints the rest
  for char2 in sys.argv[2]:
    print(" ",char2," ", end = "")
    for char in sys.argv[1]:
      print("| ", char, char2, " ", end = "", sep = "")
    print(" ")

main(sys.argv[1:])
